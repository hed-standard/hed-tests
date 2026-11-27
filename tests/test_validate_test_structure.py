"""
Unit tests for the default-schema check in validate_test_structure.py.
"""

import unittest

from src.scripts.validate_test_structure import DEFAULT_STANDARD_SCHEMA, check_default_schema


def case(name, schema):
    """Return a minimal validation case with the given name and schema."""
    return {"name": name, "schema": schema}


class TestCheckDefaultSchema(unittest.TestCase):
    """check_default_schema reports cases on an earlier standard schema that do not say why."""

    def test_default_schema_passes(self):
        self.assertEqual(check_default_schema([case("tag-invalid-in-schema", DEFAULT_STANDARD_SCHEMA)]), [])

    def test_earlier_schema_without_reason_fails(self):
        errors = check_default_schema([case("tag-invalid-in-schema", "8.4.0")])
        self.assertEqual(len(errors), 1)
        self.assertIn("tag-invalid-in-schema", errors[0])
        self.assertIn("8.4.0", errors[0])

    def test_earlier_schema_named_for_version_passes(self):
        cases = [
            case("tag-extension-invalid-not-allowed-8-0-0", "8.0.0"),
            case("temporal-tag-error-rules-apply-in-8-1-0", "8.1.0"),
            case("character-invalid-text-value-before-8-5-0", "8.2.0"),
            case("invalid-character-name-value-class-early-schema", "8.2.0"),
        ]
        self.assertEqual(check_default_schema(cases), [])

    def test_version_in_middle_of_name_does_not_count(self):
        self.assertEqual(len(check_default_schema([case("value-8-3-0-style-check", "8.3.0")])), 1)

    def test_list_schemas_are_not_checked(self):
        self.assertEqual(check_default_schema([case("merge-group-mismatch", ["8.4.0", "testconflict_2.0.0"])]), [])

    def test_malformed_name_is_skipped(self):
        cases = [case(None, "8.4.0"), case(3, "8.4.0"), case(["tag-invalid"], "8.4.0")]
        self.assertEqual(check_default_schema(cases), [])

    def test_library_string_is_not_checked(self):
        self.assertEqual(check_default_schema([case("library-only", "testconflict_2.0.0")]), [])


if __name__ == "__main__":
    unittest.main()
