import os
from logging.config import fileConfig

from alembic import context
from alembic_utils.pg_grant_table import PGGrantTable
from alembic_utils.pg_trigger import PGTrigger
from alembic_utils.pg_function import PGFunction
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
from src.database.base import BaseModel


target_metadata = [BaseModel.metadata]

url = str(os.getenv("ALEMBIC_DB_URL"))


def include_object(object, name, type_, reflected, compare_to) -> bool:
    if isinstance(object, (PGTrigger, PGGrantTable, PGFunction)):
        return False
    return True


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_schemas=True,
            include_object=include_object,
        )

        with context.begin_transaction() as transaction:
            context.run_migrations()
            if 'dry-run' in context.get_x_argument():
                print('Dry-run succeeded; now rolling back transaction...')
                transaction.rollback()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
