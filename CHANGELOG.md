# Unreleased

- Renamed schema-deprecated-deprecated-attribute to schema-deprecated-attribute-used-by-element and schema-deprecated-deprecated-property to schema-deprecated-property-used-by-attribute, and reworded their descriptions to say what uses what
- schema-deprecated-property-used-by-attribute (was schema-deprecated-deprecated-property): both fixtures are now an unpartnered score library that declares deprecatedFrom and its two properties; as an unmerged partnered library they declared a property, which SCHEMA_LIBRARY_INVALID (j) forbids now that hed-python implements reasons j-l
- Added CHARACTER_INVALID cases character-invalid-double-quote (no HED string may contain a double quote, under every schema version), character-invalid-nonascii-boundary (U+009F is a C1 control and invalid everywhere; U+00A0 is the first nonascii character and valid in a nameClass value under 8.5.0, whose declaration lists nonascii) and character-invalid-text-value-before-8-5-0 (under 8.2.0 a textClass value uses the text set, so underscores and apostrophes are valid and square brackets, curly braces and double quotes are not)
- Refreshed the vendored 8.5.0 prerelease snapshot from hed-schemas 518b34d (nameClass declares nonascii; dateTimeClass declares period, plus and Z; Report, No-go-signal, Task-trial-role and Catch-trial) and rebuilt the partnered test libraries
- value-invalid-date-time-format now also fails dates that do not exist in the Gregorian calendar (2026-02-31, 2026-04-31, 2027-02-29) and passes the leap day 2028-02-29; the explanation says validators check the calendar after the format, as the BIDS text requires
- Added SCHEMA_ANNOTATION_INVALID schema test cases: eight failing annotation values (undefined prefix, unknown external property, bare external term, two dc:source citations naming no Sources row, and three skos:exactMatch/skos:closeMatch values whose term is not in prefix notation) and seven passing ones; every case is a library partnered with 8.5.0, since the rule is gated on a standard version of 8.5.0 or later
- Fixed the combo passes case of na-in-onset column (TEMPORAL_TAG_ERROR): its first data row had three cells under a four-column header; added the missing duration value 0
- Added UNITS_INVALID cases units-invalid-case (all unit strings are case-sensitive), units-invalid-symbol-plural (symbols take no plural), and units-invalid-compound-units (SI modifiers apply per component, so cm-per-us is valid and kmm-per-s is not)
- Added the testaux test library (auxiliary items only, partnered with 8.5.0) and testclash probe versions 13.0.0-19.0.0
- Added SCHEMA_LOAD_FAILED cases for auxiliary-section merging (unit classes, units, unit modifiers, value classes, schema attributes and their properties) and two passing namespaced combinations
- Added SCHEMA_LIBRARY_INVALID cases for duplicate value class, schema attribute, and unit modifier, rooted in an unpartnered library, and an unpartnered library with its own Properties section
- Renamed schema test cases library-invalid-rooted-in-library-present to library-invalid-inlibrary-in-unmerged and library-invalid-rooted-in-duplicate-other to library-invalid-duplicate-unit
- Set warning to false on all schema test cases except SCHEMA_MISSING_EXTRA and added specification_reference to every SCHEMA_LIBRARY_INVALID case
- Replaced the v2: namespace prefix with alt: in SCHEMA_LOAD_FAILED cases and correction examples (namespace names must be alphabetic)
- Re-described same-library-two-incompatible-versions: the pair fails on the version rule alone, never on element comparison (spec 7.3.6.5)
- Added SCHEMA_LIBRARY_INVALID cases for the remaining reasons: non-empty Properties in an unmerged partnered library (j), merged-form rooted node not under its anchor (e), merged-form Properties mismatch with the partner (k), and reserved in an unmerged partnered library (l)
- Fixture fixes: partnered fixtures and the testaux/testclash schemas now use the real 8.4.0/8.5.0 property name boolRange instead of boolProperty, and the merged-form fixtures define the rooted and inLibrary attributes they use (unpartnered self-contained fixtures keep their own boolProperty declarations)
- Refreshed the vendored 8.5.0 prerelease snapshot (test_schemas/hedxml/HED8.5.0.xml) from hed-schemas and regenerated the 24 merged 8.5.0-partnered test libraries; the old snapshot still listed uV beside V, which 8.5.0 forbids

# Initial repository creation January 23, 2026

- Transferred JSON tests from hed-specification
- Added separated validation and schema tests into different directories
- Added lookup JSON dictionaries for test names vs error codes
- Added lookup JSON dictionaries for error codes vs test names
- Restructured scripts and added tests
