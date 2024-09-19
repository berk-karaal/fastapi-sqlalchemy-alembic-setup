# FastAPI project with async SQLAlchemy, Alembic and Docker

This is the completed version of the project on my blog post
[here](https://berkkaraal.com/blog/2024/09/19/setup-fastapi-project-with-async-sqlalchemy-2-alembic-postgresql-and-docker/).
The project demonstrates how to create a FastAPI project with async SQLAlchemy, Alembic, PostgreSQL
and Docker.

## Start the server without Docker

1. Create a virtual environment and activate it:

    ```console
    $ virtualenv venv --python python3.11
    $ source venv/bin/activate
    ```
2. Install the dependencies:

    ```console
    $ pip install -r requirements.txt
    ```
3. Start the PostgreSQL database:

    ```console
    $ docker compose up -d postgres
    ```
4. Run the migrations:

    ```console
    $ alembic upgrade head
    ```
5. Start the FastAPI server:

    ```console
    $ python3 -m src.main
    ```

    You can access the swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs).

## Start the server with Docker

Simply just run `$ docker compose up -d` to start the project with Docker. You can follow the logs
using `$ docker compose logs -f backend` command. You can stop the project with `$ docker compose
down`.

You can access the swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs).