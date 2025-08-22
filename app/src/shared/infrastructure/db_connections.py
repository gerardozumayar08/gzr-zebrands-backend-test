import asyncio
import functools
import logging
from typing import AsyncGenerator

from app.src.shared.settings import Settings, settings
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.pool import NullPool

logger = logging.getLogger(settings.title)


def retrieve_session_maker_class(settings: Settings = settings, engine=None):
    DEFAULT_SESSION_FACTORY = create_async_engine(
        settings.sql_uri_connection, echo=False, poolclass=NullPool
    )
    if settings.environment == "smoke_test":
        return None
    engine_factory = DEFAULT_SESSION_FACTORY if not engine else engine
    async_session = sessionmaker(
        engine_factory,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    if settings.threading:
        async_session = scoped_session(async_session, scopefunc=asyncio.current_task)
    return async_session


@functools.lru_cache
def obtener_db():
    db = retrieve_session_maker_class()
    return db()


class Database:
    def __init__(self, database_uri: str, echo_sql: bool = True) -> None:
        self.__async_engine = create_engine(
            database_uri,
            max_overflow=10,
            pool_size=10,
            pool_recycle=900,
            pool_timeout=30,
            echo=echo_sql,
        )
        self._session_local = sessionmaker(
            bind=self.__async_engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def get_db(
        self,
    ) -> AsyncGenerator[Session, None]:
        try:
            with self._session_local() as session:
                yield session
        except Exception as e:
            logger.error(e)
            raise SQLAlchemyError(
                status_code=500, detail=f"Error in the Database: {str(e)}"
            )


database = Database(settings.sql_uri_connection, echo_sql=False)
