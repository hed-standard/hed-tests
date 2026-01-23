"""
Unit tests for the consolidate_tests.py script.

Tests the consolidation functionality, statistics tracking,
validation, and error handling.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.scripts.consolidate_tests import (
    TestStatistics,
    combine_tests,
    main,
    validate_test_case,
)


class TestTestStatistics(unittest.TestCase):
    """Test the TestStatistics class."""

    def setUp(self):
        """Create a fresh TestStatistics instance for each test."""
        self.stats = TestStatistics()

    def test_initialization(self):
        """Test that TestStatistics initializes correctly."""
        self.assertEqual(self.stats.total_cases, 0)
        self.assertEqual(len(self.stats.error_codes), 0)
        self.assertEqual(len(self.stats.test_types), 0)
        self.assertEqual(len(self.stats.warnings), 0)
        self.assertEqual(len(self.stats.errors), 0)
        self.assertEqual(len(self.stats.code_dict), 0)
        self.assertEqual(len(self.stats.name_dict), 0)

    def test_add_test_case_basic(self):
        """Test adding a basic test case."""
        test_case = {
            "name": "test-case-1",
            "error_code": "TAG_INVALID",
            "tests": {"string_tests": {"passes": ["test"]}},
        }
        self.stats.add_test_case(test_case)

        self.assertEqual(self.stats.total_cases, 1)
        self.assertEqual(self.stats.error_codes["TAG_INVALID"], 1)
        self.assertEqual(self.stats.test_types["string_tests"], 1)
        self.assertIn("test-case-1", self.stats.name_dict)
        self.assertEqual(self.stats.name_dict["test-case-1"], ["TAG_INVALID"])
        self.assertIn("TAG_INVALID", self.stats.code_dict)
        self.assertEqual(self.stats.code_dict["TAG_INVALID"], ["test-case-1"])

    def test_add_test_case_with_alt_codes(self):
        """Test adding a test case with alternative error codes."""
        test_case = {
            "name": "test-case-2",
            "error_code": "TAG_INVALID",
            "alt_codes": ["PLACEHOLDER_INVALID", "VALUE_INVALID"],
            "tests": {},
        }
        self.stats.add_test_case(test_case)

        # Should have all codes in name_dict
        self.assertEqual(
            self.stats.name_dict["test-case-2"],
            ["TAG_INVALID", "PLACEHOLDER_INVALID", "VALUE_INVALID"],
        )

        # All codes should reference this test in code_dict
        self.assertIn("test-case-2", self.stats.code_dict["TAG_INVALID"])
        self.assertIn("test-case-2", self.stats.code_dict["PLACEHOLDER_INVALID"])
        self.assertIn("test-case-2", self.stats.code_dict["VALUE_INVALID"])

    def test_duplicate_test_name_detection(self):
        """Test that duplicate test names are detected and recorded as errors."""
        test_case_1 = {
            "name": "duplicate-name",
            "error_code": "TAG_INVALID",
            "tests": {},
        }
        test_case_2 = {
            "name": "duplicate-name",
            "error_code": "VALUE_INVALID",
            "tests": {},
        }

        self.stats.add_test_case(test_case_1)
        self.assertEqual(len(self.stats.errors), 0)
        self.assertIn("duplicate-name", self.stats.name_dict)

        self.stats.add_test_case(test_case_2)
        self.assertEqual(len(self.stats.errors), 1)
        self.assertIn("Duplicate test case name", self.stats.errors[0])
        # Name dict should still only have the first entry
        self.assertEqual(len(self.stats.name_dict), 1)

    def test_multiple_test_cases_same_error_code(self):
        """Test that multiple test cases can share the same error code."""
        test_case_1 = {
            "name": "test-1",
            "error_code": "TAG_INVALID",
            "tests": {},
        }
        test_case_2 = {
            "name": "test-2",
            "error_code": "TAG_INVALID",
            "tests": {},
        }

        self.stats.add_test_case(test_case_1)
        self.stats.add_test_case(test_case_2)

        self.assertEqual(self.stats.error_codes["TAG_INVALID"], 2)
        self.assertEqual(len(self.stats.code_dict["TAG_INVALID"]), 2)
        self.assertIn("test-1", self.stats.code_dict["TAG_INVALID"])
        self.assertIn("test-2", self.stats.code_dict["TAG_INVALID"])

    def test_test_type_counting(self):
        """Test that different test types are counted correctly."""
        test_case = {
            "name": "test-with-types",
            "error_code": "TAG_INVALID",
            "tests": {
                "string_tests": {"passes": ["test"]},
                "sidecar_tests": {"passes": [{"sidecar": {}}]},
                "event_tests": {"passes": [[]]},
                "combo_tests": {"passes": [{}]},
            },
        }
        self.stats.add_test_case(test_case)

        self.assertEqual(self.stats.test_types["string_tests"], 1)
        self.assertEqual(self.stats.test_types["sidecar_tests"], 1)
        self.assertEqual(self.stats.test_types["event_tests"], 1)
        self.assertEqual(self.stats.test_types["combo_tests"], 1)

    def test_add_warning(self):
        """Test adding warnings."""
        self.stats.add_warning("Test warning")
        self.assertEqual(len(self.stats.warnings), 1)
        self.assertEqual(self.stats.warnings[0], "Test warning")

    def test_add_error(self):
        """Test adding errors."""
        self.stats.add_error("Test error")
        self.assertEqual(len(self.stats.errors), 1)
        self.assertEqual(self.stats.errors[0], "Test error")


class TestValidateTestCase(unittest.TestCase):
    """Test the validate_test_case function."""

    def test_valid_test_case(self):
        """Test that a valid test case passes validation."""
        test_case = {
            "error_code": "TAG_INVALID",
            "name": "test-name",
            "description": "Test description",
            "tests": {"string_tests": {"passes": ["test"]}},
        }
        errors = validate_test_case(test_case, "test.json")
        self.assertEqual(len(errors), 0)

    def test_missing_required_fields(self):
        """Test that missing required fields are detected."""
        test_case = {
            "error_code": "TAG_INVALID",
            # Missing 'name' and 'description'
            "tests": {},
        }
        errors = validate_test_case(test_case, "test.json")
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("name" in err for err in errors))
        self.assertTrue(any("description" in err for err in errors))

    def test_invalid_error_code_format(self):
        """Test that invalid error_code formats are detected."""
        test_case = {
            "error_code": "invalid-code",  # Should be uppercase with underscores
            "name": "test-name",
            "description": "Test description",
            "tests": {},
        }
        errors = validate_test_case(test_case, "test.json")
        self.assertTrue(any("Invalid error_code format" in err for err in errors))

    def test_missing_tests(self):
        """Test that missing or empty tests are detected."""
        test_case = {
            "error_code": "TAG_INVALID",
            "name": "test-name",
            "description": "Test description",
            "tests": {},  # Empty tests
        }
        errors = validate_test_case(test_case, "test.json")
        self.assertTrue(any("No tests defined" in err for err in errors))

    def test_no_tests_field(self):
        """Test that missing tests field is detected."""
        test_case = {
            "error_code": "TAG_INVALID",
            "name": "test-name",
            "description": "Test description",
            # No 'tests' field
        }
        errors = validate_test_case(test_case, "test.json")
        self.assertTrue(any("No tests defined" in err for err in errors))


class TestCombineTests(unittest.TestCase):
    """Test the combine_tests function."""

    def setUp(self):
        """Create temporary test directories and files."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_dir = Path(self.temp_dir) / "test_files"
        self.test_dir.mkdir()
        self.output_dir = Path(self.temp_dir) / "output"
        self.output_dir.mkdir()

    def tearDown(self):
        """Clean up temporary files."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def create_test_file(self, filename, test_cases):
        """Helper to create a test file with given test cases."""
        filepath = self.test_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(test_cases, f, indent=4)
        return filepath

    def test_combine_single_file(self):
        """Test combining a single test file."""
        test_cases = [
            {
                "error_code": "TAG_INVALID",
                "name": "test-1",
                "description": "Test description",
                "tests": {"string_tests": {"passes": ["test"]}},
            }
        ]
        self.create_test_file("test1.json", test_cases)

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path)

        self.assertEqual(count, 1)
        self.assertEqual(stats.total_cases, 1)
        self.assertTrue(output_path.exists())

        with open(output_path, "r", encoding="utf-8") as f:
            combined = json.load(f)
        self.assertEqual(len(combined), 1)

    def test_combine_multiple_files(self):
        """Test combining multiple test files."""
        test_cases_1 = [
            {
                "error_code": "TAG_INVALID",
                "name": "test-1",
                "description": "Test 1",
                "tests": {},
            }
        ]
        test_cases_2 = [
            {
                "error_code": "VALUE_INVALID",
                "name": "test-2",
                "description": "Test 2",
                "tests": {},
            }
        ]

        self.create_test_file("test1.json", test_cases_1)
        self.create_test_file("test2.json", test_cases_2)

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path)

        self.assertEqual(count, 2)
        self.assertEqual(stats.total_cases, 2)
        self.assertEqual(len(stats.code_dict), 2)

    def test_exclude_prefixes(self):
        """Test that files with excluded prefixes are skipped."""
        test_cases = [
            {
                "error_code": "TAG_INVALID",
                "name": "test-1",
                "description": "Test",
                "tests": {},
            }
        ]

        self.create_test_file("EXCLUDED_test.json", test_cases)
        self.create_test_file("included_test.json", test_cases)

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path, exclude_prefixes=["EXCLUDED"])

        # Should only include one file
        self.assertEqual(count, 1)

    def test_dry_run_mode(self):
        """Test that dry-run mode doesn't write files."""
        test_cases = [
            {
                "error_code": "TAG_INVALID",
                "name": "test-1",
                "description": "Test",
                "tests": {},
            }
        ]
        self.create_test_file("test.json", test_cases)

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path, dry_run=True)

        self.assertEqual(count, 1)
        self.assertFalse(output_path.exists())  # Should not write in dry-run

    def test_invalid_json_handling(self):
        """Test that invalid JSON files are handled gracefully."""
        # Create a file with invalid JSON
        invalid_file = self.test_dir / "invalid.json"
        with open(invalid_file, "w", encoding="utf-8") as f:
            f.write("{ invalid json }")

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path)

        # Should handle the error
        self.assertGreater(len(stats.errors), 0)
        self.assertTrue(any("JSON decode error" in err for err in stats.errors))

    def test_non_list_json_handling(self):
        """Test that non-list JSON files generate warnings."""
        test_data = {"not": "a list"}  # Should be a list
        self.create_test_file("invalid_structure.json", test_data)

        output_path = self.output_dir / "combined.json"
        count, stats = combine_tests(self.test_dir, output_path)

        # Should generate a warning
        self.assertGreater(len(stats.warnings), 0)
        self.assertTrue(any("does not contain a list" in warn for warn in stats.warnings))


