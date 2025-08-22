from app.src.catalogs.application.schemas.products import ProductDTO
from app.src.catalogs.domain.exceptions.products import ProductNotFoundException
from app.src.catalogs.domain.repositories.products_repository import ProductsRepository


class DeleteProductUseCase:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def __call__(self, id) -> ProductDTO:
        product = await self.products_repository.get_by(id)
        if not product:
            raise ProductNotFoundException
        await self.products_repository.delete(product)
