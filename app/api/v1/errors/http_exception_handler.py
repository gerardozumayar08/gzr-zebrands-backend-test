import logging

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.api.v1.errors.schemas.base import GenericExceptionResponse
from app.src.shared.settings import settings

logger = logging.getLogger(settings.title)


async def http_exception_handler(_, exc: HTTPException):
    content = GenericExceptionResponse(
        message=exc.detail,
        data={"mensaje": exc.detail},
    ).model_dump()

    content = jsonable_encoder(content)
    logger.error(
        "HTTPException",
        extra={
            "json_fields": jsonable_encoder(content),
            "status_code": exc.status_code,
        },
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(content),
        media_type="application/json",
    )
