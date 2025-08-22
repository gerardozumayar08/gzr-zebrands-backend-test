from fastapi import APIRouter, Body, Depends, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

from app.api.v1.dependencies.container_manager import container_manager
from app.api.v1.dependencies.domain_exception_handler import domain_exception_handler
from app.api.v1.dependencies.exception_handler import exception_handler
from app.api.v1.dependencies.permissions_validator_handler import (
    permission_validator_handler,
)
from app.api.v1.errors.schemas.base import (
    GenericExceptionResponse,
    GenericResponse,
)
from app.api.v1.request.schemas.catalogs.products import (
    CreateProductRequest,
    UpdateProductRequest,
)
from app.api.v1.responses.schemas.catalogs.products import (
    CreateProductSuccessResponse,
    GetProductsSuccessResponse,
    UpdateProductSuccessResponse,
)
from app.src.catalogs.domain.constants.products_messages import messages
from app.src.catalogs.infrastructure.containers.products_container import (
    ProductsContainer,
)
from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.infrastructure.containers.users_container import UsersContainer

api_router = APIRouter()


auth_scheme = HTTPBearer()


@api_router.get(
    "/products",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": GetProductsSuccessResponse},
    },
    summary=messages.summary_endpoint_read_product,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/catalogs/products", action=PermissionActionsEnum.read
)
async def get_products(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: ProductsContainer = Depends(
        container_manager(ProductsContainer)
    ),
):
    use_case = await container_use_case.get_products()
    response_uc, num_rows = await use_case()
    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=response_uc,
        num_rows=num_rows,
    )
    return domain_response


@api_router.post(
    "/products",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": CreateProductSuccessResponse},
    },
    summary=messages.summary_endpoint_create_product,
)
# @exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/catalogs/products", action=PermissionActionsEnum.create
)
async def create_products(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    body: CreateProductRequest = Body(),
    container_use_case: ProductsContainer = Depends(
        container_manager(ProductsContainer)
    ),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.create_product()
        respose_uc = await use_case(body)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=respose_uc,
        num_rows=None,
    )
    return domain_response


@api_router.patch(
    "/products/{product_id}",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": UpdateProductSuccessResponse},
    },
    summary=messages.summary_endpoint_update_product,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/catalogs/products", action=PermissionActionsEnum.update
)
async def update_products(
    request: Request,
    response: Response,
    product_id: int,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    body: UpdateProductRequest = Body(),
    container_use_case: ProductsContainer = Depends(
        container_manager(ProductsContainer)
    ),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.update_product()
        respose_uc = await use_case(product_id, body, str(token.credentials))
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=respose_uc,
        num_rows=None,
    )
    return domain_response


@api_router.delete(
    "/products/{product_id}",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": GenericResponse},
    },
    summary=messages.summary_endpoint_delete_product,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/catalogs/products", action=PermissionActionsEnum.delete
)
async def delete_products(
    request: Request,
    response: Response,
    product_id: int,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: ProductsContainer = Depends(
        container_manager(ProductsContainer)
    ),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.delete_product()
        _ = await use_case(product_id)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_delete_success_message,
        data=None,
        num_rows=None,
    )
    return domain_response


@api_router.get(
    "/products/{product_id}",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": GetProductsSuccessResponse},
    },
    summary=messages.summary_endpoint_delete_product,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/catalogs/products", action=PermissionActionsEnum.read
)
async def get_single_product(
    request: Request,
    response: Response,
    product_id: int,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: ProductsContainer = Depends(
        container_manager(ProductsContainer)
    ),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        product_repository = await container_use_case.products_sqlalchemy_repository()
        product = await product_repository.get_by(product_id)
        if product:
            val_user = await container_use_case.validate_permissions()
            user = await val_user.validate_token(str(token.credentials))
            if user.is_anonymous():
                repo_product_views = (
                    await container_use_case.product_views_sqlalchemy_repository()
                )
                await repo_product_views.save_row(product_id, user.id)

        await uow.commit()

    message = messages.generic_success_message
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        message = messages.product_not_found
    domain_response = GenericResponse(
        message=message,
        data=product,
        num_rows=None,
    )
    return domain_response
