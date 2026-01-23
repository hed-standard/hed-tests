# Introduction to the HED test suite

## What is HED?

HED (Hierarchical Event Descriptors) is a framework for systematically describing events and experimental metadata in machine-actionable form. HED provides:

- **Controlled vocabulary** for annotating experimental data and events
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)

For more information, visit the HED project [homepage](https://www.hedtags.org) and the [resources page](https://www.hedtags.org/hed-resources).

## What is the HED test suite?

The **HED test suite** (`hed-tests` repository) is the official collection of JSON test cases for validating HED validator implementations. It provides:

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

## Getting started

### Clone the repository

Get the test suite from GitHub:

```bash
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

### Repository structure

```
hed-tests/
├── json_test_data/              # All test data
│   ├── validation_tests/        # 25 validation error test files
│   ├── schema_tests/            # 17 schema error test files
│   ├── javascriptTests.json     # Consolidated test file for JavaScript
│   ├── validationTests.json     # Consolidated validation tests
│   └── schemaTests.json         # Consolidated schema tests
├── src/
│   ├── scripts/                 # Utility scripts
│   └── schemas/                 # JSON schema for test validation
├── docs/                        # Documentation (this site)
└── tests/                       # Test utilities

```

Test files are organized by error code in the `json_test_data` directory. Tests that are relevant to validation of HED annotations are in the `validation_tests` subdirectory, while the tests that are relevant only to HED schema development are organized in the `schema_tests` subdirectory.

### Test structure

Tests for a specific error code are in a single file named by the most likely HED error code and must conform to a JSON schema available in `src/schemas/test_schema.json`.

```{admonition} **A validator might give a different error code**
---
class: tip
---
Because the exact error code that a validator assigns to an error depends heavily on the order in which it evaluates types of errors, a given test may produce a different error code. 
```

Each test has a `alt_codes` key that gives acceptable alternative error codes.

### Validating the tests

Ensure test files conform to the JSON schema:

# Validate a single test file

python src\\scripts\\validate_test_structure.py json_test_data\\validation_tests\\TAG_INVALID.json

# Validate all tests

python src\\scripts\\validate_test_structure.py json_test_data\\validation_tests python src\\scripts\\validate_test_structure.py json_test_data\\schema_tests

````

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
````

### Generate Test Index

Create a searchable test index:

```powershell
python src\scripts\generate_test_index.py

# Creates: docs/test_index.md
```

## Test file format

Each test file contains an array of test case objects in structured JSON format. Below is a complete example showing all available fields:

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": ["PLACEHOLDER_INVALID"],
        "name": "tag-invalid-in-schema",
        "description": "The tag is not valid in the schema it is associated with.",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": [
            "Misspelling tag names",
            "Using tags that don't exist in the specified schema version",
            "Creating extensions without proper parent tags"
        ],
        "explanation": "HED tags must exist in the specified schema or be valid extensions of existing tags.",
        "correction_strategy": "Use valid schema tags or create proper extensions",
        "correction_examples": [
            {
                "wrong": "ReallyInvalid/Extension",
                "correct": "Item/Object/Man-made-object/Device",
                "explanation": "Replaced non-existent tag with valid schema tag"
            }
        ],
        "definitions": [
            "(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"
        ],
        "tests": {
            "string_tests": {
                "fails": ["ReallyInvalid", "Label #"],
                "passes": ["Brown-color/Brown"]
            },
            "sidecar_tests": {
                "fails": [{
                    "event_code": {
                        "HED": {
                            "face": "ReallyInvalid"
                        }
                    }
                }],
                "passes": [{
                    "event_code": {
                        "HED": {
                            "face": "Brown-color/Brown"
                        }
                    }
                }]
            },
            "event_tests": {
                "fails": [[
                    ["onset", "duration", "HED"],
                    [4.5, 0, "Label #"]
                ]],
                "passes": [[
                    ["onset", "duration", "HED"],
                    [4.5, 0, "Brown-color/Brown"]
                ]]
            },
            "combo_tests": {
                "fails": [{
                    "sidecar": {
                        "event_code": {
                            "HED": {"face": "ReallyInvalid"}
                        }
                    },
                    "events": [
                        ["onset", "duration", "event_code", "HED"],
                        [4.5, 0, "face", "Red"]
                    ]
                }],
                "passes": [{
                    "sidecar": {
                        "event_code": {
                            "HED": {"face": "Acceleration/5 m-per-s^2"}
                        }
                    },
                    "events": [
                        ["onset", "duration", "event_code", "HED"],
                        [4.5, 0, "face", "Blue"]
                    ]
                }]
            }
        }
    }
]
```

### Field descriptions

**Core identification fields:**

- `error_code`: The primary error code being tested (required)
- `alt_codes`: Alternative error codes that may apply (optional)
- `name`: Unique identifier for this test case (required)
- `description`: Human-readable description of what is being tested (required)
- `warning`: Whether this is a warning (true) or error (false) (required)
- `schema`: HED schema version(s) used - string or array (required)

**AI-friendly metadata fields** (for machine learning and automated correction):

- `error_category`: Classification like "semantic", "syntax", "temporal_logic" (optional)
- `common_causes`: Array of common reasons for this error (optional)
- `explanation`: Detailed explanation of the error for AI systems (optional)
- `correction_strategy`: High-level approach to fixing the error (optional)
- `correction_examples`: Array of wrong/correct/explanation objects (optional)

**Context fields:**

- `definitions`: Array of HED definition strings required for test validation (optional)

**Test data** (the `tests` object contains four test types):

- `string_tests`: Raw HED strings to validate
  - `fails`: Array of strings that should produce the error
  - `passes`: Array of strings that should validate successfully
- `sidecar_tests`: BIDS JSON sidecar objects
  - `fails`: Array of sidecar objects that should produce the error
  - `passes`: Array of sidecar objects that should validate successfully
- `event_tests`: Tabular event data with HED columns (no sidecar)
  - `fails`: Array of event arrays (first row is headers, subsequent rows are data)
  - `passes`: Array of event arrays that should validate successfully
- `combo_tests`: Combined sidecar+events (realistic BIDS scenarios)
  - `fails`: Array of sidecar+events combinations that should fail validation
  - `passes`: Array of sidecar+events combination that should validate successfully

See [Test Format Specification](test_format.md) for complete documentation and additional optional fields.

### What this tests

Using the example above, here's what each test type validates:

**string_tests**: Direct HED string validation

- `fails: ["ReallyInvalid"]` - This raw HED string should trigger TAG_INVALID error
- `passes: ["Brown-color/Brown"]` - This raw HED string should validate successfully

**sidecar_tests**: BIDS JSON sidecar validation (metadata files)

- Tests that sidecar HED annotations properly flag invalid tags
- Validators should detect errors in the sidecar structure before events are processed

**event_tests**: Tabular event data validation (without sidecar context)

- First array in each test is the column headers
- Subsequent arrays are data rows with onset, duration, and HED values
- Tests standalone event file validation

**combo_tests**: Combined sidecar + events validation (realistic BIDS scenarios)

- Most realistic test case - mirrors actual BIDS dataset structure
- Sidecar provides HED annotations for categorical columns
- Events reference sidecar entries plus inline HED
- Validators must properly merge sidecar and event-level HED

**AI metadata usage**:

- `common_causes` helps AI systems understand why users make this error
- `explanation` provides context for automated correction suggestions
- `correction_examples` show concrete before/after examples for learning

## For validator developers

If you're building a HED validator:

1. **Clone this repository** or add as a submodule
2. **Parse test JSON files** from `json_test_data/`
3. **Execute tests** against your validation implementation
4. **Report discrepancies** as issues

See [Validator integration guide](validator_integration.md) for detailed integration instructions.

## For test contributors

Want to add new tests or improve existing ones?

1. **Follow the format**: Use the JSON schema in `src/schemas/test_schema.json`
2. **Include AI metadata**: Add explanations and correction examples
3. **Validate your changes**: Run `validate_test_structure.py`
4. **Submit a PR**: See [CONTRIBUTING.md](../CONTRIBUTING.md)

## Test statistics

Current test suite coverage:

- **42 test files**: 25 validation tests + 17 schema tests
- **136 test cases**: Comprehensive error code coverage
- **33 error codes**: All major validation errors
- **100% AI metadata**: Every test includes explanations and corrections

See [Test coverage report](test_coverage.md) for detailed statistics.

## Error code categories

Tests are organized into categories:

### Syntax errors

- `CHARACTER_INVALID` - Invalid characters in tags
- `COMMA_MISSING` - Missing required commas
- `PARENTHESES_MISMATCH` - Unmatched parentheses
- `TAG_EMPTY` - Empty tag elements

### Semantic errors

- `TAG_INVALID` - Tags not in schema
- `TAG_EXTENDED` - Invalid tag extensions
- `VALUE_INVALID` - Invalid tag values
- `UNITS_INVALID` - Invalid or missing units

### Definition errors

- `DEFINITION_INVALID` - Malformed definitions
- `DEF_INVALID` - Invalid definition usage
- `DEF_EXPAND_INVALID` - Definition expansion errors

### Sidecar errors

- `SIDECAR_INVALID` - Invalid sidecar structure
- `SIDECAR_BRACES_INVALID` - Curly brace errors
- `SIDECAR_KEY_MISSING` - Missing required keys

### Schema errors

- `SCHEMA_ATTRIBUTE_INVALID` - Invalid schema attributes
- `SCHEMA_DUPLICATE_NODE` - Duplicate schema nodes
- `SCHEMA_HEADER_INVALID` - Invalid schema headers

### Temporal Errors

- `TEMPORAL_TAG_ERROR` - Temporal tag issues
- `TEMPORAL_TAG_ERROR_DELAY` - Delay tag errors

See [Test Index](test_index.md) for complete error code listing.

## Getting help

### Documentation resources

- **[Test format specification](test_format.md)**: Complete JSON schema documentation
- **[Validator Integration Guide](validator_integration.md)**: How to use tests in your validator
- **[Test Coverage Report](test_coverage.md)**: Current coverage statistics
- **[Test Index](test_index.md)**: Searchable test case index
- **[Contributing Guide](../CONTRIBUTING.md)**: How to add or improve tests

### Support

- **Issues, questions, and bugs**: Open an [issue](https://github.com/hed-standard/hed-tests/issues) on GitHub
- **Contact**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)

### HED resources

- **[HED homepage](https://www.hedtags.org)**: Project overview
- **[HED specification](https://www.hedtags.org/hed-specification)**: Formal validation rules
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Vocabulary definitions
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation

## Next steps

- **Contribute**: Read [CONTRIBUTING.md](../CONTRIBUTING.md) to add new tests
- **View coverage**: Check [test_coverage.md](test_coverage.md) for statistics
