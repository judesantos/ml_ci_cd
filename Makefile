#.DEFAULT_GOAL := runner

run:
	@poetry run python3 src/runner.py

install: pyproject.toml
	@poetry install --no-root

check:
	@poetry run ruff check src/

clean:
	@rm -rf `find . -name __pycache__`
	@rm -rf .ruff_cache

runner: install check run clean

.PHONY: run install check clean runner