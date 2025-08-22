from app.src.catalogs.application.schemas.products import (
    ProductDTOInput,
    ProductDTOOptionalInput,
)


class CreateProductRequest(ProductDTOInput): ...


class UpdateProductRequest(ProductDTOOptionalInput): ...
