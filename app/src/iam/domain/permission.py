from dataclasses import dataclass
from typing import Optional, List

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum


@dataclass
class Permission:
    resource: str
    action: PermissionActionsEnum
    id: Optional[int] = None
    roles: Optional[List["Role"]] = None
