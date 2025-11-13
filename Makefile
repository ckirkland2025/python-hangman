#----- config -----
PY?=python3

#----- tasks -----
.PHONY: venv install setup run test clean

venv:
	@if [ ! -d ".venv" ]; then \
		$(PY) -m venv .venv; \
	fi

install: venv
	. .venv/bin/activate && pip install --upgrade pip
	@if [ -f requirements.txt ]; then \
		. .venv/bin/activate && pip install -r requirements.txt; \
	fi

setup: install
	@echo "Environment ready at .venv"

run: 
	. .venv/bin/activate && python -m hangman.game

test:
	. .venv/bin/activate && pytest -q

clean:
	rm -rf .pytest_cache .coverage htmlcov
