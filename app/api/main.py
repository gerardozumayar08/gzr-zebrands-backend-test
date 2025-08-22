from functools import lru_cache

from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from pydantic import ValidationError
from contextlib import asynccontextmanager

from app.api.v1.dependencies.middleware import log_requests_middleware

# from app.api.v1.endpoints import health_check
from app.api.v1.endpoints.api_router import api_router as api_router_v1
from app.api.v1.errors.domain_validation_handler import (
    DomainValidationException,
    domain_validation_exception_handler,
)
from app.api.v1.errors.http_exception_handler import http_exception_handler
from app.api.v1.errors.sql_exception_handler import (
    DatabaseError,
    sql_exception_handler,
)
from app.api.v1.errors.validation_error_handler import http422_error_handler
from app.src.shared.infrastructure.mappers import start_mappers
from app.src.shared.settings import settings
from app.src.shared.utils.logger import get_logger
from app.src.shared.infrastructure.run_migrations import run_migrations

start_mappers()


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_migrations()

    yield



@lru_cache(maxsize=None)
def get_application() -> FastAPI:
    get_logger()
    application = FastAPI(
        title=settings.title,
        description=settings.description,
        version=settings.version,
        servers=[
            {
                "url": "http://localhost:8080",
                "description": "Local enviroment (local)",
            },
            {
                "url": "",
                "description": "real enviroment (dev)",
            },
        ],
        openapi_tags=[
            {"name": settings.name, "description": settings.description_openapi}
        ],
        lifespan=lifespan,
    )
    application.middleware("http")(log_requests_middleware)

    application.include_router(api_router_v1, prefix=settings.api_v1_str)

    # application.include_router(health_check.api_router)
    application.add_exception_handler(
        DomainValidationException, domain_validation_exception_handler
    )
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.add_exception_handler(ValidationError, http422_error_handler)
    application.add_exception_handler(DatabaseError, sql_exception_handler)
    application.add_exception_handler(HTTPException, http_exception_handler)

    return application


app = get_application()
