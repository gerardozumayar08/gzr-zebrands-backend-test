from abc import abstractmethod
from typing import List, Optional, Tuple

from app.src.catalogs.domain.product import Product
from app.src.shared.domain.repositories.base_entity_repository import (
    BaseEntityRepository,
)


class ProductsRepository(BaseEntityRepository):
    @abstractmethod
    async def get_by(self, id: int) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self,
    ) -> Tuple[List[Product], int]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, product_id):
        raise NotImplementedError
