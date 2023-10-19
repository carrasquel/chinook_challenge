# chinook_challenge
Chinook small project with Pyramid

This is sample project which is a small web application with the chinook database, it runs with Python and the Pyramid Framework.

## Create virtual environment

In order to execute this app in a development environment you can setup a virtual environment with the following:

```
make env
```

## Install dependencies

To install dependencies

```
make deps
```

## Execute development server

To run the web application in this development environment

```
make run-dev
```

## Run tests

Tests are performed with **pytest** and converage with **pytest-cov**

```
make test
make coverage
```