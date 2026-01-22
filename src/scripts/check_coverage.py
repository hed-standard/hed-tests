"""
Check test coverage across HED error codes.

This script analyzes the test suite to report:
- Which error codes have tests
- Number of test cases per error code
- Test types available (string/sidecar/event/combo)
- AI metadata completeness
- Coverage gaps

Usage:
    python src/scripts/check_coverage.py
    python src/scripts/check_coverage.py --markdown report.md
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict


class CoverageAnalyzer:
    """Analyzer for test coverage statistics."""

    def __init__(self, test_data_dir: Path):
        """
        Initialize the coverage analyzer.

        Parameters:
            test_data_dir (Path): Path to json_test_data directory
        """
        self.test_data_dir = test_data_dir
        self.coverage_data = defaultdict(
            lambda: {
                "test_cases": 0,
                "files": [],
                "test_types": set(),
                "has_ai_metadata": False,
                "schema_versions": set(),
                "warning_count": 0,
                "error_count": 0,
            }
        )

    def analyze(self):
        """Analyze all test files and collect coverage statistics."""
        # Analyze validation tests
        validation_dir = self.test_data_dir / "validation_tests"
        if validation_dir.exists():
            self._analyze_directory(validation_dir, "validation")

        # Analyze schema tests
        schema_dir = self.test_data_dir / "schema_tests"
        if schema_dir.exists():
            self._analyze_directory(schema_dir, "schema")

    def _analyze_directory(self, directory: Path, category: str):
        """
        Analyze test files in a directory.

        Parameters:
            directory (Path): Directory to analyze
            category (str): Category name ("validation" or "schema")
        """
        for test_file in sorted(directory.glob("*.json")):
            try:
                with open(test_file, "r", encoding="utf-8") as f:
                    test_data = json.load(f)

                if not isinstance(test_data, list):
                    print(f"WARNING: {test_file.name} is not a list")
                    continue

                for test_case in test_data:
                    error_code = test_case.get("error_code", "UNKNOWN")
                    self._process_test_case(error_code, test_case, test_file, category)

            except json.JSONDecodeError as e:
                print(f"ERROR: Failed to parse {test_file.name}: {e}")
            except Exception as e:
                print(f"ERROR: Failed to process {test_file.name}: {e}")

    def _process_test_case(self, error_code: str, test_case: dict, test_file: Path, category: str):
        """
        Process a single test case.

        Parameters:
            error_code (str): Error code
            test_case (dict): Test case data
            test_file (Path): Source file
            category (str): Test category
        """
        data = self.coverage_data[error_code]

        # Count test case
        data["test_cases"] += 1

        # Track file
        if test_file.name not in data["files"]:
            data["files"].append(test_file.name)

        # Identify test types
        tests = test_case.get("tests", {})
        for test_type in tests.keys():
            data["test_types"].add(test_type)

        # Check AI metadata
        if all(key in test_case for key in ["common_causes", "explanation", "correction_strategy"]):
            data["has_ai_metadata"] = True

        # Track schema versions
        schema = test_case.get("schema", "")
        if isinstance(schema, str) and schema:
            data["schema_versions"].add(schema)
        elif isinstance(schema, list):
            data["schema_versions"].update(schema)

        # Count warnings vs errors
        if test_case.get("warning", False):
            data["warning_count"] += 1
        else:
            data["error_count"] += 1

    def get_summary(self) -> Dict:
        """
        Get summary statistics.

        Returns:
            Dict: Summary statistics
        """
        total_codes = len(self.coverage_data)
        total_test_cases = sum(data["test_cases"] for data in self.coverage_data.values())
        codes_with_ai = sum(1 for data in self.coverage_data.values() if data["has_ai_metadata"])

        test_type_counts = defaultdict(int)
        for data in self.coverage_data.values():
            for test_type in data["test_types"]:
                test_type_counts[test_type] += 1

        return {
            "total_error_codes": total_codes,
            "total_test_cases": total_test_cases,
            "codes_with_ai_metadata": codes_with_ai,
            "test_type_coverage": dict(test_type_counts),
            "ai_metadata_percentage": (codes_with_ai / total_codes * 100) if total_codes > 0 else 0,
        }

    def print_report(self):
        """Print coverage report to console."""
        summary = self.get_summary()

        print("\n" + "=" * 70)
        print("HED Test Coverage Report")
        print("=" * 70)

        # Summary statistics
        print("\n[SUMMARY] Summary Statistics")
        print(f"  Total error codes covered: {summary['total_error_codes']}")
        print(f"  Total test cases: {summary['total_test_cases']}")
        print(
            f"  Error codes with AI metadata: {summary['codes_with_ai_metadata']} "
            f"({summary['ai_metadata_percentage']:.1f}%)"
        )

        # Test type coverage
        print("\n[TYPES] Test Type Coverage")
        for test_type, count in sorted(summary["test_type_coverage"].items()):
            print(f"  {test_type}: {count} error codes")

        # Detailed coverage by error code
        print("\n[DETAILS] Coverage by Error Code")
        print(f"{'Error Code':<35} {'Cases':<8} {'Types':<25} {'AI':<5}")
        print("-" * 70)

        for error_code in sorted(self.coverage_data.keys()):
            data = self.coverage_data[error_code]
            test_types_str = ", ".join(sorted(data["test_types"]))[:20]
            ai_marker = "+" if data["has_ai_metadata"] else "-"

            print(f"{error_code:<35} {data['test_cases']:<8} {test_types_str:<25} {ai_marker:<5}")

        print("=" * 70)

    def generate_markdown(self, output_file: Path):
        """
        Generate markdown coverage report.

        Parameters:
            output_file (Path): Path to output markdown file
        """
        summary = self.get_summary()

        lines = [
            "# HED Test Coverage Report",
            "",
            f"**Generated**: {Path.cwd()}",
            "",
            "## Summary Statistics",
            "",
            f"- **Total error codes covered**: {summary['total_error_codes']}",
            f"- **Total test cases**: {summary['total_test_cases']}",
            f"- **Error codes with AI metadata**: {summary['codes_with_ai_metadata']} "
            f"({summary['ai_metadata_percentage']:.1f}%)",
            "",
            "## Test Type Coverage",
            "",
        ]

        for test_type, count in sorted(summary["test_type_coverage"].items()):
            lines.append(f"- **{test_type}**: {count} error codes")

        lines.extend(
            [
                "",
                "## Coverage by Error Code",
                "",
                "| Error Code | Test Cases | Test Types | AI Metadata | Schema Versions |",
                "|------------|------------|------------|-------------|-----------------|",
            ]
        )

        for error_code in sorted(self.coverage_data.keys()):
            data = self.coverage_data[error_code]
            test_types_str = ", ".join(sorted(data["test_types"]))
            ai_marker = "✓" if data["has_ai_metadata"] else "✗"
            schemas = ", ".join(sorted(data["schema_versions"]))[:30]

            lines.append(f"| {error_code} | {data['test_cases']} | {test_types_str} | {ai_marker} | {schemas} |")

        lines.extend(
            [
                "",
                "## Files",
                "",
            ]
        )

        # Group files by error code
        for error_code in sorted(self.coverage_data.keys()):
            data = self.coverage_data[error_code]
            lines.append(f"### {error_code}")
            for filename in data["files"]:
                lines.append(f"- `{filename}`")
            lines.append("")

        # Write to file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"\n[SUCCESS] Markdown report written to: {output_file}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Check HED test coverage")
    parser.add_argument("--markdown", type=str, help="Generate markdown report at specified path")

    args = parser.parse_args()

    # Get paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    test_data_dir = project_root / "json_test_data"

    if not test_data_dir.exists():
        print(f"ERROR: Test data directory not found: {test_data_dir}")
        return 1

    # Analyze coverage
    analyzer = CoverageAnalyzer(test_data_dir)
    analyzer.analyze()

    # Print console report
    analyzer.print_report()

    # Generate markdown if requested
    if args.markdown:
        output_path = Path(args.markdown)
        analyzer.generate_markdown(output_path)

    return 0


if __name__ == "__main__":
    exit(main())
