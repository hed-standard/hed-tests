"""
Generate comprehensive index of all HED test cases.

This script creates a searchable index of all test cases in the suite,
organized by error code, with links to test files and detailed metadata.

Usage:
    python src/scripts/generate_test_index.py
    python src/scripts/generate_test_index.py --output docs/test_index.md
    python src/scripts/generate_test_index.py --format json
"""

import argparse
import json
from pathlib import Path


class TestIndexGenerator:
    """Generator for test suite index."""

    def __init__(self, test_data_dir: Path):
        """
        Initialize the index generator.

        Parameters:
            test_data_dir (Path): Path to json_test_data directory
        """
        self.test_data_dir = test_data_dir
        self.index_data = []

    def generate(self):
        """Generate index from all test files."""
        # Process validation tests
        validation_dir = self.test_data_dir / "validation_tests"
        if validation_dir.exists():
            self._process_directory(validation_dir, "validation")

        # Process schema tests
        schema_dir = self.test_data_dir / "schema_tests"
        if schema_dir.exists():
            self._process_directory(schema_dir, "schema")

        # Sort by error code then by name
        self.index_data.sort(key=lambda x: (x["error_code"], x["name"]))

    def _process_directory(self, directory: Path, category: str):
        """
        Process test files in a directory.

        Parameters:
            directory (Path): Directory to process
            category (str): Category name
        """
        for test_file in sorted(directory.glob("*.json")):
            try:
                with open(test_file, "r", encoding="utf-8") as f:
                    test_data = json.load(f)

                if not isinstance(test_data, list):
                    continue

                for test_case in test_data:
                    self._process_test_case(test_case, test_file, category)

            except Exception as e:
                print(f"ERROR: Failed to process {test_file.name}: {e}")

    def _process_test_case(self, test_case: dict, test_file: Path, category: str):
        """
        Process a single test case.

        Parameters:
            test_case (dict): Test case data
            test_file (Path): Source file
            category (str): Test category
        """
        # Extract test counts
        tests = test_case.get("tests", {})
        test_counts = {}
        for test_type, test_data in tests.items():
            fail_count = len(test_data.get("fails", []))
            pass_count = len(test_data.get("passes", []))
            if fail_count > 0 or pass_count > 0:
                test_counts[test_type] = {"fail": fail_count, "pass": pass_count}

        # Build index entry
        entry = {
            "error_code": test_case.get("error_code", "UNKNOWN"),
            "name": test_case.get("name", "unnamed"),
            "description": test_case.get("description", ""),
            "warning": test_case.get("warning", False),
            "schema": test_case.get("schema", ""),
            "category": category,
            "file": test_file.name,
            "test_counts": test_counts,
            "error_category": test_case.get("error_category", ""),
            "has_ai_metadata": all(k in test_case for k in ["common_causes", "explanation", "correction_strategy"]),
            "has_correction_examples": "correction_examples" in test_case,
        }

        self.index_data.append(entry)

    def generate_markdown(self, output_file: Path):
        """
        Generate markdown index.

        Parameters:
            output_file (Path): Path to output file
        """
        lines = [
            "# HED Test Suite Index",
            "",
            f"Complete index of {len(self.index_data)} test cases in the HED test suite.",
            "",
            "## Quick Navigation",
            "",
        ]

        # Create navigation links by error code
        error_codes = sorted({entry["error_code"] for entry in self.index_data})
        for error_code in error_codes:
            count = sum(1 for e in self.index_data if e["error_code"] == error_code)
            lines.append(f"- [{error_code}](#{error_code.lower().replace('_', '-')}) ({count} tests)")

        lines.append("")

        # Generate detailed entries by error code
        current_error_code = None
        for entry in self.index_data:
            error_code = entry["error_code"]

            # New error code section
            if error_code != current_error_code:
                current_error_code = error_code
                lines.extend(
                    [
                        "",
                        f"## {error_code}",
                        "",
                        f"**File**: `json_test_data/{entry['category']}_tests/{entry['file']}`",
                        "",
                    ]
                )

            # Test case entry
            warning_badge = " ⚠️ Warning" if entry["warning"] else ""
            ai_badge = " 🤖 AI" if entry["has_ai_metadata"] else ""
            examples_badge = " 📝 Examples" if entry["has_correction_examples"] else ""

            lines.extend(
                [
                    f"### {entry['name']}{warning_badge}{ai_badge}{examples_badge}",
                    "",
                    f"**Description**: {entry['description']}",
                    "",
                ]
            )

            # Schema version
            schema = entry["schema"]
            if isinstance(schema, list):
                schema_str = ", ".join(schema)
            else:
                schema_str = schema or "any"
            lines.append(f"**Schema**: {schema_str}")

            # Error category
            if entry["error_category"]:
                lines.append(f"**Category**: {entry['error_category']}")

            # Test counts
            if entry["test_counts"]:
                lines.append("")
                lines.append("**Tests**:")
                for test_type, counts in entry["test_counts"].items():
                    lines.append(f"- `{test_type}`: {counts['fail']} fail, {counts['pass']} pass")

            lines.append("")

        # Write to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"✅ Markdown index written to: {output_file}")

    def generate_json(self, output_file: Path):
        """
        Generate JSON index.

        Parameters:
            output_file (Path): Path to output file
        """
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(self.index_data, f, indent=2)

        print(f"✅ JSON index written to: {output_file}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Generate HED test suite index")
    parser.add_argument(
        "--output", type=str, default="docs/test_index.md", help="Output file path (default: docs/test_index.md)"
    )
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown", help="Output format (default: markdown)")

    args = parser.parse_args()

    # Get paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    test_data_dir = project_root / "json_test_data"

    if not test_data_dir.exists():
        print(f"ERROR: Test data directory not found: {test_data_dir}")
        return 1

    # Generate index
    print("Generating test index...")
    generator = TestIndexGenerator(test_data_dir)
    generator.generate()

    print(f"Found {len(generator.index_data)} test cases")

    # Generate output
    output_path = project_root / args.output

    if args.format == "markdown":
        generator.generate_markdown(output_path)
    else:
        generator.generate_json(output_path)

    return 0


if __name__ == "__main__":
    exit(main())
