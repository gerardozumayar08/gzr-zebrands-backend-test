from typing import Dict

from pydantic import BaseModel


class AsyncHTTPClientResponse(BaseModel):
    result: Dict
    status: int
