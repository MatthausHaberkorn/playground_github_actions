PROJECT_DIR = .

.PHONY: typehint
typehint:
	mypy --exclude venv --check-untyped-defs $(PROJECT_DIR)

.PHONY: test
test:
	pytest $(PROJECT_DIR) -vv

.PHONY: lint
lint:
	ruff check $(PROJECT_DIR)

.PHONY: format
format:
	ruff format $(PROJECT_DIR)

.PHONY: check
check: lint format test typehint

.PHONY: default
default: test
