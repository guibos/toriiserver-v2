import os
import shutil

import pytest
from alembic.command import upgrade
from alembic.config import Config

from src.infrastructure.database.facade import DatabaseFacade
from src.infrastructure.database.value_objects.database_url_value_object import DatabaseURLValueObject
from src.main import App

APP_CONFIG = {
    'TESTING': True,
}

SQLITE_DB_FILENAME_MASTER = "master_sqlite.db"
SQLITE_DB_FILENAME_COPY = "sqlite.db"
SQLITE_DB_DIRECTORY_MASTER = "master_sqlite"


@pytest.fixture(scope="session")
def sqlite_prepare_master_db(tmpdir_factory):
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
def sqlite(tmpdir, sqlite_prepare_master_db):
    path = tmpdir.join(SQLITE_DB_FILENAME_COPY)
    shutil.copy(sqlite_prepare_master_db, tmpdir.join(SQLITE_DB_FILENAME_COPY))
    database_url = DatabaseURLValueObject(drivername='sqlite', database=path)
    database_facade = DatabaseFacade(database_url_config=database_url)

    return database_facade


@pytest.fixture
def app(sqlite):
    app = App(database_facade=sqlite, config=APP_CONFIG)

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
