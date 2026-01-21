# Introduction to the HED test suite

## What is HED?

HED (Hierarchical Event Descriptors) is a framework for systematically describing events and experimental metadata in machine-actionable form. HED provides:

- **Controlled vocabulary** for annotating experimental data and events
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)

For more information, visit the HED project [homepage](https://www.hedtags.org) and the [resources page](https://www.hedtags.org/hed-resources).

## What is the HED test suite?

The **HED Test Suite** (`hed-tests` repository) is the official collection of JSON test cases for validating HED validator implementations. It provides:

- **Comprehensive test coverage**: 136 test cases covering 33 error codes
- **Multiple test types**: String, sidecar, event, and combo tests
- **AI-friendly metadata**: Explanations, common causes, and correction strategies
- **Cross-platform consistency**: Single source of truth for all validators
- **Machine-readable specification**: Tests document expected validation behavior

### Purpose

The test suite serves three primary purposes:

1. **Validator validation**: Ensure Python, JavaScript, and future implementations produce consistent results
2. **Specification documentation**: Provide executable examples of HED validation rules
3. **AI training**: Enable AI systems to understand HED validation through structured examples

### Related tools and resources

- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation (primary consumer)
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation (primary consumer)
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Standardized vocabularies referenced in tests
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification (source of truth for rules)
- **[HED online tools](https://hedtools.org/hed)**: Web-based validation tools
- **[HED examples](https://github.com/hed-standard/hed-examples)**: Example annotated datasets

## Getting Started

### Clone the Repository

Get the test suite from GitHub:

```bash
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

### Repository Structure

```
hed-tests/
├── json_test_data/              # All test data
│   ├── validation_tests/        # 25 validation error test files
│   ├── schema_tests/            # 17 schema error test files
│   └── javascriptTests.json     # Consolidated test file
├── src/
│   ├── scripts/                 # Utility scripts
│   └── schemas/                 # JSON schema for test validation
├── docs/                        # Documentation (this site)
└── tests/                       # Test utilities

```

### Browse the Tests

Test files are organized by error code:

```bash
# Validation error tests
ls json_test_data/validation_tests/
# TAG_INVALID.json, UNITS_INVALID.json, etc.

# Schema validation tests
ls json_test_data/schema_tests/
# SCHEMA_ATTRIBUTE_INVALID.json, etc.
```

### Validate Test Structure

Ensure test files conform to the JSON schema:

```powershell
# Set up environment (Windows PowerShell)
python -m venv .venv
.venv\Scripts\activate.ps1
pip install -r requirements.txt

# Validate a single test file
python src\scripts\validate_test_structure.py json_test_data\validation_tests\TAG_INVALID.json

# Validate all tests
python src\scripts\validate_test_structure.py json_test_data\validation_tests
python src\scripts\validate_test_structure.py json_test_data\schema_tests
```

### Check Test Coverage

Analyze test coverage statistics:

```powershell
python src\scripts\check_coverage.py

# Output:
# HED Test Suite Coverage Report
# =====================================
# Total test files: 42
# Total test cases: 136
# Error codes covered: 33
# ...
```

### Generate Test Index

Create a searchable test index:

```powershell
python src\scripts\generate_test_index.py

# Creates: docs/test_index.md
```

## Test File Format

Each test file contains structured JSON test cases:

```json
[
    {
        "error_code": "TAG_INVALID",
        "name": "tag-invalid-basic",
        "description": "Basic test for tags not in the schema",
        "schema": "8.4.0",
        "tests": {
            "string_tests": {
                "fails": ["Invalidtag", "Red, Invalidtag"],
                "passes": ["Red", "Event"]
            }
        }
    }
]
```

See [Test Format Specification](test_format.md) for complete documentation.

## For Validator Developers

If you're building a HED validator:

1. **Clone this repository** or add as a submodule
2. **Parse test JSON files** from `json_test_data/`
3. **Execute tests** against your validation implementation
4. **Report discrepancies** as issues

See [Validator Integration Guide](validator_integration.md) for detailed integration instructions.

## For Test Contributors

Want to add new tests or improve existing ones?

1. **Follow the format**: Use the JSON schema in `src/schemas/test_schema.json`
2. **Include AI metadata**: Add explanations and correction examples
3. **Validate your changes**: Run `validate_test_structure.py`
4. **Submit a PR**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

## Test Statistics

Current test suite coverage:

- **42 test files**: 25 validation tests + 17 schema tests
- **136 test cases**: Comprehensive error code coverage
- **33 error codes**: All major validation errors
- **100% AI metadata**: Every test includes explanations and corrections

See [Test Coverage Report](test_coverage.md) for detailed statistics.

## Error Code Categories

Tests are organized into categories:

### Syntax Errors
- `CHARACTER_INVALID` - Invalid characters in tags
- `COMMA_MISSING` - Missing required commas
- `PARENTHESES_MISMATCH` - Unmatched parentheses
- `TAG_EMPTY` - Empty tag elements

### Semantic Errors
- `TAG_INVALID` - Tags not in schema
- `TAG_EXTENDED` - Invalid tag extensions
- `VALUE_INVALID` - Invalid tag values
- `UNITS_INVALID` - Invalid or missing units

### Definition Errors
- `DEFINITION_INVALID` - Malformed definitions
- `DEF_INVALID` - Invalid definition usage
- `DEF_EXPAND_INVALID` - Definition expansion errors

### Sidecar Errors
- `SIDECAR_INVALID` - Invalid sidecar structure
- `SIDECAR_BRACES_INVALID` - Curly brace errors
- `SIDECAR_KEY_MISSING` - Missing required keys

### Schema Errors
- `SCHEMA_ATTRIBUTE_INVALID` - Invalid schema attributes
- `SCHEMA_DUPLICATE_NODE` - Duplicate schema nodes
- `SCHEMA_HEADER_INVALID` - Invalid schema headers

### Temporal Errors
- `TEMPORAL_TAG_ERROR` - Temporal tag issues
- `TEMPORAL_TAG_ERROR_DELAY` - Delay tag errors

See [Test Index](test_index.md) for complete error code listing.

## Getting Help

### Documentation Resources

- **[Test Format Specification](test_format.md)**: Complete JSON schema documentation
- **[Validator Integration Guide](validator_integration.md)**: How to use tests in your validator
- **[Test Coverage Report](test_coverage.md)**: Current coverage statistics
- **[Test Index](test_index.md)**: Searchable test case index
- **[Contributing Guide](../CONTRIBUTING.md)**: How to add or improve tests

### Support

- **Issues and bugs**: Open an [issue](https://github.com/hed-standard/hed-tests/issues) on GitHub
- **Questions**: Use [GitHub Discussions](https://github.com/hed-standard/hed-tests/discussions)
- **Contact**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)

### HED Resources

- **[HED homepage](https://www.hedtags.org)**: Project overview
- **[HED specification](https://www.hedtags.org/hed-specification)**: Formal validation rules
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Vocabulary definitions
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation

## Quick Example

Here's a test case from `TAG_INVALID.json`:

```json
{
    "error_code": "TAG_INVALID",
    "name": "tag-invalid-basic",
    "description": "Basic test for tags not in the schema",
    "schema": "8.4.0",
    "explanation": "Tags must exist in the active HED schema. Each tag path must be found in the schema vocabulary.",
    "common_causes": [
        "Typo in tag name",
        "Using a tag from a different schema version"
    ],
    "correction_strategy": "Verify the tag exists using the schema browser at hedtags.org",
    "correction_examples": [
        {
            "wrong": "Invalidtag",
            "correct": "Event",
            "explanation": "Use a tag that exists in the schema"
        }
    ],
    "tests": {
        "string_tests": {
            "fails": ["Invalidtag", "Red, Invalidtag"],
            "passes": ["Red", "Event"]
        }
    }
}
```

**What this tests**:
- **Failing cases**: `Invalidtag` and `Red, Invalidtag` should produce `TAG_INVALID` error
- **Passing cases**: `Red` and `Event` should NOT produce this error
- **AI context**: Explanations help AI understand why tags must be in schema
- **Corrections**: Examples show how to fix the error

## Next Steps

- **Browse tests**: Explore [test_index.md](test_index.md) to see all test cases
- **Integrate tests**: Follow [validator_integration.md](validator_integration.md) to use in your validator
- **Contribute**: Read [CONTRIBUTING.md](../CONTRIBUTING.md) to add new tests
- **View coverage**: Check [test_coverage.md](test_coverage.md) for statistics

