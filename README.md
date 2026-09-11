# HED test suite

[![CI](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml/badge.svg)](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml) [![Docs](https://img.shields.io/badge/docs-hed--tests-blue.svg)](https://www.hedtags.org/hed-tests) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Official JSON test suite for HED (Hierarchical Event Descriptors) validation**

This repository provides comprehensive, machine-readable test cases for validating HED validator implementations across all platforms (Python, JavaScript, and future implementations). Tests ensure consistent validation behavior and serve as AI-readable specifications for HED validation rules.

## Quick start

```bash
# Linux/macOS
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

```powershell
# Windows PowerShell
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -e ".[dev,docs]"
```

See the **[user guide](https://www.hedtags.org/hed-tests)** for complete documentation, including:

- Test file format and test types
- Integrating the test suite into your validator
- Error code categories and coverage
- Contributing new tests

## Repository structure

```
hed-tests/
|-- json_test_data/
|   |-- validation_test_data/    # One JSON file per validation error code
|   |-- schema_test_data/        # One JSON file per schema error code
|   |-- validation_tests.json    # Consolidated validation tests (generated)
|   |-- schema_tests.json        # Consolidated schema tests (generated)
|   `-- *_dict.json              # Error code <-> test name lookups (generated)
|-- src/scripts/                 # Maintenance scripts (see below)
|-- src/schemas/                 # JSON schema the test files must conform to
|-- tests/                       # Unit tests for the maintenance scripts
`-- docs/                        # Documentation source
```

See [json_test_data/README.md](json_test_data/README.md) for what each JSON file represents and how validators consume them.

## Maintenance scripts

Six scripts in `src/scripts/` maintain the test suite. All run from the repository root with the project's virtual environment active; `regenerate.py` drives the other generators and is what the pre-commit hook and CI run.

### validate_test_structure.py

Checks that test files conform to the official JSON schema in `src/schemas/test_schema.json`: JSON syntax, required fields, field types, and test structure. After editing any test file under `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/`, run it with no arguments to check everything, or narrow it to just the directory or file you edited:

```bash
# Validate all test directories
python src/scripts/validate_test_structure.py

# Validate one directory
python src/scripts/validate_test_structure.py json_test_data/schema_test_data

# Validate a single file
python src/scripts/validate_test_structure.py --file json_test_data/validation_test_data/TAG_INVALID.json
```

Options: `--schema <path>` to validate against a different schema, `--verbose` for per-file detail.

### consolidate_tests.py

Combines the individual per-error-code files into the six generated files at the top of `json_test_data/` (the two consolidated test files plus four lookup dictionaries) that validators actually consume:

```bash
# Regenerate all six consolidated files
python src/scripts/consolidate_tests.py

# Preview what would be regenerated without writing anything
python src/scripts/consolidate_tests.py --dry-run
```

**Run this after every test edit and commit the regenerated files together with the edit.** The pre-commit hook and the CI step `python src/scripts/regenerate.py --check` both fail when the committed copies are stale, so a forgotten regeneration is caught before it reaches validators.

### check_coverage.py

Reports which error codes have tests, how many test cases each has, which test types (string/sidecar/event/combo) are covered, and whether the correction guidance fields are complete. Use it to find coverage gaps before adding tests:

```bash
# Print the coverage report to the console
python src/scripts/check_coverage.py

# Write the coverage report to a markdown file instead
python src/scripts/check_coverage.py --markdown report.md
```

For current test statistics, run this script rather than trusting any count written in documentation.

### generate_test_index.py

Regenerates `docs/test_index.md`, the searchable index of every test case organized by error code:

```bash
# Regenerate docs/test_index.md (the default output)
python src/scripts/generate_test_index.py

# Write the index to a different file
python src/scripts/generate_test_index.py --output some_other_file.md

# Produce the index as JSON (give it its own output file so the
# markdown index is not overwritten with JSON)
python src/scripts/generate_test_index.py --format json --output test_index.json
```

`docs/test_index.md` is generated - edit tests, not the index.

### convert_test_schemas.py

Builds the test-only schema libraries under `json_test_data/test_schemas/` from their hand-edited `.mediawiki` sources, writes the merged, load-ready XML that runners resolve version strings against, and maintains `manifest.json`. With `--refresh --hed-schemas <path-to-hed-schemas>` it first re-copies the vendored standard schema snapshots (the 8.5.0 prerelease and 8.4.0) from a local hed-schemas clone. Details, including what to check before a refresh, are in [json_test_data/test_schemas/README.md](json_test_data/test_schemas/README.md).

### regenerate.py

Runs, in order, `convert_test_schemas.py`, `consolidate_tests.py`, `generate_test_index.py`, `check_coverage.py`, and then mdformat on the markdown they write. `regenerate.py --check` does the same and then fails if any file the generators write (the merged and unmerged test-schema XML, `manifest.json`, the consolidated JSON and dictionaries, `docs/test_index.md`, `docs/test_coverage.md`) differs from the git index; the pre-commit hook and CI both use that mode, so a stale generated file cannot be committed unnoticed.

### Typical maintenance workflow

1. Edit or add a test file in `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/` (one error code per file).
2. Validate: `python src/scripts/validate_test_structure.py` (or narrow it to the directory you edited).
3. Regenerate every derived file: `python src/scripts/regenerate.py` (runs the consolidation, index, coverage, and schema-conversion scripts, then mdformat).
4. Check the result: `python -m unittest discover tests`.
5. Commit the edited file **and** the regenerated files together.

A pre-commit hook enforces step 3. Install it once per clone with `pre-commit install` (after `pip install -e ".[dev]"`); it regenerates the derived files, blocks the commit if any of them differs from what is staged, and runs the structure validators, the unit tests, ruff, and the markdown format check. CI runs the same `regenerate.py --check`, so a stale generated file fails the build even without the hook. The hooks call `python` from the PATH, so commit with the virtual environment active.

## Maintaining and updating the tests

This section is the checklist for changing the suite. The user guide describes the file format in full; this is what to do, in order.

### Adding or changing a test case

1. Every error code has one source file: `json_test_data/validation_test_data/<CODE>.json` for annotation validation, `json_test_data/schema_test_data/<CODE>[_<VARIANT>].json` for schema validation. Add a case to the file for its error code; create the file only for a new error code, and add the code to the specification's Appendix B first.
2. A case is one JSON object with a unique `name` (lower-case, hyphenated, starting with the error code's theme, for example `units-invalid-compound-units`), the `error_code`, a `description`, the correction guidance fields, and `tests`. Copy an existing case in the same file as the template so the required fields are present.
3. Validation cases name a released or vendored schema in `schema` (`"8.4.0"`, `"8.5.0"`, or a list such as `["8.5.0", "sc:testconflict_2.0.0"]`) and give `string_tests`, `sidecar_tests`, `event_tests`, and `combo_tests`, each with `fails` and `passes`. Every `fails` entry must produce the file's error code; every `passes` entry must produce no error.
4. Schema cases give `schema_tests` with `fails` and `passes`, each entry an inline schema as a list of MediaWiki lines. Use an unmerged library partnered with a vendored standard (`withStandard="8.4.0"` or `"8.5.0"`) when the case needs the standard vocabulary, or a standalone `HED version="1.0.0"` schema that declares its own attributes when it must not. In MediaWiki a repeated attribute is written by repeating it, `unitClass=a, unitClass=b`, not `unitClass=a,b`.
5. A case that needs a schema feature not yet in the vendored snapshots (a new tag or unit class in the 8.5.0 prerelease) waits for a snapshot refresh (below); until then, validators skip it by name.
6. Run the workflow above: validate, `regenerate.py`, unit tests, commit source and generated files together.

### Changing a test schema library

The libraries under `json_test_data/test_schemas/<library>/hedwiki/` are the source of truth. Edit the `.mediawiki`, run `python src/scripts/convert_test_schemas.py` (or `regenerate.py`, which includes it), and commit the regenerated XML and `manifest.json`. These libraries are test fixtures and are never published to the HED schema repositories.

### Refreshing the vendored standard schemas

When the 8.5.0 prerelease changes in hed-schemas (or 8.5.0 is released), after the change is on hed-schemas `main` and its XML has been regenerated there:

```bash
python src/scripts/convert_test_schemas.py --refresh --hed-schemas <path-to-hed-schemas>
python src/scripts/regenerate.py
```

This re-copies the vendored XML from the local hed-schemas clone, records the source commit in `manifest.json`, and rebuilds every merged library XML against the new partner. When 8.5.0 is released, change its entry in `VENDORED_STANDARDS` (in `convert_test_schemas.py`) to `standard_schema/hedxml/HED8.5.0.xml` with `released: True` before refreshing. See [json_test_data/test_schemas/README.md](json_test_data/test_schemas/README.md) for the details and cautions.

### After a change merges

- hed-python pins this repository as the git submodule `spec_tests/hed-tests` and runs every case in `spec_tests/test_errors.py`; it bumps the pin once its own implementation passes the new cases, and lists any case it cannot yet pass in that file's `skip_tests` with the reason.
- hed-javascript pins a commit of this repository; do not expect it to pass new cases until its issue for the rule is closed.
- A new rule therefore lands in this order: specification text, test case here, validator implementation, pin bump. Record which validators have caught up in the pull request description.

## Related repositories

- **[hed-python](https://github.com/hed-standard/hed-python)**: Python validator implementation
- **[hed-javascript](https://github.com/hed-standard/hed-javascript)**: JavaScript validator implementation
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal HED specification
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: HED vocabulary schemas

## Versioning

Semantic versioning: major = breaking format change, minor = new tests/error codes, patch = bug fixes. Current version: **1.0.0**

## License

MIT License — see [LICENSE](LICENSE) for details.

## Citation

If you use HED in your research, please cite:

```
Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2022).
Building FAIR functionality: Annotating events in time series data using
Hierarchical Event Descriptors (HED). Neuroinformatics, 1-17.
```

## Support

- **Documentation**: https://www.hedtags.org/hed-tests
- **Issues**: https://github.com/hed-standard/hed-tests/issues
- **Discussions**: https://github.com/orgs/hed-standard/discussions
- **Email**: hed.maintainers@gmail.com
