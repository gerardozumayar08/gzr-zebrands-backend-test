from abc import abstractmethod
from typing import Optional, Tuple, List

from app.src.iam.domain.user import User
from app.src.shared.domain.repositories.base_entity_repository import (
    BaseEntityRepository,
)


class UsersRepository(BaseEntityRepository):
    @abstractmethod
    async def get_by(self, id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
    ) -> Tuple[List[User], int]:
        raise NotImplementedError
    
    @abstractmethod
    async def delete(
        self,
    ) -> Tuple[List[User], int]:
        raise NotImplementedError
    

    @abstractmethod
    async def get_all_admins(
        self,
    ) -> List[User]:
        raise NotImplementedError
