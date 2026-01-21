# Test Format Specification

## Overview

Each JSON test file in the HED Test Suite follows a standardized structure to ensure consistent validation testing across all HED validator implementations.

## File Structure

Test files are located in:
- `json_test_data/validation_tests/` - Tests for validation error codes
- `json_test_data/schema_tests/` - Tests for schema validation errors

Each file contains an array of test case objects.

## Test Case Schema

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": ["PLACEHOLDER_INVALID"],
        "name": "tag-invalid-in-schema",
        "description": "Human-readable description of what is being tested",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": ["List of common causes"],
        "explanation": "Detailed explanation for AI/developers",
        "correction_strategy": "How to fix the issue",
        "correction_examples": [
            {
                "wrong": "Invalid HED string",
                "correct": "Corrected HED string",
                "explanation": "Why the correction works"
            }
        ],
        "definitions": [
            "(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"
        ],
        "tests": {
            "string_tests": {...},
            "sidecar_tests": {...},
            "event_tests": {...},
            "combo_tests": {...}
        }
    }
]
```

## Required Fields

### error_code
**Type**: `string`

The HED error code being tested. Must match the filename (e.g., `TAG_INVALID.json`).

**Example**: `"TAG_INVALID"`

### name
**Type**: `string`

A unique, descriptive identifier for the test case. Use lowercase with hyphens.

**Example**: `"tag-invalid-in-schema"`

### description
**Type**: `string`

Human-readable description of what the test case validates.

**Example**: `"Test that tags not in schema are detected as invalid"`

### schema
**Type**: `string`

HED schema version for this test case.

**Example**: `"8.4.0"`

### tests
**Type**: `object`

Container for all test data. Must include at least one test type.

## Optional Fields

### alt_codes
**Type**: `array[string]`

Alternative error codes that might be reported for this condition. Useful when multiple validators use different codes for the same error.

**Example**: `["PLACEHOLDER_INVALID"]`

### warning
**Type**: `boolean` (default: `false`)

Whether this test should produce a warning instead of an error.

### error_category
**Type**: `string`

Semantic category of the error. One of:
- `"syntax"` - Basic syntax errors (parentheses, commas, etc.)
- `"semantic"` - Tag meaning errors (invalid tags, wrong values)
- `"value"` - Value-specific errors (units, placeholders)
- `"consistency"` - Internal consistency errors (definition usage)
- `"uniqueness"` - Duplicate detection errors
- `"schema"` - Schema structure errors

### common_causes
**Type**: `array[string]`

List of common reasons this error occurs. Used by AI systems to understand typical mistakes.

**Example**:
```json
[
    "Typo in tag name",
    "Using deprecated tag",
    "Tag from wrong schema version"
]
```

### explanation
**Type**: `string`

Detailed explanation of the error for AI systems and developers.

**Example**: `"Tags must exist in the active HED schema. Extensions are allowed but the base tag must be valid."`

### correction_strategy
**Type**: `string`

General approach to fixing this error.

**Example**: `"Check the tag against the schema browser at hedtags.org. Use the correct tag path or a valid extension."`

### correction_examples
**Type**: `array[object]`

Concrete examples showing wrong → correct transformations.

**Structure**:
```json
[
    {
        "wrong": "Invalidtag",
        "correct": "Event",
        "explanation": "Use a tag that exists in the schema"
    }
]
```

### definitions
**Type**: `array[string]`

HED definition strings required for the test case. These are evaluated before the test strings.

**Example**:
```json
[
    "(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"
]
```

## Test Types

### string_tests

Tests for raw HED strings.

**Structure**:
```json
{
    "fails": [
        "Red, Invalidtag",
        "Blue, Typo/Tag"
    ],
    "passes": [
        "Red, Blue",
        "Event, Sensory-event"
    ]
}
```

- `fails`: Array of HED strings that should produce the error
- `passes`: Array of HED strings that should NOT produce the error

### sidecar_tests

Tests for BIDS JSON sidecar files.

**Structure**:
```json
{
    "fails": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "stimulus": "Invalidtag"
                    }
                }
            }
        }
    ],
    "passes": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "stimulus": "Sensory-event"
                    }
                }
            }
        }
    ]
}
```

Each item is an object with a `sidecar` property containing a BIDS sidecar JSON structure.

### event_tests

Tests for tabular event data with HED annotations.

**Structure**:
```json
{
    "fails": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Red, Invalidtag"]
        ]
    ],
    "passes": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Red, Blue"]
        ]
    ]
}
```

Each test is a 2D array:
- First row: Column headers (must include at least one HED column)
- Subsequent rows: Event data

### combo_tests

Combined sidecar + event tests (realistic BIDS scenarios).

**Structure**:
```json
{
    "fails": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "show": "Sensory-event"
                    }
                }
            },
            "events": [
                ["onset", "duration", "event_type", "HED"],
                [4.5, 0, "show", "Invalidtag"]
            ]
        }
    ],
    "passes": [...]
}
```

Combines a sidecar definition with event data that uses categorical values from the sidecar.

## Validation Rules

### Required Structure

1. **At least one test**: Every test case must have at least one test type with data
2. **Both fails and passes**: Each test type should include both failing and passing examples
3. **Valid JSON**: All test data must be valid JSON
4. **Consistent error_code**: Must match the filename

### Naming Conventions

- **File names**: `ERROR_CODE.json` (uppercase, underscores)
- **Test names**: `error-code-specific-scenario` (lowercase, hyphens)
- **Error codes**: Match official HED specification

### AI Metadata

For AI training and code generation, include:
- `explanation`: Why this error occurs
- `common_causes`: Typical mistakes
- `correction_strategy`: How to fix
- `correction_examples`: Concrete before/after examples

## Example Test File

Here's a complete example from `TAG_INVALID.json`:

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": [],
        "name": "tag-invalid-basic",
        "description": "Basic test for tags not in the schema",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": [
            "Typo in tag name",
            "Using a tag from a different schema version",
            "Attempting to use custom tags without proper extension syntax"
        ],
        "explanation": "Tags must exist in the active HED schema. Each tag path must be found in the schema vocabulary, though extensions to valid tags are allowed using the extension syntax.",
        "correction_strategy": "Verify the tag exists in the schema using the schema browser at hedtags.org. Check for typos, ensure you're using the correct schema version, or use proper extension syntax for custom additions.",
        "correction_examples": [
            {
                "wrong": "Invalidtag",
                "correct": "Event",
                "explanation": "Use a tag that exists in the schema"
            },
            {
                "wrong": "Red, Sensory/Invalidtag",
                "correct": "Red, Sensory-event",
                "explanation": "The full tag path must be valid"
            }
        ],
        "definitions": [],
        "tests": {
            "string_tests": {
                "fails": [
                    "Invalidtag",
                    "Red, Invalidtag",
                    "Sensory/Invalidtag"
                ],
                "passes": [
                    "Red",
                    "Event",
                    "Sensory-event"
                ]
            }
        }
    }
]
```

## Schema Validation

All test files are validated against `src/schemas/test_schema.json` using the validation script:

```powershell
.venv\Scripts\activate.ps1
python src\scripts\validate_test_structure.py json_test_data\validation_tests\TAG_INVALID.json
```

## Best Practices

1. **One error per file**: Keep test files focused on a single error code
2. **Comprehensive coverage**: Include edge cases and common scenarios
3. **Clear descriptions**: Make test names and descriptions self-explanatory
4. **AI-friendly**: Always include explanation and correction examples
5. **Real-world examples**: Use realistic HED strings that developers might encounter
6. **Both positive and negative**: Always test both failing and passing cases
7. **Schema versioning**: Specify the schema version for reproducibility

## Adding New Tests

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines on adding new test cases to the suite.
