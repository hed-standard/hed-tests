"""
Consolidate individual HED test files into unified test files for validator consumption.

This script combines separate test files from json_test_data/validation_tests/
and json_test_data/schema_tests/ into consolidated files used by validators.

Usage:
    python src/scripts/run_consolidate_tests.py
"""

import json
from pathlib import Path


def combine_tests(test_dir, output_path, exclude_prefixes=None):
    """
    Combine multiple JSON test files into a single consolidated file.

    Parameters:
        test_dir (Path): Directory containing individual test files
        output_path (Path): Path for the consolidated output file
        exclude_prefixes (list): List of filename prefixes to exclude (default: None)
    """
    if exclude_prefixes is None:
        exclude_prefixes = []

    combined_data = []

    # Get all JSON files in the directory
    test_files = sorted(test_dir.glob("*.json"))

    # Filter out excluded files
    filtered_files = [f for f in test_files if not any(f.name.startswith(prefix) for prefix in exclude_prefixes)]

    print(f"Processing {len(filtered_files)} test files from {test_dir.name}/")

    # Read and concatenate the JSON data
    for test_file in filtered_files:
        print(f"  - {test_file.name}")
        with open(test_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            # Each file contains a list of test cases
            if isinstance(data, list):
                combined_data.extend(data)
            else:
                print(f"    WARNING: {test_file.name} does not contain a list")

    # Write the combined data to output file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(combined_data, output_file, indent=4)

    print(f"Wrote {len(combined_data)} test cases to {output_path.name}")
    return len(combined_data)


def main():
    """Main function to consolidate test files."""
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

    # Exclude schema tests and deprecated tests from JavaScript consolidated file
    # (JavaScript may not need schema validation tests)
    exclude_prefixes = ["VERSION_DEPRECATED"]

    # Combine validation tests
    print("\n1. Consolidating validation tests...")
    validation_count = combine_tests(validation_tests_dir, json_test_data_dir / "validationTests.json", exclude_prefixes)

    # Combine schema tests
    print("\n2. Consolidating schema tests...")
    schema_count = combine_tests(schema_tests_dir, json_test_data_dir / "schemaTests.json", exclude_prefixes)

    # Create JavaScript consolidated file (validation tests only, excluding schema tests)
    print("\n3. Creating JavaScript consolidated file...")
    # For JavaScript, we typically don't include schema-level validation
    # So we just copy the validation tests file
    javascript_output = json_test_data_dir / "javascriptTests.json"

    # Load validation tests and write to JavaScript file
    with open(json_test_data_dir / "validationTests.json", "r", encoding="utf-8") as f:
        validation_data = json.load(f)

    with open(javascript_output, "w", encoding="utf-8") as f:
        json.dump(validation_data, f, indent=4)

    print(f"Wrote {len(validation_data)} test cases to {javascript_output.name}")

    print("\n" + "=" * 60)
    print("Consolidation complete!")
    print("=" * 60)
    print(f"Total validation tests: {validation_count}")
    print(f"Total schema tests: {schema_count}")
    print(f"JavaScript tests: {len(validation_data)}")
    print()
    print("Output files:")
    print("  - validationTests.json (all validation tests)")
    print("  - schemaTests.json (all schema tests)")
    print("  - javascriptTests.json (validation tests for JavaScript)")

    return 0


if __name__ == "__main__":
    exit(main())
