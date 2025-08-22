import os

import alembic
from alembic.config import Config
import pytest
import pytest_asyncio

from app.src.shared.infrastructure.containers.main_container import MainContainer


@pytest_asyncio.fixture(scope="function")
async def inicializar_main_container():
    main_container = MainContainer()
    await main_container.init_resources()
    yield main_container
    await main_container.shutdown_resources()


@pytest_asyncio.fixture(scope="function")
async def main_container_sql_session(inicializar_main_container):
    yield await inicializar_main_container.session()


@pytest_asyncio.fixture(scope="function")
async def main_container_uow(inicializar_main_container):
    async with await inicializar_main_container.unit_of_work() as uow:
        yield uow


@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    #alembic.command.downgrade(config, "base")
