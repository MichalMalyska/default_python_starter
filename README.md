# default_python_starter

Template for Python projects that people and coding agents work on together.

## Use

1. Create a repo from this template.
2. Rename `src/default_python_starter` and the `name` in `pyproject.toml`.
3. Run `uv sync`, then `uv run pre-commit install`.
4. Run `make check`.

## What is in it

- uv for Python and dependencies. Python 3.13.
- ruff for lint and format, complexipy for cognitive complexity, pytest for tests.
- Lint rules that ban `unittest` and mocks, and a size limit on test code. See `pyproject.toml` and `scripts/check_test_ratio.py`.
- `AGENTS.md` with the rules for coding agents. `CLAUDE.md` imports it, so Codex and Claude Code read the same file.
- Dependabot: one grouped PR a week for minor and patch updates, a 7-day cooldown on new releases, and auto-merge only for minor and patch updates.
