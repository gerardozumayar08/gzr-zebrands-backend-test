from typing import List

from pydantic import BaseModel, ConfigDict

from app.src.iam.application.schemas.permissions import PermissionsDTO


class RoleDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    id: int
    permissions: List[PermissionsDTO]

