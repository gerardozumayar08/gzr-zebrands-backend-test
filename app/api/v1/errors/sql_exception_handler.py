import logging

from fastapi.responses import JSONResponse
from sqlalchemy.exc import DatabaseError, IntegrityError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.api.v1.errors.schemas.base import GenericExceptionResponse
from app.src.shared.utils.exceptions_datails import get_exception_details
from app.src.shared.settings import settings

logger = logging.getLogger(settings.title)


def parse_exception_integrity(exc: IntegrityError):
    texto = exc._message().split("DETAIL:")[-1].strip()
    return texto


map_excepction_parser = {IntegrityError: parse_exception_integrity}


async def sql_exception_handler(_, exc: DatabaseError):
    message = map_excepction_parser.get(type(exc), lambda x: "Not defined")(exc)
    exception_details = get_exception_details(exc)
    logger.error(
        "DatabaseErrorDetails",
        extra={
            "json_fields": exception_details,
            "status_code": HTTP_422_UNPROCESSABLE_ENTITY,
        },
    )
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=GenericExceptionResponse(message=message).model_dump(),
        media_type="application/json",
    )
