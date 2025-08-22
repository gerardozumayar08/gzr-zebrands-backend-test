from abc import abstractmethod
from typing import Any, Optional


class BaseEntityRepository:
    @abstractmethod
    async def get_by(self, id: int) -> Optional[Any]:
        raise NotImplementedError

    @abstractmethod
    async def save(self, entity: Any):
        raise NotImplementedError

    @abstractmethod
    async def update(self, entity: Any):
        raise NotImplementedError
