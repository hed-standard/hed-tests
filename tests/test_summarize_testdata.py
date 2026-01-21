"""
Test utilities for analyzing HED test data structure and coverage.

This module provides tools to summarize test cases, check coverage,
and validate test file structure.
"""

import json
import os
import unittest
from pathlib import Path


class TestSummarizeTestData(unittest.TestCase):
    """Test case for summarizing and analyzing HED test data."""

    @classmethod
    def setUpClass(cls):
        """Set up test file paths."""
        # Get project root (two levels up from tests directory)
        project_root = Path(__file__).parent.parent
        json_test_data_dir = project_root / "json_test_data"

        # Collect all test files from both directories
        cls.test_files = []
        
        validation_tests_dir = json_test_data_dir / "validation_tests"
        if validation_tests_dir.exists():
            cls.test_files.extend(validation_tests_dir.glob("*.json"))
        
        schema_tests_dir = json_test_data_dir / "schema_tests"
        if schema_tests_dir.exists():
            cls.test_files.extend(schema_tests_dir.glob("*.json"))

        cls.test_files = sorted(cls.test_files)
        print(f"\nFound {len(cls.test_files)} test files")

    @staticmethod
    def get_test_info(test_file, details=True):
        """
        Extract and format test information from a test file.

        Parameters:
            test_file (Path): Path to the test file
            details (bool): Whether to include detailed test listings

        Returns:
            str: Formatted test information
        """
        indent = "   "
        with open(test_file, encoding='utf-8') as fp:
            test_info = json.load(fp)
        
        if not test_info:
            return f"EMPTY FILE: {test_file.name}"

        out_list = [f"\n{'='*60}"]
        out_list.append(f"FILE: {test_file.name}")
        out_list.append(f"ERROR CODE: {test_info[0]['error_code']}")
        out_list.append(f"TEST CASES: {len(test_info)}")
        out_list.append('='*60)

        for info in test_info:
            out_list.append(f"\n{indent}Name: {info['name']}")
            out_list.append(f"{indent}Description: {info['description']}")
            out_list.append(f"{indent}Schema: {info['schema']}")
            out_list.append(f"{indent}Warning: {info.get('warning', False)}")
            
            # Show AI-friendly metadata if present
            if 'error_category' in info:
                out_list.append(f"{indent}Category: {info['error_category']}")
            if 'common_causes' in info:
                out_list.append(f"{indent}Common causes: {len(info['common_causes'])} listed")
            if 'correction_examples' in info:
                out_list.append(f"{indent}Correction examples: {len(info['correction_examples'])}")
            
            # Show definitions if present
            definitions = info.get("definitions", [])
            if definitions:
                out_list.append(f"{indent}Definitions: {len(definitions)}")
                if details:
                    for def_str in definitions:
                        out_list.append(f"{indent*2}{def_str}")
            
            # Show test counts
            tests = info.get('tests', {})
            if 'string_tests' in tests:
                out_list.extend(
                    TestSummarizeTestData.get_test_details(
                        tests["string_tests"], "string_tests", indent, details
                    )
                )
            if 'sidecar_tests' in tests:
                out_list.extend(
                    TestSummarizeTestData.get_test_details(
                        tests["sidecar_tests"], "sidecar_tests", indent, details
                    )
                )
            if 'event_tests' in tests:
                out_list.extend(
                    TestSummarizeTestData.get_test_details(
                        tests["event_tests"], "event_tests", indent, details
                    )
                )
            if 'combo_tests' in tests:
                out_list.extend(
                    TestSummarizeTestData.get_test_details(
                        tests["combo_tests"], "combo_tests", indent, details
                    )
                )
        
        return "\n".join(out_list)

    @staticmethod
    def get_test_details(test_item, title, indent, details=True):
        """
        Format details for a specific test type.

        Parameters:
            test_item (dict): Test item containing fails/passes
            title (str): Test type title
            indent (str): Indentation string
            details (bool): Whether to show detailed test listings

        Returns:
            list: List of formatted strings
        """
        num_fail_tests = len(test_item.get("fails", []))
        num_pass_tests = len(test_item.get("passes", []))
        detail_list = [
            f"{indent*2}{title}: fail={num_fail_tests} pass={num_pass_tests}"
        ]
        
        if details:
            if num_fail_tests > 0:
                detail_list.append(f"{indent*3}Fail tests:")
                for test in test_item["fails"][:3]:  # Show first 3 examples
                    test_str = str(test)[:100]  # Truncate long tests
                    detail_list.append(f"{indent*4}{test_str}")
                if num_fail_tests > 3:
                    detail_list.append(f"{indent*4}... and {num_fail_tests - 3} more")
            
            if num_pass_tests > 0:
                detail_list.append(f"{indent*3}Pass tests:")
                for test in test_item["passes"][:3]:  # Show first 3 examples
                    test_str = str(test)[:100]  # Truncate long tests
                    detail_list.append(f"{indent*4}{test_str}")
                if num_pass_tests > 3:
                    detail_list.append(f"{indent*4}... and {num_pass_tests - 3} more")
        
        return detail_list

    def test_summary(self):
        """Generate summary of all test files."""
        print("\n" + "="*60)
        print("HED TEST SUITE SUMMARY")
        print("="*60)
        
        for test_file in self.test_files:
            out_str = self.get_test_info(test_file, details=False)
            print(out_str)
        
        print("\n" + "="*60)
        print(f"TOTAL: {len(self.test_files)} test files")
        print("="*60)

    def test_detailed_summary(self):
        """Generate detailed summary with test examples."""
        for test_file in self.test_files:
            out_str = self.get_test_info(test_file, details=True)
            print(out_str)


if __name__ == "__main__":
    unittest.main()
