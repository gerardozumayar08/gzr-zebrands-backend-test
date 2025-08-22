from typing import Optional, Tuple, List

from sqlalchemy import select

from sqlalchemy import func
from sqlalchemy.sql.selectable import Select
from sqlalchemy.orm import joinedload

from app.src.iam.domain.repositories.users_repository import UsersRepository
from app.src.iam.domain.user import User
from app.src.iam.domain.role import Role
from app.src.shared.infrastructure.repositories.base_sqlalchemy_repository import (
    BaseSqlAlchemyRepository,
)


class UsersSQLAlchemyRepository(BaseSqlAlchemyRepository, UsersRepository):
    async def get_by(self, id: int) -> Optional[User]:
        query = select(User).where(User.id == id)
        return self.session.execute(query).scalar()

    async def get_by_username(self, username: str) -> Optional[User]:
        query = select(User).where(User.username == username)
        return self.session.execute(query).scalar()

    async def save(self, entity: User):
        self.session.add(entity)
        self.session.flush()

    async def update(self, entity: User):
        self.session.add(entity)

    async def get_all(
        self,
    ) -> Tuple[List[User], int]:
        fields = (
            User.id,
            User.username,
            User.email,
            User.fullname,
            User.is_active,
        )
        query = select(*fields)
        num_rows = await self.count_rows(query)
        rows = self.session.execute(query).fetchall()

        rows_as_dicts = [
            {f"{key}": value for key, value in row._mapping.items()} for row in rows
        ]
        return rows_as_dicts, num_rows

    async def count_rows(self, query: Select):
        numero_registros = select(func.count()).select_from(query.subquery())
        return self.session.execute(numero_registros).scalar_one()

    async def delete(self, entity: User):
        self.session.delete(entity)

    async def get_all_admins(
        self,
    ) -> List[User]:
        query = (
            select(User)
            .join(User.roles)
            .filter(Role.name == "admin")
            .options(joinedload(User.roles))
        )
        result = self.session.execute(query)
        users = result.unique().scalars().all()
        return users
