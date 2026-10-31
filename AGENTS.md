# AGENTS.md

Instructions for coding agents (Codex, Claude Code and others) in this repo.

## Commands

- Install: `uv sync`
- Check everything: `make check`. Run it before you say a task is done. Exit code 0 means it passed.
- Tests only: `uv run pytest`
- Lint and format only: `make lint`

Use `uv run` and `uv add`. Do not use `pip install` or edit `uv.lock` by hand.

## Layout

- `src/default_python_starter/`: package code.
- `tests/`: pytest tests.
- `scripts/`: repo tooling.

## Code rules

- Keep functions small. `make check` fails at cyclomatic complexity 10 (ruff) or cognitive complexity 10 (complexipy).
- Split a function that hits a limit. Do not add `noqa` or raise the limit to pass the check.
- Add a dependency or abstraction only when the current task needs it.

## Test rules

- Write plain pytest functions. `unittest` is banned by a lint rule.
- Do not mock. `unittest.mock`, `mock` and `pytest-mock` are banned by a lint rule. Use real objects, a small fake class, `tmp_path`, or `monkeypatch` for environment variables and IO boundaries.
- Test behavior through the public API. Do not test private functions.
- Write one test per behavior. Use `pytest.mark.parametrize` for input variants instead of copied tests.
- Do not test trivial code such as constants, getters or dataclass fields.
- Test code may not grow past 1.5 times the source code (`scripts/check_test_ratio.py`). When it does, delete duplicate tests.
