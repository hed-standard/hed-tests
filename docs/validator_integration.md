# Validator integration guide

This guide explains how to integrate the HED Test Suite into your HED validator implementation.

## Overview

The HED Test Suite provides standardized JSON test cases that all HED validators should pass. By integrating these tests, you ensure your validator:

- **Matches the specification**: Validates HED according to the official rules
- **Maintains consistency**: Produces the same results as other validators
- **Prevents regressions**: Catches changes in validation behavior
- **Documents behavior**: Tests serve as executable specifications

## Getting the tests

### Method 1: Git clone (Recommended)

Clone the repository to access all tests:

```bash
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

Update periodically to get new tests:

```bash
git pull origin main
```

### Method 2: Download ZIP

Download the latest tests as a ZIP file:

```
https://github.com/hed-standard/hed-tests/archive/refs/heads/main.zip
```

### Method 3: Submodule

Add as a git submodule to your validator repository:

```bash
git submodule add https://github.com/hed-standard/hed-tests.git tests/hed-tests
git submodule update --init --recursive
```

## Test file structure

Tests are organized in two directories:

```
json_test_data/
├── validation_tests/      # Validation error tests
│   ├── TAG_INVALID.json
│   ├── UNITS_INVALID.json
│   └── ...
└── schema_tests/          # Schema validation tests
    ├── SCHEMA_ATTRIBUTE_INVALID.json
    └── ...
```

### Consolidated files

For convenience, consolidated test files and lookup dictionaries are provided:

**Test files:**

- `json_test_data/validation_tests.json` - All validation tests in one file
- `json_test_data/schema_tests.json` - All schema tests in one file

**Lookup dictionaries:**

- `json_test_data/validation_code_dict.json` - Maps error codes to test names
- `json_test_data/validation_testname_dict.json` - Maps test names to error codes
- `json_test_data/schema_code_dict.json` - Maps error codes to test names (schema tests)
- `json_test_data/schema_testname_dict.json` - Maps test names to error codes (schema tests)

Generate these files using:

```bash
python src/scripts/consolidate_tests.py
```

## JSON format

Each test file contains an array of test case objects:

```json
[
    {
        "error_code": "TAG_INVALID",
        "name": "tag-invalid-basic",
        "description": "Basic test for tags not in the schema",
        "schema": "8.4.0",
        "tests": {
            "string_tests": {
                "fails": ["Invalidtag"],
                "passes": ["Event"]
            }
        }
    }
]
```

See [Test Format Specification](test_format.md) for complete schema documentation.

## Integration approaches

### Approach 1: Direct test execution

Read test files and execute them directly in your test framework.

**Python example (unittest)**:

```python
import json
import unittest
from pathlib import Path

class TestHedValidation(unittest.TestCase):
    """Test HED validation using the test suite."""
    
    @classmethod
    def setUpClass(cls):
        """Load all test cases once before running tests."""
        cls.test_cases = []
        test_dir = Path("hed-tests/json_test_data/validation_tests")
        
        for test_file in test_dir.glob("*.json"):
            with open(test_file) as f:
                cases = json.load(f)
                for case in cases:
                    cls.test_cases.append((test_file.stem, case))
    
    def test_validation_suite(self):
        """Run each test case from the suite."""
        for error_code, test_case in self.test_cases:
            with self.subTest(error_code=error_code, test_name=test_case["name"]):
                schema = load_schema(test_case["schema"])
                
                # Test failing strings
                if "string_tests" in test_case.get("tests", {}):
                    for hed_string in test_case["tests"]["string_tests"].get("fails", []):
                        issues = validate_hed_string(hed_string, schema)
                        self.assertTrue(
                            any(issue.code == error_code for issue in issues),
                            f"Expected {error_code} for: {hed_string}"
                        )
                    
                    # Test passing strings
                    for hed_string in test_case["tests"]["string_tests"].get("passes", []):
                        issues = validate_hed_string(hed_string, schema)
                        self.assertFalse(
                            any(issue.code == error_code for issue in issues),
                            f"Unexpected {error_code} for: {hed_string}"
                        )

if __name__ == '__main__':
    unittest.main()
```

**JavaScript Example (Jest)**:

```javascript
const fs = require('fs');
const path = require('path');
const { validateHedString } = require('./validator');

