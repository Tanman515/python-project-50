install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

build:
	poetry build

package-install:
	python -m pip install --user --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml