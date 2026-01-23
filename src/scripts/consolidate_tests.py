"""
Consolidate individual HED test files into unified test files for validator consumption.

This script combines separate test files from json_test_data/validation_tests/
and json_test_data/schema_tests/ into consolidated files used by validators.

Usage:
    python src/scripts/consolidate_tests.py [--dry-run] [--verbose]

Arguments:
    --dry-run: Preview consolidation without writing files
    --verbose: Show detailed processing information
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


def safe_print(text: str):
    """Print text with fallback for Unicode encoding issues."""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback to ASCII-safe characters
        safe_text = text.replace("✓", "[OK]").replace("✗", "[X]").replace("⚠", "[!]").replace("─", "-")
        print(safe_text)


class TestStatistics:
    """Track statistics about test consolidation."""

    def __init__(self):
        self.total_cases = 0
        self.error_codes: Dict[str, int] = defaultdict(int)
        self.test_types: Dict[str, int] = defaultdict(int)
        self.warnings = []
        self.errors = []
        # Maps error_code -> list of test case names using that code
        self.code_dict: Dict[str, List[str]] = defaultdict(list)
        # Maps test case name -> list of error codes (including alt_codes)
        self.name_dict: Dict[str, List[str]] = {}

    def add_test_case(self, test_case: dict):
        """Add a test case to statistics tracking."""
        self.total_cases += 1

        error_code = test_case.get("error_code", "UNKNOWN")
        self.error_codes[error_code] += 1

        # Count test types
        tests = test_case.get("tests", {})
        for test_type in ["string_tests", "sidecar_tests", "event_tests", "combo_tests"]:
            if test_type in tests and tests[test_type]:
                self.test_types[test_type] += 1

        # Build code_dict and name_dict
        name = test_case.get("name", "")
        if not name:
            return

        # Check for duplicate test case names
        if name in self.name_dict:
            self.add_error(f"Duplicate test case name: '{name}'")
            return

        # Collect all error codes (primary + alternates)
        all_codes = [error_code]
        alt_codes = test_case.get("alt_codes", [])
        if alt_codes:
            all_codes.extend(alt_codes)

        # Update name_dict: test name -> list of codes
        self.name_dict[name] = all_codes

        # Update code_dict: error code -> list of test names
        for code in all_codes:
            self.code_dict[code].append(name)

    def add_warning(self, message: str):
        """Add a warning message."""
        self.warnings.append(message)

    def add_error(self, message: str):
        """Add an error message."""
        self.errors.append(message)


def validate_test_case(test_case: dict, filename: str) -> List[str]:
    """
    Validate structure of a test case.

    Parameters:
        test_case: Test case dictionary to validate
        filename: Source filename for error reporting

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    required_fields = ["error_code", "name", "description"]

    for field in required_fields:
        if field not in test_case:
            errors.append(f"{filename}: Missing required field '{field}'")

    # Validate error_code format
    if "error_code" in test_case:
        error_code = test_case["error_code"]
        if not error_code.isupper() or not error_code.replace("_", "").isalnum():
            errors.append(f"{filename}: Invalid error_code format: {error_code}")

    # Check for tests
    if "tests" not in test_case or not test_case["tests"]:
        errors.append(f"{filename}: No tests defined in test case '{test_case.get('name', 'UNKNOWN')}'")

    return errors