describe('HED Validation Tests', () => {
    const testDir = 'hed-tests/json_test_data/validation_tests';
    const files = fs.readdirSync(testDir);
    
    files.forEach(filename => {
        const errorCode = path.basename(filename, '.json');
        const testCases = JSON.parse(
            fs.readFileSync(path.join(testDir, filename), 'utf8')
        );
        
        describe(errorCode, () => {
            testCases.forEach(testCase => {
                test(testCase.name, () => {
                    const schema = loadSchema(testCase.schema);
                    
                    // Test failing strings
                    const fails = testCase.tests?.string_tests?.fails || [];
                    fails.forEach(hedString => {
                        const issues = validateHedString(hedString, schema);
                        expect(issues.some(i => i.code === errorCode)).toBe(true);
                    });
                    
                    // Test passing strings
                    const passes = testCase.tests?.string_tests?.passes || [];
                    passes.forEach(hedString => {
                        const issues = validateHedString(hedString, schema);
                        expect(issues.some(i => i.code === errorCode)).toBe(false);
                    });
                });
            });
        });
    });
});
```

### Approach 2: Generate Test Cases

Generate test files in your native test format from the JSON.

**Example**: Convert JSON to Python unittest files:

```python
import json
from pathlib import Path

def generate_test_file(json_path, output_path):
    """Generate a Python test file from JSON test cases."""
    with open(json_path) as f:
        test_cases = json.load(f)
    
    error_code = json_path.stem
    
    test_code = f'''
import unittest
from hed_validator import validate_hed_string, load_schema

class Test{error_code}(unittest.TestCase):
'''
    
    for i, case in enumerate(test_cases):
        test_code += f'''
    def test_{case["name"].replace("-", "_")}(self):
        """Test: {case["description"]}"""
        schema = load_schema("{case["schema"]}")
        
'''
        if "string_tests" in case.get("tests", {}):
            for hed_string in case["tests"]["string_tests"].get("fails", []):
                test_code += f'''
        issues = validate_hed_string("{hed_string}", schema)
        self.assertTrue(any(i.code == "{error_code}" for i in issues))
'''
            for hed_string in case["tests"]["string_tests"].get("passes", []):
                test_code += f'''
        issues = validate_hed_string("{hed_string}", schema)
        self.assertFalse(any(i.code == "{error_code}" for i in issues))
'''
    
    with open(output_path, 'w') as f:
        f.write(test_code)
```

### Approach 3: Test Report Comparison

Run tests and compare your results against a reference implementation.

```python
def compare_validation_results(test_case, reference_issues, your_issues):
    """Compare validation results against reference implementation."""
    error_code = test_case["error_code"]
    
    # Check if both found (or didn't find) the error
    ref_found = any(i.code == error_code for i in reference_issues)
    your_found = any(i.code == error_code for i in your_issues)
    
    if ref_found != your_found:
        return {
            "test": test_case["name"],
            "expected": ref_found,
            "actual": your_found,
            "status": "MISMATCH"
        }
    
    return {"status": "MATCH"}
```

## Test Types

### String Tests

Simplest test type - raw HED strings.

```python
def run_string_tests(test_case, schema):
    """Execute string_tests from a test case."""
    error_code = test_case["error_code"]
    string_tests = test_case["tests"].get("string_tests", {})
    
    # Test strings that should fail
    for hed_string in string_tests.get("fails", []):
        issues = validate_hed_string(hed_string, schema)
        assert any(i.code == error_code for i in issues), \
            f"Expected {error_code} for: {hed_string}"
    
    # Test strings that should pass
    for hed_string in string_tests.get("passes", []):
        issues = validate_hed_string(hed_string, schema)
        assert not any(i.code == error_code for i in issues), \
            f"Unexpected {error_code} for: {hed_string}"
```

### Sidecar Tests

Test BIDS JSON sidecar validation.

```python
def run_sidecar_tests(test_case, schema):
    """Execute sidecar_tests from a test case."""
    error_code = test_case["error_code"]
    sidecar_tests = test_case["tests"].get("sidecar_tests", {})
    
    for sidecar_obj in sidecar_tests.get("fails", []):
        sidecar = sidecar_obj["sidecar"]
        issues = validate_sidecar(sidecar, schema)
        assert any(i.code == error_code for i in issues)
    
    for sidecar_obj in sidecar_tests.get("passes", []):
        sidecar = sidecar_obj["sidecar"]
        issues = validate_sidecar(sidecar, schema)
        assert not any(i.code == error_code for i in issues)
```

### Event Tests

Test tabular event data.

```python
def run_event_tests(test_case, schema):
    """Execute event_tests from a test case."""
    error_code = test_case["error_code"]
    event_tests = test_case["tests"].get("event_tests", {})
    
    for event_data in event_tests.get("fails", []):
        headers = event_data[0]
        rows = event_data[1:]
        issues = validate_events(headers, rows, schema)
        assert any(i.code == error_code for i in issues)
    
    for event_data in event_tests.get("passes", []):
        headers = event_data[0]
        rows = event_data[1:]
        issues = validate_events(headers, rows, schema)
        assert not any(i.code == error_code for i in issues)
