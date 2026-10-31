# default_python_starter

Template for Python projects.

## Use

1. Create a repo from this template.
2. Rename `src/default_python_starter` and the `name` in `pyproject.toml`.
3. Run `uv sync`, then `uv run pre-commit install`.
4. Run `make check`.

## What is in it

- uv for Python and dependencies. Python 3.13.
- ruff for lint and format, complexipy for cognitive complexity, pytest for tests.
- Strict ruff rules, including a ban on `unittest` so tests use only pytest. Use pytest-mock's `mocker` fixture for mocks.
- A size limit on test code: `scripts/check_test_ratio.py`.
- `make check` runs every check. CI runs the same command.
- Dependabot: one grouped PR a week for minor and patch updates, a 7-day cooldown on new releases, and auto-merge only for minor and patch updates.
