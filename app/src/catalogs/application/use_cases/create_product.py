from app.src.catalogs.application.schemas.products import ProductDTO, ProductDTOInput
from app.src.catalogs.domain.exceptions.products import CreationProductException
from app.src.catalogs.domain.product import Product
from app.src.catalogs.domain.repositories.products_repository import ProductsRepository


class CreateProductUseCase:
    def __init__(
        self,
        products_repository: ProductsRepository,
    ):
        self.products_repository = products_repository

    async def __call__(self, product_dto: ProductDTOInput) -> ProductDTO:
        try:
            product = Product(**product_dto.model_dump())
            await self.products_repository.save(product)
            return ProductDTO.model_validate(product)
        except Exception:
            raise CreationProductException
