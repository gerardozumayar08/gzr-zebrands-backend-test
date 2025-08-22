from abc import ABC, abstractmethod
from typing import Optional

from app.src.iam.domain.permission import Permission
from app.src.shared.domain.repositories.base_entity_repository import (
    BaseEntityRepository,
)


class PermissionsRepository(ABC, BaseEntityRepository):
    @abstractmethod
    async def get_by(self, id: int) -> Optional[Permission]:
        raise NotImplementedError
