from typing import Optional

from sqlalchemy import select

from app.src.iam.domain.permission import Permission
from app.src.iam.domain.repositories.permissions_repository import PermissionsRepository
from app.src.shared.infrastructure.repositories.base_sqlalchemy_repository import (
    BaseSqlAlchemyRepository,
)


class PermissionsSQLAlchemyRepository(BaseSqlAlchemyRepository, PermissionsRepository):
    async def get_by(self, id: int) -> Optional[Permission]:
        query = select(Permission).where(Permission.id == id)
        return self.session.execute(query).scalar()

    async def save(self, entity: Permission):
        self.session.add(entity)

    async def update(self, entity: Permission):
        self.session.add(entity)
