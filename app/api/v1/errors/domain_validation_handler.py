from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.src.shared.domain.exceptions import DomainException


class DomainValidationException(DomainException):
    def __init__(self, message):
        super().__init__(message=message)


def domain_validation_exception_handler(
    _: Request, exc: DomainValidationException
) -> JSONResponse:
    data = jsonable_encoder(exc.dict())
    return JSONResponse(
        data,
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )
