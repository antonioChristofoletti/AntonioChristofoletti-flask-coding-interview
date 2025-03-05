# Flask Coding Challenge

This repository contains the base code to complete the Flask Coding Challenge.

## Requirements

- Have Python 3.9 or higher installed. We recommend using [pyenv](https://github.com/pyenv/pyenv).
- Have installed Poetry. Visit the [poetry](https://python-poetry.org/docs/) website for more info.

**Do this before the interview so you don't have to wait for the dependencies to install or lose time with environment setup.**

## Setting up the environment

- Clone this repository
- Install the dependencies using `poetry install`.

## Setting up the database

- It's necessary to have access to a SQL database. We recommend using Postgres.

  - You can run Postgres in a Docker container.
  - Another alternative is to use [ElephantSQL](https://www.elephantsql.com/plans.html) to get a free Postgres database instance in the cloud.

- Setup your database connection string in the `alembic.ini` file.
- We're using alembic to manage migrations. Run the initial migrations using `poetry run alembic upgrade head`.

## Running the Application

- Start your flask server using `poetry run flask run`.

## Running tests

We're using pytest to run tests. You can run the tests by running `poetry run pytest`.

We've already provided you with some boilerplate to run database tests. You can find them in the `tests` folder.

## Folder structure:

- `alembic`: Contains the alembic configuration and migrations.
- `api`: Contains the flask apps.
- `tests`: Contains the tests.

We've installed flask-openapi3, which will generate an OpenAPI 3 specification for you. You can find it at `/openapi`.

This library also makes it slightly different to develop your API, making Flask flavor a little more like FastAPI
(eg.: instead of router.route, you use router.get/post/put, etc). It also uses pydantic for schema definition.
You can read more about it [here](https://luolingchun.github.io/flask-openapi3/v2.x/Quickstart/).
