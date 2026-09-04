# HED test suite index

Complete index of 189 test cases in the HED test suite.

## Quick navigation

- [CHARACTER_INVALID](#character-invalid) (4 tests)
- [COMMA_MISSING](#comma-missing) (2 tests)
- [DEFINITION_INVALID](#definition-invalid) (10 tests)
- [DEF_EXPAND_INVALID](#def-expand-invalid) (6 tests)
- [DEF_INVALID](#def-invalid) (3 tests)
- [ELEMENT_DEPRECATED](#element-deprecated) (1 test)
- [PARENTHESES_MISMATCH](#parentheses-mismatch) (2 tests)
- [PLACEHOLDER_INVALID](#placeholder-invalid) (4 tests)
- [SCHEMA_ATTRIBUTE_INVALID](#schema-attribute-invalid) (1 test)
- [SCHEMA_ATTRIBUTE_VALUE_INVALID](#schema-attribute-value-invalid) (12 tests)
- [SCHEMA_CHARACTER_INVALID](#schema-character-invalid) (6 tests)
- [SCHEMA_DEPRECATION_ERROR](#schema-deprecation-error) (8 tests)
- [SCHEMA_DUPLICATE_NODE](#schema-duplicate-node) (2 tests)
- [SCHEMA_HEADER_INVALID](#schema-header-invalid) (3 tests)
- [SCHEMA_LIBRARY_INVALID](#schema-library-invalid) (18 tests)
- [SCHEMA_LOAD_FAILED](#schema-load-failed) (41 tests)
- [SCHEMA_MISSING_EXTRA](#schema-missing-extra) (1 test)
- [SCHEMA_SECTION_MISSING](#schema-section-missing) (1 test)
- [SIDECAR_BRACES_INVALID](#sidecar-braces-invalid) (5 tests)
- [SIDECAR_INVALID](#sidecar-invalid) (2 tests)
- [SIDECAR_KEY_MISSING](#sidecar-key-missing) (2 tests)
- [TAG_EMPTY](#tag-empty) (3 tests)
- [TAG_EXPRESSION_REPEATED](#tag-expression-repeated) (3 tests)
- [TAG_EXTENDED](#tag-extended) (1 test)
- [TAG_EXTENSION_INVALID](#tag-extension-invalid) (2 tests)
- [TAG_GROUP_ERROR](#tag-group-error) (4 tests)
- [TAG_INVALID](#tag-invalid) (3 tests)
- [TAG_NAMESPACE_PREFIX_INVALID](#tag-namespace-prefix-invalid) (3 tests)
- [TAG_NOT_UNIQUE](#tag-not-unique) (1 test)
- [TAG_REQUIRES_CHILD](#tag-requires-child) (1 test)
- [TEMPORAL_TAG_ERROR](#temporal-tag-error) (24 tests)
- [UNITS_INVALID](#units-invalid) (5 tests)
- [VALUE_INVALID](#value-invalid) (4 tests)
- [WIKI_DELIMITERS_INVALID](#wiki-delimiters-invalid) (1 test)

## CHARACTER_INVALID

**File**: `json_test_data/validation_test_data/CHARACTER_INVALID.json`

### character-invalid-non-printing-appears (correction guidance) (examples)

**Description**: The HED string contains a UTF-8 character.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### curly-braces-not-in-sidecar (correction guidance) (examples)

**Description**: The curly brace notation is used outside a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass

### invalid-character-name-value-class (correction guidance) (examples)

**Description**: An invalid character was used in an 8.3.0 or greater style name value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 5 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass
- `combo_tests`: 1 fail, 0 pass

### invalid-character-name-value-class-early-schema (correction guidance) (examples)

**Description**: An invalid character was as a value in a placeholder or as a tag extension.

**Schema**: 8.2.0 **Category**: validation

**Tests**:

- `string_tests`: 4 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass

## COMMA_MISSING

**File**: `json_test_data/validation_test_data/COMMA_MISSING.json`

### comma-missing-tag-and-group (correction guidance) (examples)

**Description**: A tag and a tag group are not separated by commas: A(B,D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### comma-missing-tag-groups (correction guidance) (examples)

**Description**: Two tag groups are not separated by commas: (A, B)(C, D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEFINITION_INVALID

**File**: `json_test_data/validation_test_data/DEFINITION_INVALID.json`

### definition-invalid-bad-number-of-placeholders (correction guidance) (examples)

**Description**: A definition that includes a placeholder (`#`) does not have exactly two `#` characters.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-content-has-top-level-tag (correction guidance) (examples)

**Description**: A tag with a required or unique attribute appears in a definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-empty-inner-group (correction guidance) (examples)

**Description**: A definition's enclosing tag group has an empty inner group (i.e., the definition's contents).

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-inner-group-defs (correction guidance) (examples)

**Description**: A definition's inner tag group contains `Definition`, `Def` or `Def-expand` tags.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definition-tags (correction guidance) (examples)

**Description**: A definition's enclosing tag group contains more than a `Definition` tag and an inner group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definitions (correction guidance) (examples)

**Description**: Multiple `Definition` tags with same name are encountered.

**Schema**: 8.4.0 **Category**: uniqueness

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-conflict (correction guidance) (examples)

**Description**: Definitions of the same name appear with and without a `#`.

**Schema**: 8.4.0 **Category**: consistency

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-incorrect-of-positions (correction guidance) (examples)

**Description**: A definition has placeholders (`#`) in incorrect positions.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-tag-group (correction guidance) (examples)

**Description**: A Definition tag does not appear in a tag group at the top level in an annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 0 pass
- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-not-allowed-here (correction guidance) (examples)

**Description**: A definition appears in an unexpected place such as an events file or sidecar.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_EXPAND_INVALID

**File**: `json_test_data/validation_test_data/DEF_EXPAND_INVALID.json`

### def-expand-has-extras (correction guidance) (examples)

**Description**: A Def-expand has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-bad-placeholder-value-or-units (correction guidance) (examples)

**Description**: A `Def-expand` has an incorrect type of placeholder value.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-missing-placeholder (correction guidance) (examples)

**Description**: A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-name-not-definition (correction guidance) (examples)

**Description**: A `Def-expand` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-tags-not-in-definition (correction guidance) (examples)

**Description**: The tags within a Def-expand do not match the corresponding definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-missing-inner-group (correction guidance) (examples)

**Description**: A Def-expand is missing its inner group containing the definition.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_INVALID

**File**: `json_test_data/validation_test_data/DEF_INVALID.json`

### def-invalid-bad-placeholder-value (correction guidance) (examples)

**Description**: A `Def` has a placeholder value of incorrect format or units for definition.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-missing-placeholder (correction guidance) (examples)

**Description**: A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-name (correction guidance) (examples)

**Description**: A `Def` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## ELEMENT_DEPRECATED

**File**: `json_test_data/validation_test_data/ELEMENT_DEPRECATED.json`

### tag-deprecated (warning) (correction guidance) (examples)

**Description**: A tag is deprecated

**Schema**: 8.2.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PARENTHESES_MISMATCH

**File**: `json_test_data/validation_test_data/PARENTHESES_MISMATCH.json`

### parentheses-mismatch-incorrect-nesting (correction guidance) (examples)

**Description**: The open and closed parentheses are not correctly nested in the HED string.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### parentheses-mismatch-unmatched-parentheses (correction guidance) (examples)

**Description**: A HED string does not have the same number of open and closed parentheses.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PLACEHOLDER_INVALID

**File**: `json_test_data/validation_test_data/PLACEHOLDER_INVALID.json`

### placeholder-invalid-#-in-categorical-column (correction guidance) (examples)

**Description**: A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-#-misplaced (correction guidance) (examples)

**Description**: A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.

**Schema**: 8.4.0 **Category**: schema

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-value-column (correction guidance) (examples)

**Description**: A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.

**Schema**: 8.4.0 **Category**: count

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-misplaced (correction guidance) (examples)

**Description**: A `#` appears in a place that it should not (such as in the `HED` column of an event file outside a definition).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SCHEMA_ATTRIBUTE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_INVALID.json`

### attribute-invalid-unknown (correction guidance) (examples)

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

## SCHEMA_ATTRIBUTE_VALUE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-factor-invalid (correction guidance) (examples)

**Description**: A schema unit has an invalid conversion factor

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 4 fail, 1 pass

### attribute-default-unit-invalid (correction guidance) (examples)

**Description**: A schema unit class has an invalid default value

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-allowed-character (correction guidance) (examples)

**Description**: A schema value class has an invalid allowedCharacter attribute value

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### attribute-invalid-hed-id-changed (correction guidance) (examples)

**Description**: A schema element has a hedId that changed from its previously assigned value.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-invalid (correction guidance) (examples)

**Description**: A schema element has a hedId with an invalid format (non-numeric or malformed).

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-out-range (correction guidance) (examples)

**Description**: A schema element has a hedId that is outside the valid allocated range for its section.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-in-library (correction guidance) (examples)

**Description**: A schema element has an invalid inLibrary attribute (most other library errors are SCHEMA_LIBRARY_INVALID)

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-unit-class (correction guidance) (examples)

**Description**: A schema unit class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-value-class (correction guidance) (examples)

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-on-nonplaceholder-invalid (correction guidance) (examples)

**Description**: A non placeholder tag has takes value, unit class, or value class

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### attribute-relatedTag-invalid (correction guidance) (examples)

**Description**: A related tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

### attribute-suggestedTag-invalid (correction guidance) (examples)

**Description**: A suggested tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 2 pass

## SCHEMA_CHARACTER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_CHARACTER_INVALID.json`

### schema-character-allowed-character-unit

**Description**: Allowed character properly works on units.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-character-invalid-description

**Description**: Description does not contain banned characters.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-other-term

**Description**: Invalid character in a non-tag schema element name (unit, unit class, modifier, value class, attribute, or property).

**Schema**: any

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### schema-character-invalid-prologue (correction guidance) (examples)

**Description**: Invalid character in prologue or epilogue.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-tag

**Description**: Invalid character in a tag term.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-utf8-other-term

**Description**: UTF8 characters (valid) in term.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

## SCHEMA_DEPRECATION_ERROR

**File**: `json_test_data/schema_test_data/SCHEMA_DEPRECATION_ERROR.json`

### schema-deprecated-attribute-invalid (correction guidance) (examples)

**Description**: A schema attribute issue, saying there is an unhandled deprecated attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-default-unit

**Description**: A schema deprecation issue, deprecated default units

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-deprecated-deprecated-attribute

**Description**: A schema deprecation issue, an attribute of an element is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 5 fail, 5 pass

### schema-deprecated-deprecated-property

**Description**: A schema deprecation issue, a property of an attribute is is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-invalid-child

**Description**: A schema deprecation issue, saying there is an invalid child of a deprecated node

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-invalid-suggested-related-tag

**Description**: A schema deprecation issue, saying a related or suggested tag points to a deprecated tag

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 4 pass

### schema-deprecated-unit-class

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-value-class

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_DUPLICATE_NODE

**File**: `json_test_data/schema_test_data/SCHEMA_DUPLICATE_NODE.json`

### attribute-duplicate-node (correction guidance) (examples)

**Description**: A schema attribute issue, saying there is a duplicate node.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### attribute-duplicate-node-unit

**Description**: A schema has duplicate unit entries with case-insensitive name collision.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_HEADER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_HEADER_INVALID.json`

### schema-header-malformed-attribute (correction guidance) (examples)

**Description**: A schema header contains a malformed or unknown attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-header-unknown-attribute

**Description**: An unknown attribute was found in the schema header.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-header-unmerged-value-variants (correction guidance) (examples)

**Description**: The unmerged header attribute value is case-insensitive, and unmerged="false" is equivalent to omitting the attribute (the schema is merged).

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 0 fail, 3 pass

## SCHEMA_LIBRARY_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_LIBRARY_INVALID.json`

### library-invalid-bad-name (correction guidance) (examples)

**Description**: A schema library issue, indicating the name is invalid.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### library-invalid-bad_with-standard

**Description**: A schema library issue, the with-standard attribute is present without the library attribute.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-bad_with-standard-version

**Description**: A schema library issue, indicating it references a version of the standard that can't be found.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-duplicate-schema-attribute (correction guidance) (examples)

**Description**: An unmerged partnered library schema declares a schema attribute whose name already exists in its standard schema partner.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-duplicate-standard-tag

**Description**: An unmerged library schema declares a tag whose name already exists in its standard schema partner.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-duplicate-unit

**Description**: A library schema defines elements that duplicate entries already in the base standard schema.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-duplicate-unit-modifier (correction guidance) (examples)

**Description**: An unmerged partnered library schema declares a unit modifier whose name already exists in its standard schema partner.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-duplicate-value-class (correction guidance) (examples)

**Description**: An unmerged partnered library schema declares a value class whose name already exists in its standard schema partner.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-inlibrary-in-unmerged

**Description**: A schema library issue, indicating the InLibrary attribute appears when it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-merged-properties-mismatch (correction guidance) (examples)

**Description**: A merged partnered library schema's Properties section must be identical to that of its standard schema partner.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-merged-rooted-not-under-anchor (correction guidance) (examples)

**Description**: In a merged library schema, a node with rooted=XXX must be a direct child of XXX.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-properties-in-unmerged (correction guidance) (examples)

**Description**: An unmerged partnered library schema has a non-empty Properties section.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-reserved-in-unmerged (correction guidance) (examples)

**Description**: The reserved attribute cannot be used in an unmerged partnered library schema.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-in-unpartnered (correction guidance) (examples)

**Description**: The rooted attribute appears in an unpartnered library schema, whose header has no withStandard attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-not-in-base

**Description**: A schema library issue, rooted tag does not exist.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-rooted-not-top-level

**Description**: A schema library issue, indicating a node is being rooted that is not a top level node.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-present

**Description**: A schema library issue, indicating the rooted property appears in a file it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-unpartnered-properties-allowed (correction guidance) (examples)

**Description**: An unpartnered library schema may declare its own schema attributes and a non-empty Properties section.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 0 fail, 1 pass

## SCHEMA_LOAD_FAILED

**File**: `json_test_data/validation_test_data/SCHEMA_LOAD_FAILED.json`

### aux-identical-elements-compatible (correction guidance) (examples)

**Description**: Two libraries may declare the same auxiliary elements when the declarations are identical.

**Schema**: testaux_1.0.0, testclash_13.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### aux-new-unit-class-merges-directly (correction guidance) (examples)

**Description**: New library schema auxiliary elements (unit classes with their units, unit modifiers, value classes, and schema attributes) are merged directly into the group vocabulary.

**Schema**: testconflict_2.0.0, testaux_1.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 3 pass

### aux-new-units-under-shared-class (correction guidance) (examples)

**Description**: A library may add new units under a shared unit class when the shared units themselves are identical.

**Schema**: testaux_1.0.0, testclash_15.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### aux-schema-attribute-description-conflict (correction guidance) (examples)

**Description**: Library schemas sharing a schema attribute must give it the same description.

**Schema**: testaux_1.0.0, testclash_18.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### aux-schema-attribute-property-conflict (correction guidance) (examples)

**Description**: Library schemas sharing a schema attribute must give it the same properties.

**Schema**: testaux_1.0.0, testclash_17.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### aux-unit-attribute-conflict (correction guidance) (examples)

**Description**: Library schemas sharing a unit must give it identical attribute values.

**Schema**: testaux_1.0.0, testclash_14.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### aux-unit-modifier-conflict (correction guidance) (examples)

**Description**: Library schemas sharing a unit modifier must give it identical attribute values.

**Schema**: testaux_1.0.0, testclash_19.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### aux-value-class-conflict (correction guidance) (examples)

**Description**: Library schemas sharing a value class must give it identical attribute values.

**Schema**: testaux_1.0.0, testclash_16.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### conflicting-libraries-in-separate-namespaces (correction guidance) (examples)

**Description**: A library pair that fails to merge loads once one member is given its own namespace prefix.

**Schema**: testconflict_2.0.0, cl:testclash_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### different-standard-schemas-in-same-merge-group (correction guidance) (examples)

**Description**: A standard schema version in a merge group must match the withStandard partner of the group's library schemas.

**Schema**: 8.4.0, testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### duplicate-schema-in-merge-group (correction guidance) (examples)

**Description**: The same schema (same name and version) listed twice in one merge group loads; the duplicate is ignored.

**Schema**: testconflict_2.0.0, testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### element-conflict-ancestor-path (correction guidance) (examples)

**Description**: Library schemas sharing an element must place it at the same position in the hierarchy.

**Schema**: testconflict_2.0.0, testclash_4.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-attribute-value (correction guidance) (examples)

**Description**: Library schemas sharing an element must give it identical attribute values.

**Schema**: testconflict_2.0.0, testclash_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-description (correction guidance) (examples)

**Description**: Library schemas sharing an element must give it the same description.

**Schema**: testconflict_2.0.0, testclash_3.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-in-shared-child (correction guidance) (examples)

**Description**: A changed shared child makes libraries incompatible even when their non-shared siblings would be allowed.

**Schema**: testconflict_2.0.0, testclash_9.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-in-shared-grandchild (correction guidance) (examples)

**Description**: The element compatibility rules recurse into every depth of a shared hierarchy.

**Schema**: testconflict_2.0.0, testclash_12.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-order-independent (correction guidance) (examples)

**Description**: An element conflict between two libraries fails the merge whichever library is listed first; schemas in a merge group can be combined in any order.

**Schema**: testclash_2.0.0, testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-placeholder-child (correction guidance) (examples)

**Description**: A shared element must have a placeholder (#) child in all schemas that declare it or in none.

**Schema**: testconflict_2.0.0, testclash_5.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-rooted-different-anchors (correction guidance) (examples)

**Description**: A shared rooted tag must be rooted at the same standard schema node in every library.

**Schema**: testconflict_2.0.0, testclash_7.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### element-conflict-rooted-vs-top-level (correction guidance) (examples)

**Description**: A tag rooted in the standard schema in one library cannot merge with an unrooted top-level tag of the same name in another.

**Schema**: testconflict_2.0.0, testclash_6.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### extra-standard-schemas-in-same-merge-group (correction guidance) (examples)

**Description**: A standard schema in a merge group is allowed when it matches the group partner and adds nothing to the merged result.

**Schema**: 8.5.0, testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### incompatible-merge-schemas (correction guidance) (examples)

**Description**: Library schemas in a merge group must all have the same standard schema partner.

**Schema**: testconflict_2.0.0, testminimal_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### merge-order-independent-loads (correction guidance) (examples)

**Description**: Reordering the schemas of a loadable merge group does not change the result; schemas in a merge group can be combined in any order.

**Schema**: testminimal_2.1.0, testclash_1.0.0, testconflict_2.1.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### multiple-libraries-with-same-partner (correction guidance) (examples)

**Description**: Several library schemas with the same standard schema partner merge into one namespace.

**Schema**: testconflict_2.1.0, testclash_1.0.0, testminimal_2.1.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### namespaced-groups-load-independently (correction guidance) (examples)

**Description**: Schemas with different namespace prefixes form independent merge groups whose partners need not match.

**Schema**: 8.4.0, sc:testconflict_2.1.0, ts:testminimal_1.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### nonexistent-schema-version-in-group (correction guidance) (examples)

**Description**: A schema version that does not exist cannot be loaded.

**Schema**: 8.5.0, testconflict_99.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### partnered-library-alone-loads-with-partner (correction guidance) (examples)

**Description**: A partnered library schema listed alone automatically includes its standard schema partner.

**Schema**: testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### prefixed-group-with-mismatched-partners (correction guidance) (examples)

**Description**: The partnered-combination rules apply inside each prefixed merge group, not only to unprefixed schemas.

**Schema**: 8.5.0, sc:testconflict_2.0.0, sc:testminimal_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### prefixed-standard-schema-forms-own-group (correction guidance) (examples)

**Description**: A standard schema under a namespace prefix forms its own merge group independent of the unprefixed group.

**Schema**: 8.5.0, sc:8.4.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### same-library-two-incompatible-versions (correction guidance) (examples)

**Description**: Two versions of the same library cannot appear in one merge group, even when they differ only by a patch-level change such as a revised element description.

**Schema**: testconflict_2.1.0, testconflict_2.1.1 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### same-library-two-versions-in-group (correction guidance) (examples)

**Description**: Two different versions of the same library schema cannot appear in the same merge group.

**Schema**: testconflict_2.0.0, testconflict_2.1.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### same-library-two-versions-in-separate-namespaces (correction guidance) (examples)

**Description**: Two versions of one library load together when each version has its own namespace.

**Schema**: testconflict_2.1.0, alt:testconflict_2.1.1 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### shared-element-compatible-across-libraries (correction guidance) (examples)

**Description**: Two libraries may declare the same element when the declarations are identical.

**Schema**: testconflict_2.0.0, testclash_1.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### shared-hierarchy-diverges-at-grandchild (correction guidance) (examples)

**Description**: Libraries sharing an identical chain of elements may diverge below it.

**Schema**: testconflict_2.0.0, testclash_11.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### shared-rooted-hierarchy-different-children (correction guidance) (examples)

**Description**: A shared element may have different non-placeholder children in different libraries.

**Schema**: testconflict_2.0.0, testclash_8.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### shared-rooted-tag-disjoint-children (correction guidance) (examples)

**Description**: A shared element's children may be entirely disjoint between libraries.

**Schema**: testconflict_2.0.0, testclash_10.0.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### standard-schema-after-library-loads (correction guidance) (examples)

**Description**: A standard schema matching the group partner may appear anywhere in the list; schemas in a merge group can be combined in any order.

**Schema**: testconflict_2.0.0, 8.5.0 **Category**: schema

**Tests**:

- `string_tests`: 0 fail, 2 pass

### standard-schema-after-library-mismatch (correction guidance) (examples)

**Description**: A standard schema that differs from the group partner fails wherever it appears in the list; schemas in a merge group can be combined in any order.

**Schema**: testconflict_2.0.0, 8.4.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### two-standard-versions-in-same-merge-group (correction guidance) (examples)

**Description**: Two different standard schema versions cannot appear in the same merge group.

**Schema**: 8.4.0, 8.5.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### two-unpartnered-libraries-in-same-namespace (correction guidance) (examples)

**Description**: Two unpartnered library schemas cannot share one namespace prefix.

**Schema**: ts:testconflict_1.1.2, ts:testminimal_1.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

### unpartnered-library-in-shared-namespace (correction guidance) (examples)

**Description**: An unpartnered library schema cannot share a namespace with other schemas.

**Schema**: 8.5.0, testconflict_1.1.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

## SCHEMA_MISSING_EXTRA

**File**: `json_test_data/schema_test_data/SCHEMA_MISSING_EXTRA.json`

### schema-missing-extra (warning) (correction guidance) (examples)

**Description**: An extras section (Sources, Prefixes, or External annotations) has a row with an empty column value.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 8 fail, 1 pass

## SCHEMA_SECTION_MISSING

**File**: `json_test_data/schema_test_data/SCHEMA_SECTION_MISSING.json`

### schema-section-missing (correction guidance) (examples)

**Description**: A required schema section is missing from the schema file.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 9 fail, 1 pass

## SIDECAR_BRACES_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_BRACES_INVALID.json`

### sidecar-braces-appear-as-value-rather-than-tag (correction guidance) (examples)

**Description**: The curly braces are in a value rather than as a separate tag substitute.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### sidecar-braces-circular-reference (correction guidance) (examples)

**Description**: The item in curly braces has a HED annotation that contains curly braces.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-contents-invalid (correction guidance) (examples)

**Description**: The item in curly braces is not the word HED or a column name with HED annotations in the sidecar.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-invalid-spot (correction guidance) (examples)

**Description**: A curly brace reference must only appear where a tag could.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass

### sidecar-braces-self-reference (correction guidance) (examples)

**Description**: The item in curly braces has a HED annotation that contains itself.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 1 fail, 3 pass
- `combo_tests`: 1 fail, 2 pass

## SIDECAR_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_INVALID.json`

### sidecar-invalid-key-at-wrong-level (correction guidance) (examples)

**Description**: The HED key is not a second-level dictionary key.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### sidecar-invalid-na-annotated (correction guidance) (examples)

**Description**: An annotation entry is provided for `n/a`.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SIDECAR_KEY_MISSING

**File**: `json_test_data/validation_test_data/SIDECAR_KEY_MISSING.json`

### sidecar-key-missing (warning) (correction guidance) (examples)

**Description**: A value in a categorical column does not have an expected entry in a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `combo_tests`: 1 fail, 1 pass

### sidecar-refers-to-missing-tsv-hed-column (warning) (correction guidance) (examples)

**Description**: (Warning) A sidecar uses a \{HED} column which does not appear in the corresponding tsv file.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EMPTY

**File**: `json_test_data/validation_test_data/TAG_EMPTY.json`

### tag-empty-begin-end-comma (correction guidance) (examples)

**Description**: A HED string begins or ends with a comma (ignoring white space).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-empty-parentheses (correction guidance) (examples)

**Description**: A tag group is empty (i.e., empty parentheses are not allowed).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-extra-commas-or-parentheses (correction guidance) (examples)

**Description**: A HED string has extra commas or parentheses separated by only white space.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 5 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXPRESSION_REPEATED

**File**: `json_test_data/validation_test_data/TAG_EXPRESSION_REPEATED.json`

### tag-expression-repeated-same-level (correction guidance) (examples)

**Description**: A tag is repeated in the same tag group or level.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-duplicated-across-multiple-rows (correction guidance) (examples)

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: duplication

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-with-duplicated-onsets-across-multiple-rows (correction guidance) (examples)

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENDED

**File**: `json_test_data/validation_test_data/TAG_EXTENDED.json`

### tag-extended-extension (warning) (correction guidance) (examples)

**Description**: A tag represents an extension from the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 7 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENSION_INVALID

**File**: `json_test_data/validation_test_data/TAG_EXTENSION_INVALID.json`

### tag-extension-invalid-bad-node-name (correction guidance) (examples)

**Description**: A tag extension term does not comply with rules for schema nodes.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-extension-invalid-duplicate (correction guidance) (examples)

**Description**: A tag extension term is already in the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_GROUP_ERROR

**File**: `json_test_data/validation_test_data/TAG_GROUP_ERROR.json`

### multiple-top-level-tags-in-same-group (correction guidance) (examples)

**Description**: Multiple tags with the topLevelTagGroup attribute appear in the same top-level tag group. (Delay and Duration are allowed to be in the same topLevelTagGroup).

**Schema**: 8.4.0 **Category**: cardinality

**Tests**:

- `string_tests`: 4 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-deferred-in-splice (correction guidance) (examples)

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-missing (correction guidance) (examples)

**Description**: A tag has tagGroup or topLevelTagGroup attribute, but is not enclosed in parentheses.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 5 fail, 4 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-not-top-level (correction guidance) (examples)

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_INVALID

**File**: `json_test_data/validation_test_data/TAG_INVALID.json`

### tag-has-extra-whitespace (correction guidance) (examples)

**Description**: A HED tag has extra internal whitespace, including directly before or after slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-has-leading-trailing-or-consecutive-slashes (correction guidance) (examples)

**Description**: A HED tag has leading, trailing or consecutive slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 8 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-invalid-in-schema (correction guidance) (examples)

**Description**: The tag is not valid in the schema it is associated with.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_NAMESPACE_PREFIX_INVALID

**File**: `json_test_data/validation_test_data/TAG_NAMESPACE_PREFIX_INVALID.json`

### tag-namespace_prefix-invalid-characters (correction guidance) (examples)

**Description**: A tag prefix has invalid characters.

**Schema**: 8.5.0, sc:testconflict_2.1.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-namespace_prefix-with-colon-values (correction guidance) (examples)

**Description**: A tag prefix has invalid characters.

**Schema**: ts:8.5.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-with-namespace-has-no-schema (correction guidance) (examples)

**Description**: A tag starting with name: does not have an associated schema.

**Schema**: 8.5.0, sc:testconflict_2.1.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_NOT_UNIQUE

**File**: `json_test_data/validation_test_data/TAG_NOT_UNIQUE.json`

### tag-not-unique (correction guidance) (examples)

**Description**: A tag with unique attribute appears more than once in an event-level HED string.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_REQUIRES_CHILD

**File**: `json_test_data/validation_test_data/TAG_REQUIRES_CHILD.json`

### tag-requires-child-missing (correction guidance) (examples)

**Description**: A tag has the requireChild schema attribute but does not have a child.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TEMPORAL_TAG_ERROR

**File**: `json_test_data/validation_test_data/TEMPORAL_TAG_ERROR.json`

### na-in-onset column (correction guidance) (examples)

**Description**: n/a is in the onset column.

**Schema**: 8.4.0 **Category**: data_format

**Tests**:

- `combo_tests`: 2 fail, 2 pass

### temporal-tag-error-duplicated-onset-or-offset (correction guidance) (examples)

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duplicated-onset-or-offset-delay (correction guidance) (examples)

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duration-group (correction guidance) (examples)

**Description**: A Duration or Delay has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 0 fail, 1 pass

### temporal-tag-error-extra tags (correction guidance) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-extra tags-delay (correction guidance) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras (correction guidance) (examples)

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras-delay (correction guidance) (examples)

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event (correction guidance) (examples)

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event-delay (correction guidance) (examples)

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-mismatch-delay (correction guidance) (examples)

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group (correction guidance) (examples)

**Description**: An Onset or Offset tag appears in a nested tag group (not a top-level tag group).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group-delay (correction guidance) (examples)

**Description**: A delay appears in a group not in the top level.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group (correction guidance) (examples)

**Description**: An Onset or Offset tag does not appear in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group-delay (correction guidance) (examples)

**Description**: A Delay is not in the tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups (correction guidance) (examples)

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups-delay (correction guidance) (examples)

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-offset-with-no-onset (correction guidance) (examples)

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups (correction guidance) (examples)

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups-delay (correction guidance) (examples)

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed (correction guidance) (examples)

**Description**: A temporal tag appears appears in a tsv with no onset column

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed-delay (correction guidance) (examples)

**Description**: An Inset, Offset, or Onset tag appears in a tsv with no onset column

**Schema**: 8.3.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs (correction guidance) (examples)

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs-delay (correction guidance) (examples)

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## UNITS_INVALID

**File**: `json_test_data/validation_test_data/UNITS_INVALID.json`

### units-invalid-case (correction guidance) (examples)

**Description**: Units are case-sensitive: a unit name, unit symbol, or SI modifier written in a case other than the one listed in the schema is invalid.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 5 fail, 5 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-compound-units (correction guidance) (examples)

**Description**: A compound unit such as m-per-s takes an SI modifier on each of its components; a modifier applied to the whole string, or a misspelled or wrongly cased component, is invalid.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 3 fail, 4 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-for-unit-class (correction guidance) (examples)

**Description**: A tag has a value with units that are invalid or not of the correct unit class for the tag.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-si-units (correction guidance) (examples)

**Description**: A unit modifier is applied to units that are not SI units.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-symbol-plural (correction guidance) (examples)

**Description**: A unit symbol cannot be pluralized, and a unit name accepts only its standard English plural.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 3 fail, 4 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## VALUE_INVALID

**File**: `json_test_data/validation_test_data/VALUE_INVALID.json`

### invalid-character-numeric-class (correction guidance) (examples)

**Description**: An invalid character was used in an 8.3.0 or greater style numeric value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 8 fail, 10 pass
- `sidecar_tests`: 1 fail, 1 pass

### value-invalid-#-substitution (correction guidance) (examples)

**Description**: The value substituted for a placeholder (`#`) is not valid.

**Schema**: 8.3.0 **Category**: validation

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-blank-missing-before-units (correction guidance) (examples)

**Description**: The units are not separated from the value by a single blank.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-incompatible-value-class (correction guidance) (examples)

**Description**: A tag placeholder value is incompatible with the specified value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## WIKI_DELIMITERS_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-format (correction guidance) (examples)

**Description**: A schema unit has an invalid conversion factor due to bad formatting

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 0 pass
