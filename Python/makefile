PYTHON=python

.PHONY: clean-pyc

default: run

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	flake8

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

run:
	$(PYTHON) main.py
