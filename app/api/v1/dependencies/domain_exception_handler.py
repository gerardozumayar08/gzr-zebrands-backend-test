from functools import wraps
from typing import Callable

from fastapi import Response, status

from app.api.v1.errors.schemas.base import GenericExceptionResponse
from app.src.shared.domain.exceptions import DomainException


def domain_exception_handler(
    error_message: str,
    status_code_exception: int = status.HTTP_400_BAD_REQUEST,
):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            response: Response = kwargs.get("response")
            try:
                response_uc = await func(*args, **kwargs)
                return response_uc
            except DomainException as e:
                if response:
                    response.status_code = (
                        getattr(e, "status_code")
                        if hasattr(e, "status_code")
                        else status_code_exception
                    )
                if message_exception := getattr(e, "message"):
                    error_mesage_output = message_exception
                else:
                    error_mesage_output = error_message
                return GenericExceptionResponse(
                    **{
                        "message": error_mesage_output,
                    }
                )
            finally:
                container_use_case = kwargs.get("container_use_case")
                if container_use_case:
                    await container_use_case.shutdown_resources()

        return wrapper

    return decorator
