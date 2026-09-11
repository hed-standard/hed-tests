"""
Regenerate every derived file in the repository and optionally check staleness.

Runs, in order, the four generators and then mdformat on the markdown they
write, so the committed copies are always the formatted output:

1. convert_test_schemas.py  -> json_test_data/test_schemas/hedxml/*.xml, */hedxml_unmerged/*.xml, manifest.json
2. consolidate_tests.py     -> json_test_data/*.json (consolidated tests, dictionaries)
3. generate_test_index.py   -> docs/test_index.md
4. check_coverage.py        -> docs/test_coverage.md
5. mdformat --wrap no --number on docs/ and the tracked root-level *.md files

With --check the script then compares the derived paths against the git index
and exits 1 if any differ (or are untracked), listing them. The pre-commit hook
and CI both use --check, so a stale generated file can never be committed
unnoticed.

Usage:
    python src/scripts/regenerate.py          # regenerate in place
    python src/scripts/regenerate.py --check  # regenerate, then fail if anything changed
"""

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = Path("src") / "scripts"

# Paths (relative to the repository root) that the generators write.
DERIVED_PATHS = [
    "json_test_data/test_schemas/hedxml",
    "json_test_data/test_schemas/testaux/hedxml_unmerged",
    "json_test_data/test_schemas/testclash/hedxml_unmerged",
    "json_test_data/test_schemas/testconflict/hedxml_unmerged",
    "json_test_data/test_schemas/testminimal/hedxml_unmerged",
    "json_test_data/test_schemas/manifest.json",
    "json_test_data/validation_tests.json",
    "json_test_data/validation_code_dict.json",
    "json_test_data/validation_testname_dict.json",
    "json_test_data/schema_tests.json",
    "json_test_data/schema_code_dict.json",
    "json_test_data/schema_testname_dict.json",
    "docs/test_index.md",
    "docs/test_coverage.md",
]

GENERATOR_COMMANDS = [
    [str(SCRIPTS_DIR / "convert_test_schemas.py")],
    [str(SCRIPTS_DIR / "consolidate_tests.py")],
    [str(SCRIPTS_DIR / "generate_test_index.py")],
    [str(SCRIPTS_DIR / "check_coverage.py"), "--markdown", "docs/test_coverage.md"],
]


def run(cmd: list[str], cwd: Path) -> int:
    """Run a command from the repository root, echoing it first.

    Parameters:
        cmd (list[str]): Command and arguments.
        cwd (Path): Directory to run in.

    Returns:
        int: The command's exit code.
    """
    print(f"$ {' '.join(cmd)}", flush=True)
    return subprocess.run(cmd, cwd=cwd).returncode


def tracked_root_markdown(repo_root: Path) -> list[str]:
    """List the git-tracked *.md files at the repository root.

    Parameters:
        repo_root (Path): Repository root.

    Returns:
        list[str]: Relative paths, sorted.
    """
    result = subprocess.run(["git", "ls-files", "--", "*.md"], cwd=repo_root, capture_output=True, text=True, check=True)
    return sorted(line for line in result.stdout.splitlines() if line and "/" not in line)


def regenerate(repo_root: Path) -> int:
    """Run all generators and then mdformat.

    Parameters:
        repo_root (Path): Repository root.

    Returns:
        int: 0 on success, otherwise the first failing command's exit code.
    """
    for cmd in GENERATOR_COMMANDS:
        code = run([sys.executable, *cmd], repo_root)
        if code != 0:
            print(f"[FAIL] {cmd[0]} exited with {code}", file=sys.stderr)
            return code
    md_targets = ["docs", *tracked_root_markdown(repo_root)]
    code = run([sys.executable, "-m", "mdformat", "--wrap", "no", "--number", *md_targets], repo_root)
    if code != 0:
        print(f"[FAIL] mdformat exited with {code}", file=sys.stderr)
    return code


def find_stale(repo_root: Path, paths: list[str]) -> list[str]:
    """Return derived files whose working-tree content differs from the git index.

    Covers both modified tracked files and untracked files under the given
    paths, so a newly generated file that was never staged is reported too.

    Parameters:
        repo_root (Path): Repository root (must be inside a git work tree).
        paths (list[str]): Paths relative to repo_root to compare.

    Returns:
        list[str]: Relative paths of files that differ, sorted.
    """
    modified = subprocess.run(
        ["git", "diff", "--name-only", "--", *paths], cwd=repo_root, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", *paths],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.splitlines()
    return sorted({p for p in modified + untracked if p})


def main(arg_list: list[str] = None) -> int:
    """Entry point.

    Parameters:
        arg_list (list[str], optional): Arguments; defaults to sys.argv[1:].

    Returns:
        int: Exit code.
    """
    parser = argparse.ArgumentParser(description="Regenerate all derived files in hed-tests")
    parser.add_argument(
        "--check",
        action="store_true",
        help="After regenerating, exit 1 if any derived file differs from the git index",
    )
    args = parser.parse_args(arg_list)

    code = regenerate(PROJECT_ROOT)
    if code != 0:
        return code

    if args.check:
        stale = find_stale(PROJECT_ROOT, DERIVED_PATHS)
        if stale:
            print("\n[FAIL] regenerated files differ from the committed copies; stage them:", file=sys.stderr)
            for path in stale:
                print(f"  {path}", file=sys.stderr)
            return 1
        print("\n[OK] all derived files are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
