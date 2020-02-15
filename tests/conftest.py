import os
import tempfile

import pytest
from alembic.command import upgrade
from alembic.config import Config

from src.main import create_app


SQLITE_DB_FILENAME_MASTER = "master_sqlite.db"
SQLITE_DB_FILENAME_COPY = "sqlite.db"
SQLITE_DB_DIRECTORY_MASTER = "master_sqlite"


@pytest.fixture(scope="session")
def prepare_master_sqlite_db(tmpdir_factory):
    directory = tmpdir_factory.mktemp(SQLITE_DB_DIRECTORY_MASTER)
    path = directory.join(SQLITE_DB_FILENAME_MASTER)
    migrations_dir = os.getcwd()
    config_file = os.path.join(migrations_dir, "alembic.ini")
    config = Config(file_=config_file)
    config.set_main_option('database_url.drivername', 'sqlite')
    config.set_main_option('database_url.database', path.strpath)
    upgrade(config, "head")
    return path


@pytest.fixture
def app():
    master_db = prepare_master_sqlite_db()

    app = create_app({
        'TESTING': True,
    })

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
