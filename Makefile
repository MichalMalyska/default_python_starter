.PHONY: check lint test

# One command for people and agents. Exit code 0 means done.
check: lint test

lint:
	uv run pre-commit run --all-files

test:
	uv run pytest
