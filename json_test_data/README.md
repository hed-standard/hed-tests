# json_test_data

The test data for the HED validation test suite. Two kinds of content live here: **source** test files, edited by hand, and **generated** files produced from them by `src/scripts/consolidate_tests.py`. Never edit a generated file directly - edit the source file and regenerate.

## Source: the per-error-code test files

- `validation_test_data/` - one JSON file per HED validation error code (e.g. `TAG_INVALID.json`). Each file holds an array of test case objects for that error code: failing and passing examples as raw HED strings, BIDS sidecars, event tables, and sidecar+event combinations, plus the correction guidance fields (`explanation`, `common_causes`, `correction_strategy`, `correction_examples`).
- `schema_test_data/` - the same structure, one file per schema-level error code (e.g. `SCHEMA_ATTRIBUTE_INVALID.json`), for errors found when loading and checking HED schemas themselves.

Every test file must conform to the JSON schema in `src/schemas/test_schema.json`; check with `python src/scripts/validate_test_structure.py` (no arguments validates both test directories).

## Generated: the consolidated files validators consume

`consolidate_tests.py` combines the per-error-code files into six files at this directory's root. Validator implementations (hed-python, hed-javascript, and others) read these, not the individual files:

- `validation_tests.json` - every validation test case in one array. The primary input for a validator's conformance run.
- `schema_tests.json` - every schema test case in one array.
- `validation_code_dict.json` - maps each validation error code to the names of its test cases. Used to select or report tests by error code.
- `validation_testname_dict.json` - the reverse map: test case name to its error code. Used to look up what a named test is checking.
- `schema_code_dict.json` - error code to test names, for the schema tests.
- `schema_testname_dict.json` - test name to error code, for the schema tests.

## Keeping source and generated files in sync

After editing anything in `validation_test_data/` or `schema_test_data/`, run:

```bash
python src/scripts/consolidate_tests.py
```

and commit the regenerated files together with your edit. Both the pre-commit hook and CI run `python src/scripts/regenerate.py --check`, which fails when a committed generated file is stale, so a forgotten regeneration is caught before validators consume outdated tests.

The full test format specification and maintenance workflow are in the [user guide](https://www.hedtags.org/hed-tests).
