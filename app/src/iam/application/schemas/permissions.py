from pydantic import BaseModel, ConfigDict

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum


class PermissionsDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    resource: str
    action: PermissionActionsEnum
    id: int