def combine_tests(
    test_dir: Path, output_path: Path, exclude_prefixes: List[str] = None, dry_run: bool = False, verbose: bool = False
) -> Tuple[int, TestStatistics]:
    """
    Combine multiple JSON test files into a single consolidated file.

    Parameters:
        test_dir: Directory containing individual test files
        output_path: Path for the consolidated output file
        exclude_prefixes: List of filename prefixes to exclude
        dry_run: If True, preview without writing files
        verbose: If True, show detailed information

    Returns:
        Tuple of (total test cases, statistics object)
    """
    if exclude_prefixes is None:
        exclude_prefixes = []

    combined_data = []
    stats = TestStatistics()

    # Get all JSON files in the directory
    test_files = sorted(test_dir.glob("*.json"))

    # Filter out excluded files
    filtered_files = [f for f in test_files if not any(f.name.startswith(prefix) for prefix in exclude_prefixes)]

    print(f"\nProcessing {len(filtered_files)} test files from {test_dir.name}/")

    # Read and concatenate the JSON data
    for test_file in filtered_files:
        if verbose:
            print(f"  - {test_file.name}")

        try:
            with open(test_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Validate structure
            if not isinstance(data, list):
                warning = f"    WARNING: {test_file.name} does not contain a list"
                print(warning)
                stats.add_warning(warning)
                continue

            # Process each test case
            for test_case in data:
                # Validate test case
                validation_errors = validate_test_case(test_case, test_file.name)
                for error in validation_errors:
                    stats.add_error(error)
                    if verbose:
                        print(f"    ERROR: {error}")

                # Add to combined data and statistics
                # Note: add_test_case will check for duplicate names and add errors
                combined_data.append(test_case)
                stats.add_test_case(test_case)

        except json.JSONDecodeError as e:
            error = f"JSON decode error in {test_file.name}: {e}"
            print(f"  ERROR: {error}")
            stats.add_error(error)
            continue
        except Exception as e:
            error = f"Error processing {test_file.name}: {e}"
            print(f"  ERROR: {error}")
            stats.add_error(error)
            continue

    # Write the combined data to output file
    if not dry_run:
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as output_file:
                json.dump(combined_data, output_file, indent=4)
            safe_print(f"✓ Wrote {len(combined_data)} test cases to {output_path.name}")
        except Exception as e:
            error = f"Failed to write {output_path.name}: {e}"
            print(f"  ERROR: {error}")
            stats.add_error(error)
            return 0, stats
    else:
        print(f"[DRY RUN] Would write {len(combined_data)} test cases to {output_path.name}")

    return len(combined_data), stats


def print_statistics(stats: TestStatistics, verbose: bool = False):
    """
    Print consolidation statistics.

    Parameters:
        stats: TestStatistics object containing consolidation data
        verbose: If True, show detailed breakdown
    """
    if verbose:
        safe_print("\n" + "─" * 60)
        print("Test Statistics")
        safe_print("─" * 60)
        print(f"Total test cases: {stats.total_cases}")

        if stats.error_codes:
            print(f"\nError codes ({len(stats.error_codes)}):")
            for code, count in sorted(stats.error_codes.items()):
                print(f"  {code}: {count}")

        if stats.test_types:
            print("\nTest types:")
            for test_type, count in sorted(stats.test_types.items()):
                print(f"  {test_type}: {count}")

    if stats.warnings:
        safe_print(f"\n⚠ Warnings ({len(stats.warnings)}):")
        for warning in stats.warnings:
            print(f"  {warning}")

    if stats.errors:
        safe_print(f"\n✗ Errors ({len(stats.errors)}):")
        for error in stats.errors:
            print(f"  {error}")


def main(arg_list: List[str] = None):
    """
    Main function to consolidate test files.

    Parameters:
        arg_list: Optional list of command-line arguments to parse.
                  If None, uses sys.argv. Useful for testing or programmatic calls.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Consolidate HED test files for validator consumption")
    parser.add_argument("--dry-run", action="store_true", help="Preview consolidation without writing files")
    parser.add_argument("--verbose", action="store_true", help="Show detailed processing information")
    args = parser.parse_args(arg_list)

    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent

    # Define directories
    json_test_data_dir = project_root / "json_test_data"
    validation_tests_dir = json_test_data_dir / "validation_tests"
    schema_tests_dir = json_test_data_dir / "schema_tests"

    # Verify directories exist
    if not validation_tests_dir.exists():
        print(f"ERROR: Directory not found: {validation_tests_dir}")
        return 1

    if not schema_tests_dir.exists():
        print(f"ERROR: Directory not found: {schema_tests_dir}")
        return 1

    print("=" * 60)
    print("HED Test Consolidation")
    print("=" * 60)
    if args.dry_run:
        print("[DRY RUN MODE - No files will be written]")

    # Exclude deprecated tests from consolidated files
    exclude_prefixes = ["VERSION_DEPRECATED"]

    all_stats = TestStatistics()

    # Combine validation tests
    print("\n1. Consolidating validation tests...")
    validation_count, val_stats = combine_tests(
        validation_tests_dir,
        json_test_data_dir / "validation_tests.json",
        exclude_prefixes,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )

    # Save validation test dictionaries
    if not args.dry_run:
        try:
            with open(json_test_data_dir / "validation_code_dict.json", "w", encoding="utf-8") as f:
                json.dump(dict(val_stats.code_dict), f, indent=4)
            with open(json_test_data_dir / "validation_testname_dict.json", "w", encoding="utf-8") as f:
                json.dump(val_stats.name_dict, f, indent=4)
            if args.verbose:
                print("  Saved code_dict and name_dict")
        except Exception as e:
            error = f"Failed to write dictionary files: {e}"
            print(f"  ERROR: {error}")
            val_stats.add_error(error)

    # Merge statistics
    all_stats.total_cases += val_stats.total_cases
    for code, count in val_stats.error_codes.items():
        all_stats.error_codes[code] += count
    for test_type, count in val_stats.test_types.items():
        all_stats.test_types[test_type] += count
    all_stats.warnings.extend(val_stats.warnings)
    all_stats.errors.extend(val_stats.errors)

    if args.verbose:
        print_statistics(val_stats, verbose=True)

    # Combine schema tests
    print("\n2. Consolidating schema tests...")
    schema_count, schema_stats = combine_tests(
        schema_tests_dir,
        json_test_data_dir / "schema_tests.json",
        exclude_prefixes,
        dry_run=args.dry_run,
        verbose=args.verbose,
    )

    # Save schema test dictionaries
    if not args.dry_run:
        try:
            with open(json_test_data_dir / "schema_code_dict.json", "w", encoding="utf-8") as f:
                json.dump(dict(schema_stats.code_dict), f, indent=4)
            with open(json_test_data_dir / "schema_testname_dict.json", "w", encoding="utf-8") as f:
                json.dump(schema_stats.name_dict, f, indent=4)
            if args.verbose:
                print("  Saved code_dict and name_dict")
        except Exception as e:
            error = f"Failed to write dictionary files: {e}"
            print(f"  ERROR: {error}")
            schema_stats.add_error(error)

    # Merge statistics
    for code, count in schema_stats.error_codes.items():
        all_stats.error_codes[code] += count
    for test_type, count in schema_stats.test_types.items():
        all_stats.test_types[test_type] += count
    all_stats.warnings.extend(schema_stats.warnings)
    all_stats.errors.extend(schema_stats.errors)

    if args.verbose:
        print_statistics(schema_stats, verbose=True)

    # Print summary
    print("\n" + "=" * 60)
    print("Consolidation Summary")
    print("=" * 60)
    print(f"Validation tests: {validation_count}")
    print(f"Schema tests: {schema_count}")
    print(f"Total unique error codes: {len(all_stats.error_codes)}")
    print()
    print("Output files:")
    print("  - validation_tests.json (all validation tests)")
    print("  - validation_code_dict.json (error codes to test names)")
    print("  - validation_testname_dict.json (test names to error codes)")
    print("  - schema_tests.json (all schema tests)")
    print("  - schema_code_dict.json (error codes to test names)")
    print("  - schema_testname_dict.json (test names to error codes)")

    # Print overall statistics
    if args.verbose:
        print_statistics(all_stats, verbose=True)
    elif all_stats.warnings or all_stats.errors:
        print_statistics(all_stats, verbose=False)

    # Return appropriate exit code
    if all_stats.errors:
        safe_print("\n✗ Consolidation completed with errors")
        return 1
    elif all_stats.warnings:
        safe_print("\n⚠ Consolidation completed with warnings")
        return 0
    else:
        safe_print("\n✓ Consolidation completed successfully")
        return 0


if __name__ == "__main__":
    exit(main())
