# HED test suite index

Complete index of 235 test cases in the HED test suite.

## Quick navigation

- [CHARACTER_INVALID](#character-invalid) (8 tests)
- [COMMA_MISSING](#comma-missing) (2 tests)
- [DEFINITION_INVALID](#definition-invalid) (13 tests)
- [DEF_EXPAND_INVALID](#def-expand-invalid) (7 tests)
- [DEF_INVALID](#def-invalid) (3 tests)
- [ELEMENT_DEPRECATED](#element-deprecated) (1 test)
- [PARENTHESES_MISMATCH](#parentheses-mismatch) (3 tests)
- [PLACEHOLDER_INVALID](#placeholder-invalid) (6 tests)
- [SCHEMA_ANNOTATION_INVALID](#schema-annotation-invalid) (1 test)
- [SCHEMA_ATTRIBUTE_INVALID](#schema-attribute-invalid) (2 tests)
- [SCHEMA_ATTRIBUTE_VALUE_INVALID](#schema-attribute-value-invalid) (14 tests)
- [SCHEMA_CHARACTER_INVALID](#schema-character-invalid) (6 tests)
- [SCHEMA_DEPRECATION_ERROR](#schema-deprecation-error) (8 tests)
- [SCHEMA_DUPLICATE_NODE](#schema-duplicate-node) (3 tests)
- [SCHEMA_HEADER_INVALID](#schema-header-invalid) (3 tests)
- [SCHEMA_LIBRARY_INVALID](#schema-library-invalid) (23 tests)
- [SCHEMA_LOAD_FAILED](#schema-load-failed) (41 tests)
- [SCHEMA_MISSING_EXTRA](#schema-missing-extra) (1 test)
- [SCHEMA_RESERVED_INVALID](#schema-reserved-invalid) (2 tests)
- [SCHEMA_SECTION_MISSING](#schema-section-missing) (1 test)
- [SIDECAR_BRACES_INVALID](#sidecar-braces-invalid) (5 tests)
- [SIDECAR_INVALID](#sidecar-invalid) (4 tests)
- [SIDECAR_KEY_MISSING](#sidecar-key-missing) (2 tests)
- [TABULAR_INVALID](#tabular-invalid) (4 tests)
- [TAG_EMPTY](#tag-empty) (3 tests)
- [TAG_EXPRESSION_REPEATED](#tag-expression-repeated) (3 tests)
- [TAG_EXTENDED](#tag-extended) (1 test)
- [TAG_EXTENSION_INVALID](#tag-extension-invalid) (6 tests)
- [TAG_GROUP_ERROR](#tag-group-error) (6 tests)
- [TAG_INVALID](#tag-invalid) (3 tests)
- [TAG_NAMESPACE_PREFIX_INVALID](#tag-namespace-prefix-invalid) (3 tests)
- [TAG_NOT_UNIQUE](#tag-not-unique) (1 test)
- [TAG_REQUIRES_CHILD](#tag-requires-child) (2 tests)
- [TEMPORAL_TAG_ERROR](#temporal-tag-error) (31 tests)
- [UNITS_INVALID](#units-invalid) (6 tests)
- [VALUE_INVALID](#value-invalid) (6 tests)
- [WIKI_DELIMITERS_INVALID](#wiki-delimiters-invalid) (1 test)

## CHARACTER_INVALID

**File**: `json_test_data/validation_test_data/CHARACTER_INVALID.json`

### character-invalid-double-quote (correction guidance) (examples)

**Description**: A HED string contains a double quote, which no HED string may contain whatever the value class. In a tabular file a double quote is an ordinary character, so a HED cell written wholly in quotes ("Red") keeps its quotes and fails.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### character-invalid-non-printing-appears (correction guidance) (examples)

**Description**: The HED string contains a UTF-8 character.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### character-invalid-nonascii-boundary (correction guidance) (examples)

**Description**: The nonascii character set starts at code 160 (U+00A0): the C1 control characters 128-159 are forbidden everywhere, and 160 and above are allowed wherever nonascii is.

**Schema**: 8.5.0 **Category**: validation

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### character-invalid-structural-in-text-value (correction guidance) (examples)

**Description**: From HED 8.5.0 a textClass value may not contain a parenthesis, the number sign, or the tilde, the characters that change the structure of the HED string the value is substituted into.

**Schema**: 8.5.0 **Category**: validation

**Tests**:

- `string_tests`: 4 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### character-invalid-text-value-before-8-5-0 (correction guidance) (examples)

**Description**: Under standard schemas 8.3.0 and 8.4.0 a textClass value uses the text character set: printable or non-ASCII characters except comma, square brackets, and curly braces, with the double quote and tilde excluded from every HED string. Under 8.0.0 to 8.2.0 the same applies without the non-ASCII characters, which those schemas exclude from every HED string.

**Schema**: 8.2.0 **Category**: validation

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
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

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### comma-missing-tag-groups (correction guidance) (examples)

**Description**: Two tag groups are not separated by commas: (A, B)(C, D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 1 fail, 1 pass
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

### definition-invalid-content-has-delay-or-duration-in-8-1-0 (correction guidance) (examples)

**Description**: Delay and Duration may not appear in a definition's contents (reason d). The rule holds in every standard schema version; 8.1.0 is not special, and this case pins it there because the 8.1.0 schema does not mark Delay and Duration reserved.

**Schema**: 8.1.0 **Category**: content

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass

### definition-invalid-content-has-top-level-tag (correction guidance) (examples)

**Description**: A definition's contents contain, at any level, a structural reserved tag (Definition, Def, Def-expand, Onset, Offset, Inset, Delay, Duration, Event-context; reason d) or a tag with the required or unique attribute (reason j).

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 7 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-duplicate-definitions-differ (correction guidance) (examples)

**Description**: A definition name may be defined more than once only when every definition of it is identical; the same name with different contents is an error.

**Schema**: 8.4.0 **Category**: uniqueness

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

**Description**: Definitions with the same name have different contents.

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

### definition-invalid-second-part-not-placeholder (correction guidance) (examples)

**Description**: The value of a Definition tag has a part after the name other than a single # (reason l): Definition/NewDef/3 and Definition/NewDef/Extra fail. Definition/NewDef/#/# fails too, as reason f (three # in the definition) or l.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 3 fail, 1 pass
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

### def-expand-tags-in-any-order (correction guidance) (examples)

**Description**: The tags and groups within a Def-expand may appear in any order; only their content and nesting must match the definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 2 fail, 2 pass
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

### parentheses-mismatch-in-value-column (correction guidance) (examples)

**Description**: A value in a sidecar-annotated value column contains an unmatched parenthesis, so the HED string obtained by substituting the value for the # is unbalanced.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `combo_tests`: 1 fail, 1 pass

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

### placeholder-invalid-after-extension (correction guidance) (examples)

**Description**: A placeholder (`#`) follows a user extension term (Item/Blech/#) or stands in for one (Item/#). The # cannot be an extension, so this is PLACEHOLDER_INVALID in every context, events file or sidecar.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 3 fail, 2 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-in-value-column (correction guidance) (examples)

**Description**: A value in a sidecar-annotated value column contains a # character, so the HED string obtained by substituting the value for the # of the annotation still holds a placeholder.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-#-misplaced (correction guidance) (examples)

**Description**: A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.

**Schema**: 8.4.0 **Category**: schema

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
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

## SCHEMA_ANNOTATION_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ANNOTATION_INVALID.json`

### schema-annotation-invalid (warning) (correction guidance) (examples)

**Description**: An annotation attribute value does not follow the prefix:id value grammar or cites a source that has no row in the Sources section.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 8 fail, 7 pass

## SCHEMA_ATTRIBUTE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_INVALID.json`

### attribute-invalid-any-units-not-empty (correction guidance) (examples)

**Description**: The pseudo unit class anyUnits lists a unit or has defaultUnits.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

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

### attribute-invalid-multiple-unit-classes (correction guidance) (examples)

**Description**: A placeholder (#) lists more than one unit class in its unitClass attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-unit-class (correction guidance) (examples)

**Description**: A schema unit class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-unit-class-without-numeric-value-class (correction guidance) (examples)

**Description**: A placeholder (#) has a unitClass attribute but its valueClass is not numericClass, or it has no valueClass.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

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

### schema-deprecated-attribute-used-by-element

**Description**: A schema deprecation issue: an element uses a deprecated schema attribute

**Schema**: any

**Tests**:

- `schema_tests`: 5 fail, 5 pass

### schema-deprecated-default-unit

**Description**: A schema deprecation issue, deprecated default units

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

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

### schema-deprecated-property-used-by-attribute

**Description**: A schema deprecation issue: a schema attribute uses a deprecated property

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

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

### attribute-duplicate-node-derived-in-two-classes (correction guidance) (examples)

**Description**: A unit string is derived by two unit classes (SI modifier applied to a unit of each) and listed by neither, so it would be ambiguous on a placeholder that accepts any unit.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

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

### library-invalid-duplicate-unit-class (correction guidance) (examples)

**Description**: An unmerged partnered library schema redeclares a unit class of its standard schema partner with a description or attributes instead of naming it only to add units.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

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

### library-invalid-reserved-in-merged-library-node (correction guidance) (examples)

**Description**: In a merged partnered library schema, a library node (one with inLibrary) cannot carry the reserved attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-reserved-in-unmerged (correction guidance) (examples)

**Description**: The reserved attribute cannot be used in an unmerged partnered library schema.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-reserved-in-unpartnered (correction guidance) (examples)

**Description**: An unpartnered library schema cannot use the reserved attribute on its own tags.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-reserved-name (correction guidance) (examples)

**Description**: A library schema cannot define a tag whose name is a reserved tag of a standard schema, such as Onset.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

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

### library-invalid-rooted-under-reserved (correction guidance) (examples)

**Description**: A partnered library schema cannot use rooted to place a node under a reserved tag such as Onset.

**Schema**: any **Category**: schema_development

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

**Description**: The same schema (same name and version) listed twice in one merge group is an error; a schema name may appear only once in a merge group.

**Schema**: testconflict_2.0.0, testconflict_2.0.0 **Category**: schema

**Tests**:

- `string_tests`: 2 fail, 0 pass

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

## SCHEMA_RESERVED_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_RESERVED_INVALID.json`

### schema-reserved-invalid-child-node (correction guidance) (examples)

**Description**: A reserved tag in a standard schema cannot have a child node other than #.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-reserved-invalid-missing-or-unmarked (correction guidance) (examples)

**Description**: A standard schema must define every reserved tag with the attributes the reserved-tag rules rely on.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 4 fail, 1 pass

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

### sidecar-invalid-key-whitespace (correction guidance) (examples)

**Description**: A top-level sidecar key begins or ends with whitespace (reason d). A trailing blank, a leading blank, and a trailing tab fail, on categorical and value entries, on a padded key beside its unpadded twin, and on a padded key whose entry has no HED. A sidecar key trial with a padded entry for a header column trial fails. Unpadded keys pass, including a key with an internal blank and a key that ends with a no-break space (U+00A0), which is not whitespace for this rule.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 5 fail, 5 pass
- `combo_tests`: 1 fail, 1 pass

### sidecar-invalid-na-annotated (correction guidance) (examples)

**Description**: An annotation entry is provided for `n/a`.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### sidecar-invalid-value-key-whitespace (correction guidance) (examples)

**Description**: In a categorical entry, a column value listed as a key under HED begins or ends with whitespace (reason e). A trailing blank, a leading blank, and a trailing tab on a key under HED fail, and a combo whose sidecar has the padded key go fails even though the table holds go. Unpadded keys pass, including a key with an internal blank, a key ending with a no-break space (U+00A0, not whitespace for the rule), and a padded key in a BIDS Levels dictionary of the same entry, which is not checked.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 3 fail, 4 pass
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

## TABULAR_INVALID

**File**: `json_test_data/validation_test_data/TABULAR_INVALID.json`

### tabular-invalid-blank-column-name (correction guidance) (examples)

**Description**: A column name in the first line of a tabular file is blank, the empty string (reason c). A first line that ends with a tab has a blank last name, a first line that is only a tab has two blank names, a blank name between two others fails, and two blank names are reported under (c) for each blank name, not as a repeated name under (a). A header naming trial for a sidecar entry trial fails when the header also has a blank column. The same tables without the blank column pass.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 3 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### tabular-invalid-column-name-whitespace (correction guidance) (examples)

**Description**: A column name in the first line of a tabular file begins or ends with whitespace (reason b). A trailing or leading blank fails, on the HED column or on any other column, a padded name that is also repeated is reported under (b), trial beside a padded trial is one padded name rather than a repeat, and a name made only of a blank is padded and fails under (b), not as a blank name (c). A header naming trial for a sidecar entry trial fails when the header cell is padded. The same tables with unpadded names pass, including a name with an internal blank and a name that ends with a no-break space (U+00A0), which is not whitespace for this rule.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 6 fail, 4 pass
- `combo_tests`: 1 fail, 1 pass

### tabular-invalid-duplicate-column-name (correction guidance) (examples)

**Description**: A column name appears more than once in the first line (the column names) of a tabular file (reason a). The error does not depend on whether the repeated column is annotated: a repeated HED column, a repeated column with no annotation, a name repeated three times, and a repeated column that a sidecar annotates all fail. Distinct names pass, including a name that is a prefix of another (trial and trial_type). Names are compared exactly as written: a double quote is an ordinary character, so trial and "trial" are two names, and 1 and 1.0 are two names, not one number.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 3 fail, 4 pass
- `combo_tests`: 1 fail, 1 pass

### tabular-invalid-value-whitespace (correction guidance) (examples)

**Description**: A value in a column with categorical or value HED annotations begins or ends with whitespace (reason d). In a categorical column, go with a trailing or leading blank, a value made only of a blank, and n/a with a trailing blank fail; in a value column, 30 with a trailing or leading blank fails. The same tables pass with go, 30, n/a, and an empty cell, and also with a HED column cell that has blanks around its tag, a categorical value ending with a no-break space (U+00A0, not whitespace for the rule; it only lacks an annotation, a warning), and a padded value in a column with no HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `combo_tests`: 6 fail, 4 pass

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

- `string_tests`: 8 fail, 1 pass
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

### tag-extension-invalid-no-letter (correction guidance) (examples)

**Description**: A tag extension term contains no letter (Item/Blech/3, Item/1-2, Item/\_). An extension term must contain at least one letter: A-Z or a-z, or any Unicode letter in schema versions whose nameClass allows non-ASCII characters (8.3.0 and later), so a non-ASCII term with no letter (a degree sign, an Arabic-Indic digit) also fails.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 7 fail, 5 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-extension-invalid-no-letter-8-2-0 (correction guidance) (examples)

**Description**: The rule that an extension term must contain a letter applies to every standard schema version >= 8.0.0, here 8.2.0: Item/Blech/3 and Item/1-2 fail, Item/Blech/1red passes.

**Schema**: 8.2.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 1 pass

### tag-extension-invalid-reserved-tag (correction guidance) (examples)

**Description**: A structural reserved tag is extended with a term (Onset/Blah, Event-context/Blah). Reserved tags must not be extended although they inherit extensionAllowed from Property. A # after a reserved tag (Onset/#) is tested in tag-extension-invalid-reserved-tag-placeholder, since it may be reported under either of two codes.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-extension-invalid-reserved-tag-placeholder (correction guidance) (examples)

**Description**: A # follows a reserved tag that takes no value. It is an error in every context: a HED string ((Event-context/#, (Red)), since string tests use no temporal tag), an events file, a sidecar value column, and a combo ((Onset/#, Def/MyColor)). A validator may report it as TAG_EXTENSION_INVALID (the # extends a reserved tag) or as PLACEHOLDER_INVALID (the # has no placeholder child to stand for, or is not allowed there at all), depending on which check finds it first.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_GROUP_ERROR

**File**: `json_test_data/validation_test_data/TAG_GROUP_ERROR.json`

### multiple-top-level-tags-in-same-group (correction guidance) (examples)

**Description**: Multiple tags with the topLevelTagGroup attribute appear in the same top-level tag group. (Delay and Duration are allowed to be in the same topLevelTagGroup).

**Schema**: 8.4.0 **Category**: cardinality

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 3 fail, 2 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-deferred-in-splice (correction guidance) (examples)

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 3 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 3 pass

### tag-group-error-event-context-braces (correction guidance) (examples)

**Description**: An Event-context group contains a sidecar column reference (\{column}). Column references may not appear in an Event-context group; they may appear beside it.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-event-context-contents (correction guidance) (examples)

**Description**: An `Event-context` group contains, besides the `Event-context` tag, only tag groups, one per ongoing event process.

**Schema**: 8.4.0 **Category**: cardinality

**Tests**:

- `string_tests`: 2 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-missing (correction guidance) (examples)

**Description**: A tag has tagGroup or topLevelTagGroup attribute, but is not enclosed in parentheses.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
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

### tag-requires-child-reserved-value-in-8-2-0 (correction guidance) (examples)

**Description**: Under standard schema 8.2.0, Delay and Duration lack the requireChild attribute but still require a value, because requireValue is true for them in reserved_tags.json (reason b): (Delay, (Red)) and (Duration, (Red)) fail. The same strings fail under 8.0.0 and 8.1.0 for the same reason (pinned for 8.1.0 in temporal-tag-error-rules-apply-in-8-1-0).

**Schema**: 8.2.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass

## TEMPORAL_TAG_ERROR

**File**: `json_test_data/validation_test_data/TEMPORAL_TAG_ERROR.json`

### na-in-onset column (correction guidance) (examples)

**Description**: n/a is in the onset column.

**Schema**: 8.4.0 **Category**: data_format

**Tests**:

- `combo_tests`: 2 fail, 2 pass

### temporal-tag-error-delay-missing-group (correction guidance) (examples)

**Description**: A Delay that is the only reserved tag of its group must have exactly one inner group, so (Delay/3 s) fails. Beside Onset, Offset, Inset, or Duration, Delay is secondary and that tag's row gives the group rules: (Onset, Def/MyColor, Delay/3 s) passes with no inner group, while (Delay/3 s, Duration/2 s) fails because Duration needs one.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-delay-not-convertible (correction guidance) (examples)

**Description**: In a timeline table (a table with an onset column), a Delay tag has a value that cannot be converted to the default units of its unit class because the unit has no conversionFactor (month and year in HED 8.4.0), so the delayed onset cannot be placed on the timeline. Delay is never allowed in a descriptor table (cause k), so it can never carry a non-convertible unit. Appendix B TEMPORAL_TAG_ERROR cause n. Implemented in hed-python PR #1399; hed-javascript issue #860.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 2 fail, 2 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-delay-with-anchored-marker (correction guidance) (examples)

**Description**: A `Delay` tag may appear in an `Onset`, `Offset`, or `Inset` group, delaying that marker; the marker tag must stay at the top level of the group, not inside the delayed inner group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 2 pass
- `combo_tests`: 1 fail, 1 pass

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

- `string_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 0 fail, 1 pass

### temporal-tag-error-duration-not-convertible (correction guidance) (examples)

**Description**: In a timeline table (a table with an onset column), a Duration tag has a value that cannot be converted to the default units of its unit class because the unit has no conversionFactor (month and year in HED 8.4.0), so the end time cannot be placed on the timeline. The same Duration is valid in a descriptor table such as participants.tsv, where there is no timeline to map it onto. Appendix B TEMPORAL_TAG_ERROR cause n.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 3 fail, 2 pass
- `combo_tests`: 1 fail, 2 pass

### temporal-tag-error-duration-with-top-level-def (correction guidance) (examples)

**Description**: A Duration group may not have a Def tag or a Def-expand group at its top level (rule 2: Duration has no anchor); one may appear inside the inner group. A Def-expand group stands where its Def tag would and is never counted as the inner group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 4 fail, 3 pass
- `event_tests`: 1 fail, 1 pass

### temporal-tag-error-extra tags (correction guidance) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-extra tags-delay (correction guidance) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras (correction guidance) (examples)

**Description**: An Inset group has tags, other than its anchor and an optional Delay, that are not in a tag group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras-delay (correction guidance) (examples)

**Description**: An Inset group has tags, other than its anchor and an optional Delay, that are not in a tag group.

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

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group-delay (correction guidance) (examples)

**Description**: A delay appears in a group not in the top level.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-no-conversion-factor-in-8-0-0 (correction guidance) (examples)

**Description**: Standard schema 8.0.0 gives no time unit a conversionFactor. In a timeline table a Delay or Duration value in the default unit, given or omitted and written as s, second, or seconds, is taken as is, so (Duration/3 s, (Red)), (Duration/3, (Red)) and (Duration/3 second, (Red)) pass; a modified form or any other unit cannot be placed on the timeline, so (Duration/300 ms, (Red)) and (Duration/2 minute, (Red)) fail (cause n). The same Duration passes in a descriptor table.

**Schema**: 8.0.0 **Category**: temporal

**Tests**:

- `event_tests`: 2 fail, 2 pass

### temporal-tag-error-not-tag-group (correction guidance) (examples)

**Description**: An Onset or Offset tag does not appear in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group-delay (correction guidance) (examples)

**Description**: A Delay is not in the tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 5 fail, 2 pass
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

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups-delay (correction guidance) (examples)

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-rules-apply-in-8-1-0 (correction guidance) (examples)

**Description**: The reserved-tag rules for Delay and Duration apply in every standard schema version, including 8.1.0, whose schema gives these tags none of the reserved, topLevelTagGroup, or requireChild attributes: a nested or ungrouped Delay or Duration, one without a value, and a Delay in a descriptor table all fail; (Delay/2 s, (Blue)) and (Onset, Def/MyColor, Delay/3 s) in a timeline table pass.

**Schema**: 8.1.0 **Category**: temporal

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 4 fail, 1 pass

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

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 2 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs-delay (correction guidance) (examples)

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 2 pass
- `combo_tests`: 1 fail, 1 pass

## UNITS_INVALID

**File**: `json_test_data/validation_test_data/UNITS_INVALID.json`

### units-invalid-any-units (correction guidance) (examples)

**Description**: A placeholder with unitClass=anyUnits (Quantity in HED 8.5.0) accepts a value with or without a unit; when a unit is given it must be a valid unit of some unit class of the schema.

**Schema**: 8.5.0 **Category**: validation

**Tests**:

- `string_tests`: 4 fail, 7 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass

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

### bad-value-in-curly-column (correction guidance) (examples)

**Description**: A column referenced in curly braces has an invalid value in a row whose selected template does not substitute it.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `combo_tests`: 1 fail, 1 pass

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

### value-invalid-date-time-format (correction guidance) (examples)

**Description**: A dateTimeClass value does not have the BIDS Datetime format (RFC 3339 with an optional offset), or its date does not exist in the Gregorian calendar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 11 fail, 7 pass
- `sidecar_tests`: 4 fail, 3 pass
- `event_tests`: 4 fail, 3 pass
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
