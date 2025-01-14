
build:
	@poetry run python3 src/runner_builder.py

run:
	@poetry run python3 src/runner_inference.py

install: pyproject.toml
	@poetry install --no-root

check:
	@poetry run flake8 src/

clean:
	@rm -rf `find . -name __pycache__`
	@rm -rf .ruff_cache

runner: install check run clean
builder: install check build clean

all: install check build run clean

.DEFAULT_GOAL := all
.PHONY: build run install check clean runner builder