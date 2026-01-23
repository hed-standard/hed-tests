# HED Test Suite

[![CI](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml/badge.svg)](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml) [![Documentation Status](https://readthedocs.org/projects/hed-tests/badge/?version=latest)](https://hed-tests.readthedocs.io/en/latest/?badge=latest) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Official JSON test suite for HED (Hierarchical Event Descriptors) validation**

This repository provides comprehensive, machine-readable test cases for validating HED validator implementations. Tests are designed to ensure consistent validation behavior across all platforms (Python, JavaScript, and future implementations) and serve as AI-readable specifications for HED validation rules.

## Purpose

The HED test suite serves multiple critical functions:

- **Validator Testing**: Ensures all HED validator implementations produce consistent results
- **Specification Documentation**: Machine-readable examples of HED validation rules
- **AI Training**: Structured test cases with explanations for AI systems to learn HED validation
- **Cross-Platform Consistency**: Single source of truth for validation behavior
- **Regression Prevention**: Catch validation changes across versions

## Repository Structure

```
hed-tests/
├── json_test_data/              # Test data (primary content)
│   ├── validation_tests/        # Individual error code tests
│   │   ├── TAG_INVALID.json
│   │   ├── UNITS_INVALID.json
│   │   └── ...                  # One file per error code
│   ├── schema_tests/           # Schema validation tests
│   │   └── SCHEMA_*.json
│   ├── validation_tests.json    # Consolidated validation tests
│   ├── schema_tests.json        # Consolidated schema tests
│   ├── validation_code_dict.json    # Error code → test name mappings (validation)
│   ├── validation_testname_dict.json # Test name → error codes (validation)
│   ├── schema_code_dict.json        # Error code → test name mappings (schema)
│   └── schema_testname_dict.json    # Test name → error codes (schema)
├── src/scripts/                # Utility scripts
│   └── consolidate_tests.py
├── tests/                      # Test analysis utilities
└── docs/                       # Documentation
```

## Test File Format

Each test file contains structured JSON with the following format:

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": ["PLACEHOLDER_INVALID"],
        "name": "tag-invalid-in-schema",
        "description": "Human-readable description",
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
                "explanation": "Why this works"
            }
        ],
        "definitions": ["(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"],
        "tests": {
            "string_tests": {
                "fails": ["Strings that should fail"],
                "passes": ["Strings that should pass"]
            },
            "sidecar_tests": {...},
            "event_tests": {...},
            "combo_tests": {...}
        }
    }
]
```

### Test Types

1. **string_tests**: Raw HED strings
1. **sidecar_tests**: JSON sidecar files (BIDS metadata)
1. **event_tests**: Tabular event data with HED columns
1. **combo_tests**: Combined sidecar + event data (realistic scenarios)

## Usage for Validator Developers

### Python Validator Example

```python
import json
from pathlib import Path

# Load test file
test_file = Path("json_test_data/validation_tests/TAG_INVALID.json")
tests = json.loads(test_file.read_text())

# Run tests
for test_case in tests:
    for fail_string in test_case["tests"]["string_tests"]["fails"]:
        # Your validator should report an error
        errors = your_validator.validate(fail_string, schema=test_case["schema"])
        assert len(errors) > 0, f"Should fail: {fail_string}"
        assert any(e["code"] in [test_case["error_code"]] + test_case.get("alt_codes", []) 
                   for e in errors)
    
    for pass_string in test_case["tests"]["string_tests"]["passes"]:
        # Your validator should NOT report an error
        errors = your_validator.validate(pass_string, schema=test_case["schema"])
        assert len(errors) == 0, f"Should pass: {pass_string}"
```

### JavaScript Validator Example

Use the consolidated `validation_tests.json` and `schema_tests.json` files:

```javascript
const validationTests = require('./json_test_data/validation_tests.json');
const schemaTests = require('./json_test_data/schema_tests.json');

validationTests.forEach(testCase => {
    testCase.tests.string_tests.fails.forEach(hedString => {
        const errors = validator.validate(hedString, testCase.schema);
        expect(errors.length).toBeGreaterThan(0);
        expect(errors.some(e => e.code === testCase.error_code)).toBe(true);
    });
    
    testCase.tests.string_tests.passes.forEach(hedString => {
        const errors = validator.validate(hedString, testCase.schema);
        expect(errors.length).toBe(0);
    });
});
```

## Error Code Categories

Tests are organized by error code:

### Syntax Errors

- `CHARACTER_INVALID`: Invalid UTF-8 characters
- `COMMA_MISSING`: Missing required commas
- `PARENTHESES_MISMATCH`: Unmatched parentheses
- `TAG_EMPTY`: Empty tags

### Semantic Errors

- `TAG_INVALID`: Tag not in schema
- `TAG_EXTENDED`: Extension validation
- `TAG_EXTENSION_INVALID`: Invalid extensions
- `VALUE_INVALID`: Invalid tag values
- `UNITS_INVALID`: Invalid units

### Definition Errors

- `DEFINITION_INVALID`: Invalid definitions
- `DEF_INVALID`: Invalid Def usage
- `DEF_EXPAND_INVALID`: Invalid Def-expand

### Sidecar Errors

- `SIDECAR_INVALID`: Sidecar structure issues
- `SIDECAR_BRACES_INVALID`: Invalid brace syntax
- `SIDECAR_KEY_MISSING`: Missing required keys

### Schema Errors

- `SCHEMA_ATTRIBUTE_INVALID`: Invalid schema attributes
- `SCHEMA_DUPLICATE_NODE`: Duplicate schema nodes
- `SCHEMA_HEADER_INVALID`: Invalid schema headers

### Temporal Errors

- `TEMPORAL_TAG_ERROR`: Temporal tag issues
- `TEMPORAL_TAG_ERROR_DELAY`: Temporal delay issues

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding new test cases
- Test file format requirements
- JSON validation
- Pull request process

## Development Setup

```powershell
# Clone repository
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests

# Create virtual environment (Windows PowerShell)
python -m venv .venv
.venv/Scripts/activate.ps1

# Install dependencies
pip install -r requirements-dev.txt
```

### Running Scripts

```powershell
# Activate environment first
.venv/Scripts/activate.ps1

# Consolidate tests and generate dictionaries
python src/scripts/consolidate_tests.py

# Analyze test coverage
python -m unittest tests.test_summarize_testdata -v
```

## Related Repositories

- **[hed-python](https://github.com/hed-standard/hed-python)**: Python validator implementation
- **[hed-javascript](https://github.com/hed-standard/hed-javascript)**: JavaScript validator implementation
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal HED specification
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: HED vocabulary schemas

## Test Statistics

**Current coverage** (as of January 2026):

- **Validation tests**: 25 error codes
- **Schema tests**: 11 error codes
- **Total test cases**: 500+ individual tests
- **Test types**: String, sidecar, event, and combo tests

## Versioning

This repository follows semantic versioning:

- **Major**: Breaking changes to test format
- **Minor**: New test cases or error codes
- **Patch**: Bug fixes in existing tests

Current version: **1.0.0**

## License

MIT License - see [LICENSE](LICENSE) for details

## Citation

If you use HED in your research, please cite:

```
Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2022).
Building FAIR functionality: Annotating events in time series data using 
Hierarchical Event Descriptors (HED). Neuroinformatics, 1-17.
```

## Support

- **Documentation**: https://www.hedtags.org
- **Issues**: https://github.com/hed-standard/hed-tests/issues
- **Discussions**: https://github.com/hed-standard/hed-specification/discussions
- **Email**: hed.maintainers@gmail.com
