# HED Test Coverage Report

**Generated**: coverage.md

## Summary Statistics

- **Total error codes covered**: 33
- **Total test cases**: 136
- **Error codes with AI metadata**: 33 (100.0%)

## Test Type Coverage

- **combo_tests**: 23 error codes
- **event_tests**: 23 error codes
- **schema_tests**: 9 error codes
- **sidecar_tests**: 23 error codes
- **string_tests**: 24 error codes

## Coverage by Error Code

| Error Code                     | Test Cases | Test Types                                            | AI Metadata | Schema Versions                |
| ------------------------------ | ---------- | ----------------------------------------------------- | ----------- | ------------------------------ |
| CHARACTER_INVALID              | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.2.0, 8.4.0                   |
| COMMA_MISSING                  | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEFINITION_INVALID             | 10         | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEF_EXPAND_INVALID             | 6          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEF_INVALID                    | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| ELEMENT_DEPRECATED             | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.2.0                          |
| PARENTHESES_MISMATCH           | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| PLACEHOLDER_INVALID            | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SCHEMA_ATTRIBUTE_INVALID       | 1          | schema_tests                                          | ✓           |                                |
| SCHEMA_ATTRIBUTE_VALUE_INVALID | 12         | schema_tests                                          | ✓           |                                |
| SCHEMA_CHARACTER_INVALID       | 6          | schema_tests                                          | ✓           |                                |
| SCHEMA_DEPRECATION_ERROR       | 8          | schema_tests                                          | ✓           |                                |
| SCHEMA_DUPLICATE_NODE          | 2          | schema_tests                                          | ✓           |                                |
| SCHEMA_HEADER_INVALID          | 2          | schema_tests                                          | ✓           |                                |
| SCHEMA_LIBRARY_INVALID         | 8          | schema_tests                                          | ✓           |                                |
| SCHEMA_LOAD_FAILED             | 3          | string_tests                                          | ✓           | 8.1.0, 8.2.0, lang_1.1.0, sc:8 |
| SCHEMA_SECTION_MISSING         | 1          | schema_tests                                          | ✓           |                                |
| SIDECAR_BRACES_INVALID         | 5          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SIDECAR_INVALID                | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SIDECAR_KEY_MISSING            | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EMPTY                      | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXPRESSION_REPEATED        | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXTENDED                   | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXTENSION_INVALID          | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_GROUP_ERROR                | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_INVALID                    | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_NAMESPACE_PREFIX_INVALID   | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, sc:score_1.0.0, ts:8.3. |
| TAG_NOT_UNIQUE                 | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_REQUIRES_CHILD             | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TEMPORAL_TAG_ERROR             | 24         | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, 8.4.0                   |
| UNITS_INVALID                  | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| VALUE_INVALID                  | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, 8.4.0                   |
| WIKI_DELIMITERS_INVALID        | 1          | schema_tests                                          | ✓           |                                |

## Files

### CHARACTER_INVALID

- `CHARACTER_INVALID.json`

### COMMA_MISSING

- `COMMA_MISSING.json`

### DEFINITION_INVALID

- `DEFINITION_INVALID.json`

### DEF_EXPAND_INVALID

- `DEF_EXPAND_INVALID.json`

### DEF_INVALID

- `DEF_INVALID.json`

### ELEMENT_DEPRECATED

- `ELEMENT_DEPRECATED.json`

### PARENTHESES_MISMATCH

- `PARENTHESES_MISMATCH.json`

### PLACEHOLDER_INVALID

- `PLACEHOLDER_INVALID.json`

### SCHEMA_ATTRIBUTE_INVALID

- `SCHEMA_ATTRIBUTE_INVALID.json`

### SCHEMA_ATTRIBUTE_VALUE_INVALID

- `SCHEMA_ATTRIBUTE_VALUE_INVALID_ALLOWED_CHARACTER.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_DEFAULT_UNIT.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_HED_ID.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_IN_LIBRARY.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_NON_PLACEHOLDER_HAS_CLASS.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_RELATED_TAG.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_SUGGESTED_TAG.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_UNIT_CLASS.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_VALUE_CLASS.json`

### SCHEMA_CHARACTER_INVALID

- `SCHEMA_CHARACTER_INVALID.json`

### SCHEMA_DEPRECATION_ERROR

- `SCHEMA_DEPRECATION_ERROR.json`

### SCHEMA_DUPLICATE_NODE

- `SCHEMA_DUPLICATE_NODE.json`

### SCHEMA_HEADER_INVALID

- `SCHEMA_HEADER_INVALID.json`

### SCHEMA_LIBRARY_INVALID

- `SCHEMA_LIBRARY_INVALID.json`

### SCHEMA_LOAD_FAILED

- `SCHEMA_LOAD_FAILED.json`

### SCHEMA_SECTION_MISSING

- `SCHEMA_SECTION_MISSING.json`

### SIDECAR_BRACES_INVALID

- `SIDECAR_BRACES_INVALID.json`

### SIDECAR_INVALID

- `SIDECAR_INVALID.json`

### SIDECAR_KEY_MISSING

- `SIDECAR_KEY_MISSING.json`

### TAG_EMPTY

- `TAG_EMPTY.json`

### TAG_EXPRESSION_REPEATED

- `TAG_EXPRESSION_REPEATED.json`

### TAG_EXTENDED

- `TAG_EXTENDED.json`

### TAG_EXTENSION_INVALID

- `TAG_EXTENSION_INVALID.json`

### TAG_GROUP_ERROR

- `TAG_GROUP_ERROR.json`

### TAG_INVALID

- `TAG_INVALID.json`

### TAG_NAMESPACE_PREFIX_INVALID

- `SCHEMA_LOAD_FAILED.json`
- `TAG_NAMESPACE_PREFIX_INVALID.json`

### TAG_NOT_UNIQUE

- `TAG_NOT_UNIQUE.json`

### TAG_REQUIRES_CHILD

- `TAG_REQUIRES_CHILD.json`

### TEMPORAL_TAG_ERROR

- `TEMPORAL_TAG_ERROR.json`
- `TEMPORAL_TAG_ERROR_DELAY.json`

### UNITS_INVALID

- `UNITS_INVALID.json`

### VALUE_INVALID

- `VALUE_INVALID.json`

### WIKI_DELIMITERS_INVALID

- `SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`