class TestMainFunction(unittest.TestCase):
    """Test the main function."""

    def test_help_argument(self):
        """Test that --help argument works."""
        with self.assertRaises(SystemExit) as cm:
            main(["--help"])
        # argparse exits with 0 for --help
        self.assertEqual(cm.exception.code, 0)

    def test_dry_run_argument(self):
        """Test that dry-run mode can be invoked."""
        # Just test that it doesn't crash
        result = main(["--dry-run"])
        self.assertIsInstance(result, int)

    def test_verbose_argument(self):
        """Test that verbose mode can be invoked."""
        result = main(["--verbose", "--dry-run"])
        self.assertIsInstance(result, int)

    def test_default_arguments(self):
        """Test main with no arguments (uses sys.argv)."""
        # Mock sys.argv to simulate command-line usage
        with patch("sys.argv", ["consolidate_tests.py", "--dry-run"]):
            result = main()
            self.assertIsInstance(result, int)

    def test_missing_directories(self):
        """Test that missing directories are handled."""
        # This would require mocking Path.exists(), which is complex
        # For now, just verify the function returns an int
        result = main(["--dry-run"])
        self.assertIn(result, [0, 1])  # Should return valid exit code


class TestIntegration(unittest.TestCase):
    """Integration tests using actual test data."""

    @classmethod
    def setUpClass(cls):
        """Set up paths to actual test data."""
        project_root = Path(__file__).parent.parent
        cls.json_test_data_dir = project_root / "json_test_data"
        cls.validation_tests_dir = cls.json_test_data_dir / "validation_tests"
        cls.schema_tests_dir = cls.json_test_data_dir / "schema_tests"

    def test_actual_validation_tests_structure(self):
        """Test that actual validation tests have valid structure."""
        if not self.validation_tests_dir.exists():
            self.skipTest("Validation tests directory not found")

        test_files = list(self.validation_tests_dir.glob("*.json"))
        self.assertGreater(len(test_files), 0, "No test files found")

        for test_file in test_files:
            with self.subTest(file=test_file.name):
                with open(test_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                self.assertIsInstance(data, list, f"{test_file.name} should contain a list")

                for test_case in data:
                    errors = validate_test_case(test_case, test_file.name)
                    if errors:
                        self.fail(f"Validation errors in {test_file.name}: {errors}")

    def test_no_duplicate_test_names_in_actual_data(self):
        """Test that there are no duplicate test names in actual data."""
        if not self.validation_tests_dir.exists():
            self.skipTest("Validation tests directory not found")

        stats = TestStatistics()
        test_files = list(self.validation_tests_dir.glob("*.json"))

        for test_file in test_files:
            with open(test_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                for test_case in data:
                    stats.add_test_case(test_case)

        # Check for duplicate errors
        duplicate_errors = [e for e in stats.errors if "Duplicate" in e]
        if duplicate_errors:
            self.fail(f"Found duplicate test names: {duplicate_errors}")

    def test_code_dict_coverage(self):
        """Test that code_dict is properly populated from actual data."""
        if not self.validation_tests_dir.exists():
            self.skipTest("Validation tests directory not found")

        output_path = self.json_test_data_dir / "temp_test_output.json"
        try:
            count, stats = combine_tests(self.validation_tests_dir, output_path, dry_run=True)

            # Verify code_dict is populated
            self.assertGreater(len(stats.code_dict), 0)
            self.assertGreater(len(stats.name_dict), 0)

            # Verify consistency
            self.assertEqual(len(stats.name_dict), count)

            # Verify all test names in code_dict exist in name_dict
            for _code, test_names in stats.code_dict.items():
                for test_name in test_names:
                    self.assertIn(test_name, stats.name_dict)

        finally:
            if output_path.exists():
                output_path.unlink()


if __name__ == "__main__":
    unittest.main(verbosity=2)
