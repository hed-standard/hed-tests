"""
Validate HED test files against the official JSON schema.

This script validates all test files in json_test_data/ to ensure they
conform to the official test structure schema. It checks:
- JSON syntax validity
- Required fields presence
- Field type correctness
- Proper test structure
- Validation cases use the default standard schema (DEFAULT_STANDARD_SCHEMA)
  unless the case is about an earlier version and its name says so

Usage:
    python src/scripts/validate_test_structure.py
    python src/scripts/validate_test_structure.py json_test_data/validation_tests
    python src/scripts/validate_test_structure.py --file <path>
    python src/scripts/validate_test_structure.py --verbose
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("ERROR: jsonschema package not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)

# The standard schema every validation case uses unless the case is about a difference between versions.
DEFAULT_STANDARD_SCHEMA = "8.5.0"

# A case on an earlier standard schema must say so at the end of its name: the version (-8-0-0, -in-8-1-0,
# -before-8-5-0) or -early-schema.
EARLIER_SCHEMA_NAME = re.compile(r"-(\d+-\d+-\d+|early-schema)$")

# Cases on an earlier standard schema whose names do not end in the version. Keep this list short.
EARLIER_SCHEMA_CASES: frozenset[str] = frozenset()

STANDARD_VERSION = re.compile(r"^\d+\.\d+\.\d+$")


def check_default_schema(cases: list) -> list[str]:
    """
    Report validation cases that name a single standard schema other than the default without saying why.

    Parameters:
        cases (list): The parsed contents of one validation test data file.

    Returns:
        list[str]: One message per offending case; empty when every case conforms.
    """
    errors = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            continue
        schema = case.get("schema")
        name = case.get("name", "")
        if not isinstance(schema, str) or not STANDARD_VERSION.match(schema) or schema == DEFAULT_STANDARD_SCHEMA:
            continue
        if not isinstance(name, str):
            continue  # a malformed name is reported by the JSON Schema validation

        if EARLIER_SCHEMA_NAME.search(name) or name in EARLIER_SCHEMA_CASES:
            continue
        errors.append(
            f"  [{index} -> schema] case '{name}' uses standard schema {schema}; use {DEFAULT_STANDARD_SCHEMA}, "
            f"or, if the case is about an earlier version, end its name with the version (for example -{schema.replace('.', '-')})"
        )
    return errors


class TestValidator:
    """Validator for HED test files."""

    def __init__(self, schema_path: Path):
        """
        Initialize the validator with the JSON schema.

        Parameters:
            schema_path (Path): Path to the test schema JSON file
        """
        self.schema_path = schema_path
        self.schema = self._load_schema()
        self.validator = Draft7Validator(self.schema)

    def _load_schema(self) -> dict:
        """Load the JSON schema from file."""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema not found: {self.schema_path}")

        with open(self.schema_path, encoding="utf-8") as f:
            return json.load(f)

    def validate_file(self, test_file: Path) -> tuple[bool, list[str]]:
        """
        Validate a single test file.

        Parameters:
            test_file (Path): Path to the test file

        Returns:
            Tuple[bool, List[str]]: (is_valid, list_of_errors)
        """
        errors = []

        # Check file exists
        if not test_file.exists():
            return False, [f"File not found: {test_file}"]

        # Load and parse JSON
        try:
            with open(test_file, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            return False, [f"JSON syntax error: {e}"]
        except Exception as e:
            return False, [f"Error reading file: {e}"]

        # Validate against schema
        validation_errors = list(self.validator.iter_errors(data))

        if validation_errors:
            for error in validation_errors:
                # Format error message with path
                path = " -> ".join(str(p) for p in error.path) if error.path else "root"
                errors.append(f"  [{path}] {error.message}")

        # Validation cases use the default standard schema
        if test_file.parent.name == "validation_test_data" and isinstance(data, list):
            errors.extend(check_default_schema(data))

        return len(errors) == 0, errors

    def validate_directory(self, directory: Path, recursive: bool = False) -> dict[str, tuple[bool, list[str]]]:
        """
        Validate all JSON files in a directory.

        Parameters:
            directory (Path): Directory to validate
            recursive (bool): Whether to search subdirectories

        Returns:
            Dict[str, Tuple[bool, List[str]]]: Results by filename
        """
        results = {}

        if recursive:
            json_files = directory.rglob("*.json")
        else:
            json_files = directory.glob("*.json")

        for json_file in sorted(json_files):
            # Skip consolidated files and dictionaries
            if json_file.name in [
                "validation_tests.json",
                "schema_tests.json",
                "validation_code_dict.json",
                "validation_testname_dict.json",
                "schema_code_dict.json",
                "schema_testname_dict.json",
            ]:
                continue

            is_valid, errors = self.validate_file(json_file)
            results[str(json_file.relative_to(directory.parent.parent))] = (is_valid, errors)

        return results


def print_results(results: dict[str, tuple[bool, list[str]]], verbose: bool = False):
    """
    Print validation results.

    Parameters:
        results (Dict): Validation results
        verbose (bool): Whether to show details for passing files
    """
    total = len(results)
    passed = sum(1 for is_valid, _ in results.values() if is_valid)
    failed = total - passed

    print("\n" + "=" * 70)
    print("HED Test Structure Validation Results")
    print("=" * 70)

    # Show failures
    if failed > 0:
        print(f"\n[FAIL] FAILED: {failed} file(s)\n")
        for filename, (is_valid, errors) in results.items():
            if not is_valid:
                print(f"[FAIL] {filename}")
                for error in errors:
                    print(f"   {error}")
                print()
    else:
        print("\n[PASS] All files passed validation!")

    # Show passes
    if verbose and passed > 0:
        print(f"\n[PASS] PASSED: {passed} file(s)\n")
        for filename, (is_valid, _) in results.items():
            if is_valid:
                print(f"[PASS] {filename}")

    # Summary
    print("\n" + "=" * 70)
    print(f"Total: {total} | Passed: {passed} | Failed: {failed}")
    print("=" * 70)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Validate HED test files against JSON schema")
    parser.add_argument(
        "directory", type=str, nargs="?", help="Directory to validate (default: validate all test directories)"
    )
    parser.add_argument("--file", type=str, help="Validate a specific file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show details for passing files")
    parser.add_argument("--schema", type=str, help="Path to schema file (default: src/schemas/test_schema.json)")

    args = parser.parse_args()

    # Get project root and paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    json_test_data_dir = project_root / "json_test_data"

    # Determine schema path
    if args.schema:
        schema_path = Path(args.schema)
    else:
        schema_path = project_root / "src" / "schemas" / "test_schema.json"

    print(f"Using schema: {schema_path}")

    # Create validator
    try:
        validator = TestValidator(schema_path)
    except Exception as e:
        print(f"ERROR: Failed to load schema: {e}")
        return 1

    # Validate
    if args.file:
        # Validate single file
        test_file = Path(args.file)
        is_valid, errors = validator.validate_file(test_file)

        if is_valid:
            print(f"[PASS] {test_file} is valid")
            return 0
        else:
            print(f"[FAIL] {test_file} is invalid:")
            for error in errors:
                print(f"   {error}")
            return 1
    elif args.directory:
        # Validate specified directory
        target_dir = Path(args.directory)
        if not target_dir.exists():
            print(f"ERROR: Directory not found: {target_dir}")
            return 1

        results = validator.validate_directory(target_dir)

        # Print results
        print_results(results, verbose=args.verbose)

        # Exit with error if any failures
        failed_count = sum(1 for is_valid, _ in results.values() if not is_valid)
        return 1 if failed_count > 0 else 0
    else:
        # Validate all files
        results = {}

        # Validate validation_test_data
        validation_tests_dir = json_test_data_dir / "validation_test_data"
        if validation_tests_dir.exists():
            results.update(validator.validate_directory(validation_tests_dir))

        # Validate schema_test_data
        schema_tests_dir = json_test_data_dir / "schema_test_data"
        if schema_tests_dir.exists():
            results.update(validator.validate_directory(schema_tests_dir))

        # Print results
        print_results(results, verbose=args.verbose)

        # Exit with error if any failures
        failed_count = sum(1 for is_valid, _ in results.values() if not is_valid)
        return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
