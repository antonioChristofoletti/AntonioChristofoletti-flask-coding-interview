import os

import pytest
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.db import Base


@pytest.fixture(scope="session")
def db():
    # Set up the in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")

    # Create a new Alembic configuration object
    parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    alembic_ini_path = os.path.join(parent_dir, "alembic.ini.test")
    alembic_cfg = Config(alembic_ini_path)

    # Associate the SQLite database URL with the configuration object
    alembic_cfg.set_main_option("sqlalchemy.url", str(engine.url))

    # Run the Alembic upgrade command to apply migrations
    command.upgrade(alembic_cfg, "head")

    # Create a session factory and bind it to the database connection
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and return the session-bound database connection
    connection = session.connection()
    Base.metadata.create_all(bind=connection)
    yield Session
    session.rollback()
    connection.close()
