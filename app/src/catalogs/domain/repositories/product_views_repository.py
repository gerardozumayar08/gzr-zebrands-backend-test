from abc import abstractmethod
from typing import List, Optional, Tuple

from app.src.catalogs.domain.product_view import ProductView
from app.src.shared.domain.repositories.base_entity_repository import (
    BaseEntityRepository,
)


class ProductViewsRepository(BaseEntityRepository):
    @abstractmethod
    async def get_by(self, id: int) -> Optional[ProductView]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
    ) -> Tuple[List[ProductView], int]:
        raise NotImplementedError
