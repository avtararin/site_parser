PYTHON_VERSION = 3.10.12
VENV_NAME = venv

all: install venv run

install: venv
	. $(VENV_NAME)/bin/activate && pip install -r requirements.txt

venv:
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)

run:
	. $(VENV_NAME)/bin/activate && pip -V
	python3 my_parser.py >> result.txt
test:
	pytest

clean:
	rm -rf $(VENV_NAME) .mypy_cache .pytest_cache tests/.mypy_cache tests/.pytest_cache

	> result.txt