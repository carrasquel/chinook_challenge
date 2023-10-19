ifndef VENVNAME
  VENVNAME = venv
endif

ifeq ($(OS),Windows_NT)
	CURRENT_DIR = $(shell cd)
	INTERPRETER_DIR = $(CURRENT_DIR)/$(VENVNAME)/Scripts
else
	CURRENT_DIR = $(shell pwd)
	INTERPRETER_DIR = $(CURRENT_DIR)/$(VENVNAME)/bin
endif

PYTHON=$(INTERPRETER_DIR)/python

python:
	@echo "[RUN]: activate virtual environment"
	$(INTERPRETER_DIR)/python

env:
	@echo "[RUN]: create virtual environment"
	python -m venv venv

activate:
	@echo "[RUN]: activate virtual environment"
	$(INTERPRETER_DIR)/activate && pip -V

deps: activate
	@echo "[RUN]: install dependencies"
	$(INTERPRETER_DIR)/pip install -r ./requirements.txt
	$(INTERPRETER_DIR)/pip install -r ./dev-requirements.txt

run-dev: activate
	@echo "[RUN]: run development server"
	python ./server.py

cli: activate
	@echo "[RUN]: run app cli"
	$(INTERPRETER_DIR)/activate && python -i ./cli.py

isort:
	$(PYTHON) -m isort --check-only .

black:
	$(PYTHON) -m black --check .

flake8:
	$(PYTHON) -m flake8 .

bandit:
	$(PYTHON) -m bandit -r app

lint: isort black flake8 bandit

test:
	$(PYTHON) -m pytest
