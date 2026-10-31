"""
Convert the test schema mediawiki sources to the XML files validators load.

The test schema set lives in json_test_data/test_schemas/. Each library
subdirectory holds hand-edited unmerged .mediawiki sources in hedwiki/.
This script generates, for every library version:

- <library>/hedxml_unmerged/HED_<library>_<version>.xml (unmerged XML)
- hedxml/HED_<library>_<version>.xml (merged, load-ready XML in the shared
  flat folder that also holds the vendored standard schemas)

It also verifies that no library tag name exists in the library's standard
schema partner (spec SCHEMA_LIBRARY_INVALID reason i) and regenerates
manifest.json. Generated XML is committed alongside the sources; rerun this
script after any mediawiki edit, as with consolidate_tests.py.

Usage:
    python src/scripts/convert_test_schemas.py [--refresh --hed-schemas PATH] [--verbose]

Arguments:
    --refresh: Re-copy the vendored standard schema snapshots from a local
        hed-schemas checkout (given with --hed-schemas) and record their
        source commits in manifest.json before converting.
    --hed-schemas: Path to a local hed-schemas checkout (only with --refresh).
    --verbose: Show per-file processing information.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.etree import ElementTree

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEST_SCHEMAS_DIR = PROJECT_ROOT / "json_test_data" / "test_schemas"
HEDXML_DIR = TEST_SCHEMAS_DIR / "hedxml"
MANIFEST_PATH = TEST_SCHEMAS_DIR / "manifest.json"

SOURCE_REPOSITORY = "https://github.com/hed-standard/hed-schemas"

# The vendored standard schema snapshots kept in hedxml/ so schema loading is
# fully hermetic. --refresh re-copies these from a hed-schemas checkout.
VENDORED_STANDARDS = [
    {
        "file": "HED8.5.0.xml",
        "source_path": "standard_schema/hedxml/HED8.5.0.xml",
        "released": True,
    },
    {
        "file": "HED8.4.0.xml",
        "source_path": "standard_schema/hedxml/HED8.4.0.xml",
        "released": True,
    },
    {
        "file": "HED8.3.0.xml",
        "source_path": "standard_schema/hedxml/HED8.3.0.xml",
        "released": True,
    },
    {
        "file": "HED8.2.0.xml",
        "source_path": "standard_schema/hedxml/HED8.2.0.xml",
        "released": True,
    },
    {
        "file": "HED8.1.0.xml",
        "source_path": "standard_schema/hedxml/HED8.1.0.xml",
        "released": True,
    },
    {
        "file": "HED8.0.0.xml",
        "source_path": "standard_schema/hedxml/HED8.0.0.xml",
        "released": True,
    },
]

WIKI_HEADER_RE = re.compile(r'^HED\b[^\n]*?version="(?P<version>[^"]+)"')
WITH_STANDARD_RE = re.compile(r'withStandard="(?P<partner>[^"]+)"')
TOP_TAG_RE = re.compile(r"^'''([A-Za-z0-9-]+)'''")
CHILD_TAG_RE = re.compile(r"^\*+\s*([A-Za-z0-9-]+)")


def parse_wiki_header(wiki_path: Path) -> tuple[str, str | None]:
    """Read the version and withStandard partner from a mediawiki header line.

    Parameters:
        wiki_path (Path): Path to the .mediawiki source file.

    Returns:
        tuple[str, str | None]: The version string and the partner version
            (None for an unpartnered schema).
    """
    header = wiki_path.read_text(encoding="utf-8").splitlines()[0]
    version_match = WIKI_HEADER_RE.match(header)
    if not version_match:
        raise ValueError(f"Cannot parse HED header line in {wiki_path}")
    partner_match = WITH_STANDARD_RE.search(header)
    return version_match.group("version"), partner_match.group("partner") if partner_match else None


def wiki_tag_names(wiki_path: Path) -> set[str]:
    """Collect the tag names declared in a mediawiki schema section.

    Parameters:
        wiki_path (Path): Path to the .mediawiki source file.

    Returns:
        set[str]: Lowercased tag names between the start and end schema markers.
    """
    names: set[str] = set()
    in_schema = False
    for line in wiki_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("!# start schema"):
            in_schema = True
            continue
        if stripped.startswith("!# end schema"):
            break
        if not in_schema:
            continue
        match = TOP_TAG_RE.match(line) or CHILD_TAG_RE.match(line)
        if match:
            names.add(match.group(1).lower())
    return names


def standard_tag_names(xml_path: Path) -> set[str]:
    """Collect the tag names in a standard schema XML file.

    Parameters:
        xml_path (Path): Path to the standard schema XML file.

    Returns:
        set[str]: Lowercased names of every node in the schema section.
    """
    root = ElementTree.parse(xml_path).getroot()
    schema_element = root.find("schema")
    names: set[str] = set()
    for node in schema_element.iter("node"):
        name = node.find("name")
        if name is not None and name.text:
            names.add(name.text.strip().lower())
    return names


def refresh_vendored_standards(hed_schemas_dir: Path, verbose: bool) -> dict[str, str]:
    """Re-copy the vendored standard snapshots and read their source commits.

    Parameters:
        hed_schemas_dir (Path): Local hed-schemas checkout to copy from.
        verbose (bool): Show per-file information.

    Returns:
        dict[str, str]: Map of vendored file name to source commit hash.
    """
    commits: dict[str, str] = {}
    for entry in VENDORED_STANDARDS:
        source = hed_schemas_dir / entry["source_path"]
        if not source.is_file():
            raise FileNotFoundError(f"Vendored source not found: {source}")
        target = HEDXML_DIR / entry["file"]
        shutil.copyfile(source, target)
        result = subprocess.run(
            ["git", "-C", str(hed_schemas_dir), "log", "-1", "--format=%H", "--", entry["source_path"]],
            capture_output=True,
            text=True,
            check=True,
        )
        commits[entry["file"]] = result.stdout.strip()
        if verbose:
            print(f"Refreshed {target.name} from {source} at {commits[entry['file']][:12]}")
    return commits


def existing_vendored_commits() -> dict[str, str]:
    """Read the vendored source commits recorded in the current manifest.

    Returns:
        dict[str, str]: Map of vendored file name to source commit hash.
    """
    if not MANIFEST_PATH.is_file():
        return {}
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        manifest = json.load(f)
    return {
        entry["file"].split("/")[-1]: entry.get("source_commit", "") for entry in manifest.get("vendored_standard_schemas", [])
    }


def version_sort_key(wiki_path: Path) -> tuple:
    """Order wiki files by numeric version components (2.0.0 before 10.0.0).

    Parameters:
        wiki_path (Path): A HED_<library>_<version>.mediawiki path.

    Returns:
        tuple: A key sorting numeric versions numerically; anything
            non-numeric sorts after them by file name.
    """
    version = wiki_path.stem.rsplit("_", 1)[-1]
    parts = version.split(".")
    if parts and all(part.isdigit() for part in parts):
        return (0, tuple(int(part) for part in parts), wiki_path.name)
    return (1, (), wiki_path.name)


def discover_libraries() -> list[Path]:
    """Find the library subdirectories of the test schema set.

    Returns:
        list[Path]: Sorted library directories containing a hedwiki/ folder.
    """
    return sorted(d for d in TEST_SCHEMAS_DIR.iterdir() if d.is_dir() and (d / "hedwiki").is_dir())


def check_partner_collisions(library: str, wiki_path: Path, partner: str, standard_names: dict[str, set[str]]) -> list[str]:
    """Check that no library tag name exists in the standard schema partner.

    A library schema cannot have tags that are in its standard schema partner
    (spec SCHEMA_LIBRARY_INVALID reason i).

    Parameters:
        library (str): The library name.
        wiki_path (Path): The .mediawiki source to check.
        partner (str): The withStandard partner version.
        standard_names (dict[str, set[str]]): Cache of partner tag names by version.

    Returns:
        list[str]: Error messages, empty when there is no collision.
    """
    partner_file = HEDXML_DIR / f"HED{partner}.xml"
    if partner not in standard_names:
        standard_names[partner] = standard_tag_names(partner_file)
    collisions = wiki_tag_names(wiki_path) & standard_names[partner]
    return [
        f"{wiki_path.name}: library tag '{name}' exists in standard partner {partner} (SCHEMA_LIBRARY_INVALID reason i)"
        for name in sorted(collisions)
    ]


def convert_all(verbose: bool) -> tuple[dict, list[str]]:
    """Convert every library's mediawiki sources to unmerged and merged XML.

    Parameters:
        verbose (bool): Show per-file information.

    Returns:
        tuple[dict, list[str]]: The libraries section for the manifest and a
            list of error messages (empty on success).
    """
    from hed.schema import hed_cache, load_schema

    errors: list[str] = []
    libraries: dict = {}
    standard_names: dict[str, set[str]] = {}

    # Point the hedtools cache at the vendored standards so partner resolution
    # during wiki loading is hermetic (no network, no user cache).
    with tempfile.TemporaryDirectory() as cache_dir:
        original_cache = hed_cache.HED_CACHE_DIRECTORY
        hed_cache.set_cache_directory(cache_dir)
        try:
            for entry in VENDORED_STANDARDS:
                vendored = HEDXML_DIR / entry["file"]
                if not vendored.is_file():
                    errors.append(f"Missing vendored standard schema: {vendored}")
                    return libraries, errors
                shutil.copyfile(vendored, Path(cache_dir) / entry["file"])

            for library_dir in discover_libraries():
                library = library_dir.name
                versions: dict = {}
                unmerged_dir = library_dir / "hedxml_unmerged"
                unmerged_dir.mkdir(exist_ok=True)
                for wiki_path in sorted((library_dir / "hedwiki").glob("*.mediawiki"), key=version_sort_key):
                    version, partner = parse_wiki_header(wiki_path)
                    expected_name = f"HED_{library}_{version}.mediawiki"
                    if wiki_path.name != expected_name:
                        errors.append(f"{wiki_path.name}: expected cache-convention name {expected_name}")
                        continue
                    if partner:
                        errors.extend(check_partner_collisions(library, wiki_path, partner, standard_names))
                    try:
                        schema = load_schema(str(wiki_path))
                    except Exception as e:  # noqa: BLE001 - report every load failure uniformly
                        errors.append(f"{wiki_path.name}: load failed: {e}")
                        continue
                    xml_name = f"HED_{library}_{version}.xml"
                    schema.save_as_xml(str(unmerged_dir / xml_name), save_merged=False)
                    schema.save_as_xml(str(HEDXML_DIR / xml_name), save_merged=True)
                    versions[version] = {"withStandard": partner}
                    if verbose:
                        target = "merged with " + partner if partner else "unpartnered"
                        print(f"Converted {wiki_path.name} ({target})")
                libraries[library] = {"versions": versions}
        finally:
            hed_cache.set_cache_directory(original_cache)

    return libraries, errors


def write_manifest(libraries: dict, vendored_commits: dict[str, str]):
    """Write manifest.json for the test schema set.

    Parameters:
        libraries (dict): The libraries section produced by convert_all.
        vendored_commits (dict[str, str]): Vendored file name to source commit.
    """
    manifest = {
        "description": (
            "Machine-readable inventory of the hed-tests test schema set. "
            "Regenerated by src/scripts/convert_test_schemas.py; vendored "
            "source commits are updated by its --refresh mode."
        ),
        "libraries": libraries,
        "vendored_standard_schemas": [
            {
                "file": f"hedxml/{entry['file']}",
                "source_repository": SOURCE_REPOSITORY,
                "source_path": entry["source_path"],
                "source_commit": vendored_commits.get(entry["file"], ""),
                "released": entry["released"],
            }
            for entry in VENDORED_STANDARDS
        ],
    }
    with open(MANIFEST_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=4)
        f.write("\n")


def main() -> int:
    """Convert the test schemas and regenerate the manifest.

    Returns:
        int: 0 on success, 1 on any error.
    """
    parser = argparse.ArgumentParser(description="Convert test schema mediawiki sources to XML")
    parser.add_argument("--refresh", action="store_true", help="Re-copy the vendored standard snapshots first")
    parser.add_argument("--hed-schemas", type=str, help="Path to a local hed-schemas checkout (with --refresh)")
    parser.add_argument("--verbose", action="store_true", help="Show per-file processing information")
    args = parser.parse_args()

    # Both --refresh (copy targets) and conversion (merged XML outputs) write
    # into hedxml/; make sure it exists rather than assuming it.
    HEDXML_DIR.mkdir(parents=True, exist_ok=True)

    if args.refresh:
        if not args.hed_schemas:
            print("ERROR: --refresh requires --hed-schemas <path to hed-schemas checkout>")
            return 1
        vendored_commits = refresh_vendored_standards(Path(args.hed_schemas), args.verbose)
    else:
        vendored_commits = existing_vendored_commits()

    libraries, errors = convert_all(args.verbose)
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        return 1

    write_manifest(libraries, vendored_commits)
    total = sum(len(lib["versions"]) for lib in libraries.values())
    print(f"Converted {total} schema versions in {len(libraries)} libraries; manifest.json regenerated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
