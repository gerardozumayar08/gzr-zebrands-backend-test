from dataclasses import dataclass, field
from typing import List, Optional

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.domain.role import Role
from app.src.iam.infrastructure.auth import create_access_token, verify_password


@dataclass
class User:
    username: str
    fullname: str
    email: str
    hashed_password: str
    is_active: bool
    id: Optional[int] = None
    roles: Optional[List[Role]] = field(default_factory=list)

    def verify_password(self, password):
        return verify_password(password, self.hashed_password)

    def create_access_token(self):
        return create_access_token(data={"sub": str(self.id)})

    def has_permission(self, endpoint: str, action: PermissionActionsEnum) -> bool:
        return any(
            perm.resource == endpoint and perm.action == action
            for role in self.roles
            for perm in role.permissions
        )

    def is_admin(
        self,
    ) -> bool:
        return any(role.name == "admin" for role in self.roles)

    def is_anonymous(
        self,
    ) -> bool:
        return all(role.name == "anonymous" for role in self.roles)
