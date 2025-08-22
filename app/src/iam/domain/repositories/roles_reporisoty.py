from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from app.src.iam.domain.role import Role
from app.src.shared.domain.repositories.base_entity_repository import (
    BaseEntityRepository,
)


class RolesRepository(ABC, BaseEntityRepository):
    @abstractmethod
    async def get_by(self, id: int) -> Optional[Role]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
    ) -> Tuple[List[Role], int]:
        raise NotImplementedError
