from typing import List

from app.api.v1.responses.schemas.generic_response import GenericResponse
from app.src.catalogs.application.schemas.products import ProductDTO


class GetProductsSuccessResponse(GenericResponse):
    data: List[ProductDTO]


class CreateProductSuccessResponse(GenericResponse):
    data: ProductDTO


class UpdateProductSuccessResponse(CreateProductSuccessResponse): ...


class GetProductSuccessResponse(GenericResponse):
    data: ProductDTO
