lint:
	pipenv run mypy -p src

test:
	pipenv run python -m unittest

run:
	pipenv run python -m src.main
