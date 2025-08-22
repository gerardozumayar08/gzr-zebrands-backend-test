from typing import Optional, Tuple, List

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy import func
from sqlalchemy.sql.selectable import Select

from app.src.iam.domain.repositories.roles_reporisoty import RolesRepository
from app.src.iam.domain.role import Role
from app.src.shared.infrastructure.repositories.base_sqlalchemy_repository import (
    BaseSqlAlchemyRepository,
)


class RolesSQLAlchemyRepository(BaseSqlAlchemyRepository, RolesRepository):
    async def get_by(self, id: int) -> Optional[Role]:
        query = select(Role).where(Role.id == id)
        return self.session.execute(query).scalar()

    async def save(self, entity: Role):
        self.session.add(entity)

    async def update(self, entity: Role):
        self.session.add(entity)

    async def get_all(
        self,
    ) -> Tuple[List[Role], int]:
        query = select(
            Role,
        )
        num_rows = await self.count_rows(query)
        rows = self.session.execute(query)
        return rows.scalars().all(), num_rows

    async def count_rows(self, query: Select):
        numero_registros = select(func.count()).select_from(query.subquery())
        return self.session.execute(numero_registros).scalar_one()
