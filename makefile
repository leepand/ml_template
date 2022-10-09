TEST_PATH=./

.DEFAULT_GOAL := help

.PHONY: help precommit lint tests black ci

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: precommit
precommit: ## Run all pre-commit hooks
	pre-commit run --all-file --show-diff-on-failure

.PHONY: lint
lint: ## Lint your code using pylint
	python -m pylint --version
	find . -type f -name "*.py" | xargs python -m pylint

.PHONY: tests
test: ## Run tests using pytest
	python -m pytest --version
	python -m pytest tests

.PHONY: black
black: ## Format your code using black
	python -m black --version
	python -m black .
## Run ci part
.PHONY: ci
ci: precommit tests
