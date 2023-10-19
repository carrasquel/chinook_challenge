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