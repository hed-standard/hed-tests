# Test schemas

Test-only HED schema libraries used by the JSON test suite, primarily by the
schema-loading tests in
`validation_test_data/SCHEMA_LOAD_FAILED.json` and
`validation_test_data/TAG_NAMESPACE_PREFIX_INVALID.json`. These libraries are
not released through hed-schemas and must never be published to the HED
schema repositories; they exist so the suite can exercise every
schema-combination rule with fully controlled vocabularies.

## Loading convention (for validator implementers)

Test cases keep plain version strings in their `schema` fields (for example
`"8.5.0, testconflict_1.0.0"`, prefixed forms included) because the tests are
about version-string and merge-group semantics. Runners resolve those version
strings against the flat folder `json_test_data/test_schemas/hedxml/` as a
local schema directory instead of the released-schema repositories. The
folder contains every merged library version plus the vendored standard
schemas, under the standard cache-convention file names
(`HED_<library>_<version>.xml`, `HED<version>.xml`), so a whole merge group
resolves against this single directory and no network access is needed.

In hed-python this is exactly:

```python
from hed.schema import load_schema_version

schema = load_schema_version(versions, xml_folder="json_test_data/test_schemas/hedxml")
```

Validators that bundle their schemas (for example hed-javascript) implement
the same rule: resolve every version string in a test's `schema` list against
this folder by cache-convention file name.

## Layout

- `hedxml/` - flat, load-ready: all merged library XML plus the vendored
  standard schemas. This is the only folder runners need.
- `<library>/hedwiki/` - hand-edited unmerged `.mediawiki` sources, the
  source of truth for each library.
- `<library>/hedxml_unmerged/` - generated unmerged XML.
- `manifest.json` - machine-readable inventory: libraries, versions, each
  version's `withStandard` partner, and the hed-schemas commit each vendored
  standard snapshot came from.

## The libraries

- **testconflict** - the primary, semver-clean library: every
  version-to-version change follows the semantic versioning rules in the HED
  specification (section 3.1.3). Unpartnered 1.x versions and 2.x versions
  partnered with standard schema 8.5.0.
- **testclash** - the conflict companion: each version carries the constant
  `Clash-tag` scaffold plus at most one probe element shared with another
  library, identical except for one controlled difference. Versions 1.0.0
  through 12.0.0 probe tag elements shared with testconflict 2.x (attribute
  value, description, ancestor path, placeholder child, rooted anchor, or a
  shared-hierarchy variation); versions 13.0.0 and later probe auxiliary
  elements shared with testaux 1.0.0 (unit class, unit, unit modifier, value
  class, or schema attribute). One conflict per version, so each load test
  isolates a single rule.
- **testminimal** - a third library name with an unchanging vocabulary:
  unpartnered 1.0.0, 2.0.0 partnered with 8.4.0, and 2.1.0 partnered with
  8.5.0, for the mismatched-partner and multi-library cases.
- **testaux** - the auxiliary-items library: a single version 1.0.0
  partnered with 8.5.0 that declares one auxiliary element of each type
  (unit class `auxUnits` with units `auxunit` and `bigauxunit`, unit
  modifier `auxMod`, value class `auxClass`, schema attribute
  `auxAttribute`) plus the tags `Aux-measure` and `Aux-value` that use
  them, so the auxiliary-section merge rules have controlled probes. The
  testclash 13.0.0+ versions carry probe copies of these elements.

Each version's prologue states its role and the semver level of its change
from the predecessor.

## Vendored standard schemas

`hedxml/HED8.5.0.xml` (prerelease snapshot) and `hedxml/HED8.4.0.xml`
(released) are vendored copies from hed-standard/hed-schemas so schema
loading is fully hermetic; their source commits are recorded in
`manifest.json`. The vendored copies stay after 8.5.0 is released.

## Regeneration

The `.mediawiki` sources are the editable source of truth. After editing
one, regenerate and commit the XML together with the edit; the pre-commit hook
and CI run `regenerate.py --check`, which fails when a committed generated
file is stale:

```bash
python src/scripts/convert_test_schemas.py
```

To update the vendored standard snapshots from a local hed-schemas checkout
(for example when the 8.5.0 prerelease changes):

```bash
python src/scripts/convert_test_schemas.py --refresh --hed-schemas <path-to-hed-schemas>
python src/scripts/regenerate.py
```

What `--refresh` does, and what to check before running it:

- `--hed-schemas` is the path of a local clone of hed-standard/hed-schemas.
  Nothing is fetched from the network.
- For each entry in `VENDORED_STANDARDS` at the top of the script (today
  `standard_schema/prerelease/HED8.5.0.xml` and
  `standard_schema/hedxml/HED8.4.0.xml`) it copies the **XML** file from that
  clone over `hedxml/<file>`. It does not read the mediawiki, so hed-schemas
  must have regenerated its XML from the mediawiki first.
- It records, in `manifest.json`, the last commit in that clone that touched
  the source path (`git log -1 -- <source_path>`). Run it with the clone on
  hed-schemas `main` after the change has merged; a refresh from an unmerged
  branch records a commit that is not on `main`.
- It then rebuilds every merged library XML in `hedxml/` against the new
  partner, which is why many `HED_<library>_<version>.xml` files change.
- `regenerate.py` afterwards keeps the consolidated JSON and the docs in step,
  so the pre-commit `regenerate.py --check` passes.

The script also verifies that no library tag name exists in that library's
standard schema partner (spec SCHEMA_LIBRARY_INVALID reason i), so edits
cannot introduce a partner collision silently.

## Consequences for validators

A validator pins this repository (hed-python as the `spec_tests/hed-tests`
submodule; hed-javascript by commit). A test case that needs something only a
newer snapshot has (for example `units-invalid-any-units` needs the `Quantity`
tag and the `anyUnits` unit class of the 8.5.0 prerelease) fails on a validator
whose pin predates the refresh. The validator either bumps its pin or skips the
case by name until it does; hed-python keeps such skips, with the reason, in
`spec_tests/test_errors.py`.
