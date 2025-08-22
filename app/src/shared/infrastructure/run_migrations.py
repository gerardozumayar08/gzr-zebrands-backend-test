import alembic
from alembic.config import Config


def run_migrations():
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
