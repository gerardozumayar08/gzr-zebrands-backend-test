from typing import Any, Optional

from pydantic import BaseModel, Field


class GenericResponse(BaseModel):
    data: Optional[Any] = None
    message: Optional[str] = None
    rows: Optional[int] = None


class GenericExceptionResponse(GenericResponse):
    message: str
    data: Optional[Any] = Field(default=None)
