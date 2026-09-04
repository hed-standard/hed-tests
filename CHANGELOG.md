# Unreleased

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

# Initial repository creation January 23, 2026

- Transferred JSON tests from hed-specification
- Added separated validation and schema tests into different directories
- Added lookup JSON dictionaries for test names vs error codes
- Added lookup JSON dictionaries for error codes vs test names
- Restructured scripts and added tests