```

### Combo Tests

Combined sidecar + event tests (most realistic).

```python
def run_combo_tests(test_case, schema):
    """Execute combo_tests from a test case."""
    error_code = test_case["error_code"]
    combo_tests = test_case["tests"].get("combo_tests", {})
    
    for combo in combo_tests.get("fails", []):
        sidecar = combo["sidecar"]
        headers = combo["events"][0]
        rows = combo["events"][1:]
        
        issues = validate_bids_dataset(sidecar, headers, rows, schema)
        assert any(i.code == error_code for i in issues)
    
    for combo in combo_tests.get("passes", []):
        sidecar = combo["sidecar"]
        headers = combo["events"][0]
        rows = combo["events"][1:]
        
        issues = validate_bids_dataset(sidecar, headers, rows, schema)
        assert not any(i.code == error_code for i in issues)
```

## Handling Definitions

Some tests require definitions to be loaded before validation:

```python
def run_test_with_definitions(test_case, schema):
    """Run test case with definition pre-loading."""
    # Load definitions first
    definitions = test_case.get("definitions", [])
    definition_dict = {}
    
    for def_string in definitions:
        name, definition = parse_definition(def_string)
        definition_dict[name] = definition
    
    # Now run tests with definitions available
    for hed_string in test_case["tests"]["string_tests"]["fails"]:
        issues = validate_hed_string(
            hed_string, 
            schema, 
            definitions=definition_dict
        )
        # ... assertions
```

## Error Code Mapping

Your validator might use different error codes. Use the `alt_codes` field:

```python
def check_error_match(issue, expected_code, alt_codes):
    """Check if an issue matches expected code or alternates."""
    if issue.code == expected_code:
        return True
    
    return issue.code in alt_codes
```

Example from test case:

```json
{
    "error_code": "TAG_INVALID",
    "alt_codes": ["PLACEHOLDER_INVALID"],
    ...
}
```

## CI/CD Integration

Add test suite validation to your CI pipeline:

**GitHub Actions Example**:

```yaml
name: HED Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Clone HED test suite
        run: |
          git clone https://github.com/hed-standard/hed-tests.git
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run HED test suite
        run: |
          python -m unittest tests.test_hed_validation -v
```

## Reporting Issues

If your validator produces different results:

1. **Verify the test case**: Ensure you're parsing the JSON correctly
2. **Check schema version**: Make sure you're using the correct schema
3. **Review the specification**: Check the HED specification for clarification
4. **File an issue**: Report discrepancies at https://github.com/hed-standard/hed-tests/issues

Include:

- Test case name and error code
- Expected vs actual behavior
- Your validator implementation (Python, JavaScript, etc.)
- Schema version used

## Best Practices

1. **Run all tests**: Don't cherry-pick - run the entire suite
2. **Automate execution**: Integrate tests into CI/CD
3. **Track coverage**: Monitor which tests pass/fail over time
4. **Update regularly**: Pull latest tests periodically
5. **Report discrepancies**: Help improve the test suite
6. **Use schema versions**: Respect the schema version in each test
7. **Handle all test types**: Support string, sidecar, event, and combo tests

## Example Integrations

### hed-python

The Python validator integrates these tests directly:

```python
# tests/test_validation_suite.py
import json
import unittest
from pathlib import Path

class TestValidationSuite(unittest.TestCase):
    def test_validation_suite(self):
        test_dir = Path("hed-tests/json_test_data/validation_tests")
        for test_file in test_dir.glob("*.json"):
            with self.subTest(test_file=test_file.name):
                with open(test_file) as f:
                    test_cases = json.load(f)
                # ... run tests
```

### hed-javascript

The JavaScript validator uses the consolidated file:

```javascript
// tests/validation.test.js
const testData = require('./hed-tests/json_test_data/validation_tests.json');

describe('HED Validation Suite', () => {
    testData.forEach(testCase => {
        // ... run tests
    });
});
```

### Using lookup dictionaries

Efficiently find tests for specific error codes:

```python
import json

# Find all tests that validate TAG_INVALID
with open('hed-tests/json_test_data/validation_code_dict.json') as f:
    code_dict = json.load(f)

tag_tests = code_dict.get('TAG_INVALID', [])
print(f"TAG_INVALID is validated by {len(tag_tests)} tests")

# Load only those tests
with open('hed-tests/json_test_data/validation_tests.json') as f:
    all_tests = json.load(f)

filtered_tests = [t for t in all_tests if t['name'] in tag_tests]
```

## Questions?

- **Issues**: https://github.com/hed-standard/hed-tests/issues
- **Discussions**: https://github.com/hed-standard/hed-tests/discussions
- **HED Homepage**: https://www.hedtags.org
