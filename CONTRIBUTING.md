# Contributing to HED Test Suite

Thank you for your interest in contributing to the HED Test Suite! This document provides guidelines for adding new tests, improving existing ones, and maintaining test quality.

## Table of contents

- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Adding New Test Cases](#adding-new-test-cases)
- [Test File Format](#test-file-format)
- [Validation and Quality](#validation-and-quality)
- [Pull Request Process](#pull-request-process)
- [Best Practices](#best-practices)
- [Questions and Support](#questions-and-support)

## Getting started

### Prerequisites

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/hed-tests.git
   cd hed-tests
   ```
3. **Set up the environment**:
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .venv/Scripts/activate.ps1
   pip install -e ".[dev,docs]"
   ```
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/add-new-tests
   ```

### Familiarize Yourself

Before contributing, review:

- [README.md](README.md) - Repository overview
- [docs/test_format.md](docs/test_format.md) - Complete format specification
- [docs/test_index.md](docs/test_index.md) - Existing test cases
- [src/schemas/test_schema.json](src/schemas/test_schema.json) - JSON schema

## Types of contributions

### 1. Adding new test cases

Add tests for:

- **Uncovered error codes**: Check [docs/test_coverage.md](docs/test_coverage.md)
- **Edge cases**: Unusual scenarios not yet tested
- **Common mistakes**: Real-world errors developers encounter
- **Complex scenarios**: Multi-condition tests

### 2. Improving existing tests

Enhance tests by:

- Adding AI-friendly metadata (`explanation`, `common_causes`, `correction_examples`)
- Including additional test types (sidecar, event, combo tests)
- Expanding failing/passing cases
- Clarifying descriptions

### 3. Documentation

Improve documentation:

- Clarify test format specifications
- Add integration examples
- Document new error codes
- Fix typos and formatting

### 4. Tooling

Enhance test infrastructure:

- Improve validation scripts
- Add coverage analysis features
- Create test generation utilities
- Enhance CI/CD workflows

## Adding new test cases

### Step 1: Identify the error code

Determine which error code your test validates. Error codes should match the HED specification:

- Validation errors: `TAG_INVALID`, `UNITS_INVALID`, etc.
- Schema errors: `SCHEMA_ATTRIBUTE_INVALID`, etc.

If adding a completely new error code, create a new test file.

### Step 2: Choose the test file

- **Existing error code**: Edit the corresponding file in `json_test_data/validation_tests/` or `json_test_data/schema_tests/`
- **New error code**: Create a new file named `ERROR_CODE.json`

### Step 3: Write the test case

Follow this template:

```json
{
    "error_code": "TAG_INVALID",
    "alt_codes": [],
    "name": "descriptive-test-name",
    "description": "Clear description of what this tests",
    "warning": false,
    "schema": "8.4.0",
    "error_category": "semantic",
    "common_causes": [
        "First common cause",
        "Second common cause"
    ],
    "explanation": "Detailed explanation for AI and developers",
    "correction_strategy": "How to fix this error",
    "correction_examples": [
        {
            "wrong": "Invalid HED string",
            "correct": "Corrected HED string",
            "explanation": "Why this correction works"
        }
    ],
    "definitions": [],
    "tests": {
        "string_tests": {
            "fails": [
                "HED string that should fail validation"
            ],
            "passes": [
                "HED string that should pass validation"
            ]
        }
    }
}
```

### Step 4: Include multiple test types

Whenever possible, include multiple test types:

#### String tests (Always include)

```json
"string_tests": {
    "fails": [
        "Invalidtag",
        "Red, Invalidtag"
    ],
    "passes": [
        "Red",
        "Event"
    ]
}
```

#### Sidecar tests (BIDS JSON)

```json
"sidecar_tests": {
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

#### Event tests (tabular data)

```json
"event_tests": {
    "fails": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Invalidtag"]
        ]
    ],
    "passes": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Event"]
        ]
    ]
}
```

#### Combo tests (realistic BIDS)

```json
"combo_tests": {
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

### Step 5: Add AI-Ffriendly metadata

**Always include** these fields for AI training:

#### explanation

Detailed explanation of why this error occurs:

```json
"explanation": "Tags must exist in the active HED schema. Each tag path must be found in the schema vocabulary, though extensions to valid tags are allowed using the extension syntax."
```

#### common_causes

List of typical reasons developers encounter this error:

```json
"common_causes": [
    "Typo in tag name",
    "Using a tag from a different schema version",
    "Attempting to use custom tags without proper extension syntax"
]
```

#### correction_strategy

General approach to fixing the error:

```json
"correction_strategy": "Verify the tag exists in the schema using the schema browser at hedtags.org. Check for typos, ensure you're using the correct schema version, or use proper extension syntax for custom additions."
```

#### correction_examples

Concrete before/after examples:

```json
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
]
```

### Step 6: Validate your test

Before committing, validate the test structure:

```powershell
.venv/Scripts/activate.ps1
python src/scripts/validate_test_structure.py json_test_data/validation_tests/YOUR_FILE.json
```

If validation passes, check coverage:

```powershell
python src/scripts/check_coverage.py
```

## Test file format

### Required fields

- `error_code` (string): The error code being tested
- `name` (string): Unique test identifier (lowercase-with-hyphens)
- `description` (string): Human-readable test description
- `schema` (string): HED schema version
- `tests` (object): Must contain at least one test type

### Optional but recommended

- `alt_codes` (array): Alternative error codes
- `warning` (boolean): Is this a warning instead of error?
- `error_category` (string): Semantic category
- `common_causes` (array): **Highly recommended for AI**
- `explanation` (string): **Highly recommended for AI**
- `correction_strategy` (string): **Highly recommended for AI**
- `correction_examples` (array): **Highly recommended for AI**
- `definitions` (array): Definitions needed for tests

### Naming conventions

**File names**: `ERROR_CODE.json`

- Uppercase with underscores
- Example: `TAG_INVALID.json`

**Test names**: `error-code-specific-scenario`

- Lowercase with hyphens
- Descriptive but concise
- Example: `tag-invalid-in-sidecar`

## Validation and quality

### JSON schema validation

All tests must pass JSON schema validation:

```powershell
python src/scripts/validate_test_structure.py json_test_data/validation_tests/
python src/scripts/validate_test_structure.py json_test_data/schema_tests/
```

### Quality checklist

Before submitting a PR, ensure:

- [ ] **Valid JSON**: No syntax errors
- [ ] **Passes schema validation**: Validated with `validate_test_structure.py`
- [ ] **Both fails and passes**: Each test type includes both
- [ ] **AI metadata included**: Explanation, causes, corrections
- [ ] **Clear descriptions**: Self-explanatory test names
- [ ] **Correct schema version**: Matches the schema you tested against
- [ ] **Realistic examples**: Uses practical HED strings
- [ ] **Multiple test types**: Includes string tests at minimum

### Testing against validators

If possible, test your cases against existing validators:

**Python (hed-python)**:

```python
from hed import HedString, load_schema

schema = load_schema('8.4.0')
hed_string = HedString("Your test string", schema)
issues = hed_string.validate()
# Verify error code appears/doesn't appear as expected
```

**JavaScript (hed-javascript)**:

```javascript
const { validateHedString } = require('hed-javascript');
const issues = validateHedString('Your test string', schema);
// Verify error code appears/doesn't appear as expected
```

## Pull request process

### 1. Commit your changes

Write clear commit messages:

```bash
git add json_test_data/validation_tests/TAG_INVALID.json
git commit -m "Add edge case tests for TAG_INVALID

- Add test for invalid tag in nested groups
- Include combo test with sidecar + events
- Add AI-friendly correction examples"
```

### 2. Push to your fork

```bash
git push origin feature/add-new-tests
```

### 3. Create pull request

- Go to your fork on GitHub
- Click "Pull Request"
- Provide a clear title and description
- Reference any related issues

### PR Description template

```markdown
## Description
Brief summary of changes.

## Changes made
- Added X new test cases for ERROR_CODE
- Improved Y test with additional metadata
- Fixed Z validation issue

## Testing
- [x] Validated with validate_test_structure.py
- [x] Checked coverage with check_coverage.py
- [x] Tested against hed-python validator

## Related issues
Closes #123
```

### 4. Address review feedback

Maintainers will review and may request changes. Address feedback by:

1. Making requested changes
2. Committing updates
3. Pushing to your branch (PR updates automatically)

### 5. Merge

Once approved, maintainers will merge your PR.

## Best practices

### Writing tests

1. **Start simple**: Begin with string_tests, add complexity later
2. **Test edge cases**: Include unusual but valid scenarios
3. **Be comprehensive**: Test both obvious and subtle cases
4. **Use real examples**: Base tests on actual developer mistakes
5. **Think about AI**: Write explanations that help machines learn

### Organization

1. **One error per file**: Keep files focused on single error codes
2. **Logical naming**: Use descriptive, consistent names
3. **Group related tests**: Put similar scenarios in the same file
4. **Document special cases**: Add comments if test is unusual

### Maintenance

1. **Update coverage docs**: Run `check_coverage.py` after changes
2. **Regenerate index**: Run `generate_test_index.py` if adding tests
3. **Check consolidation**: Run `consolidate_tests.py` to update consolidated files and dictionaries
4. **Keep schemas current**: Test against latest HED schema versions

## Examples

### Good test case

```json
{
    "error_code": "TAG_INVALID",
    "name": "tag-invalid-nested-groups",
    "description": "Test invalid tags within nested groups",
    "schema": "8.4.0",
    "error_category": "semantic",
    "common_causes": [
        "Typo in tag name within complex annotation"
    ],
    "explanation": "Even within nested groups, all tags must exist in the schema.",
    "correction_strategy": "Verify each tag path in nested groups using the schema browser.",
    "correction_examples": [
        {
            "wrong": "(Red, (Invalidtag, Blue))",
            "correct": "(Red, (Event, Blue))",
            "explanation": "Replace invalid nested tag with valid schema tag"
        }
    ],
    "tests": {
        "string_tests": {
            "fails": [
                "(Red, (Invalidtag, Blue))",
                "(Onset, (Invalidtag))"
            ],
            "passes": [
                "(Red, (Event, Blue))",
                "(Onset, (Event))"
            ]
        }
    }
}
```

### Bad test case

```json
{
    "error_code": "TAG_INVALID",
    "name": "test1",
    "description": "test",
    "schema": "8.4.0",
    "tests": {
        "string_tests": {
            "fails": ["x"],
            "passes": ["y"]
        }
    }
}
```

**Problems**:

- Non-descriptive name ("test1")
- Vague description ("test")
- No AI metadata
- Unclear test strings ("x", "y")
- Missing error category
- No correction examples

## Questions and support

### Before asking

1. Read [docs/test_format.md](docs/test_format.md)
2. Check [docs/test_index.md](docs/test_index.md) for similar tests
3. Review existing test files for examples
4. Run validation scripts to identify issues

### Getting help

- **Questions**: Open a [GitHub Discussion](https://github.com/hed-standard/hed-tests/discussions)
- **Bug reports**: File an [issue](https://github.com/hed-standard/hed-tests/issues)
- **Feature requests**: Open an issue with `enhancement` label
- **Email**: Contact [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)

### Useful resources

- **HED specification**: https://www.hedtags.org/hed-specification
- **Schema browser**: https://www.hedtags.org/hed-schema-browser
- **HED homepage**: https://www.hedtags.org
- **Python validator**: https://github.com/hed-standard/hed-python
- **JavaScript validator**: https://github.com/hed-standard/hed-javascript

## Code of conduct

Please be respectful and professional in all interactions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank you!

Your contributions help make HED validation more consistent, reliable, and accessible. Thank you for helping improve the HED ecosystem!
