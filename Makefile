## Lint your code using pylint
.PHONY: lint
lint:
	python3 -m pylint --version
	python3 -m pylint src
.PHONY: test
test:
	python3 -m pytest --version
	python3 -m pytest tests
.PHONY: black
black:
	python3 -m black --version
	python3 -m black .
.PHONY: ci
	ci: precommit lint test
