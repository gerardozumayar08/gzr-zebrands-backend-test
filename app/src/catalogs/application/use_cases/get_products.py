from typing import List, Tuple

from app.src.catalogs.domain.repositories.products_repository import ProductsRepository
from app.src.catalogs.application.schemas.products import ProductDTO


class GetProductsUseCase:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def __call__(
        self,
    ) -> Tuple[List[ProductDTO], int]:
        data, num_rows = await self.products_repository.get_all()
        data = [ProductDTO.model_validate(d) for d in data]
        return data, num_rows
