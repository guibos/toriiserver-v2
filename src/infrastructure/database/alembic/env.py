import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
from sqlalchemy.engine.url import URL


sys.path.append(os.getcwd())

from src.infrastructure.database.models.title_model import Base
from src.infrastructure.configuration.configuration_repository import Configuration
from src.infrastructure.database.value_objects.database_url_value_object import DatabaseURLValueObject


config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def set_config() -> None:
    if not config.get_main_option("database_url.drivername"):
        url_config = Configuration().get_section(section='database')
        for key in url_config:
            if url_config[key]:  # Not None Values
                config.set_main_option(f'database_url.{key}', url_config[key])


def get_url() -> URL:
    return DatabaseURLValueObject(
        drivername=config.get_main_option('database_url.drivername'),
        username=config.get_main_option('database_url.username'),
        password=config.get_main_option('database_url.password'),
        host=config.get_main_option('database_url.host'),
        port=config.get_main_option('database_url.port'),
        database=config.get_main_option('database_url.database'),
        query=config.get_main_option('database_url.query'),
    ).get_url()


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    config_ini = config.get_section(config.config_ini_section)
    config_ini['sqlalchemy.url'] = get_url()
    connectable = engine_from_config(
        config_ini,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


set_config()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
