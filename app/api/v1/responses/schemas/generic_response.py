from typing import Any, Optional

from pydantic import BaseModel, Field


class GenericResponse(BaseModel):
    message: Optional[str] = Field(
        default=None, title="Response message", max_length=250
    )
    data: Any = None
    num_rows: Optional[int] = Field(default=None, title="Number of records")
