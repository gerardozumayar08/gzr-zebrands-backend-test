from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    fullname: str
    is_active: bool


class UserDTOInput(BaseModel):
    username: str
    password: str
    email: str
    fullname: str
    roles_ids: List[int]


class UserDTOOptionalInput(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    fullname: Optional[str] = None
    roles_ids: Optional[List[int]] = None
