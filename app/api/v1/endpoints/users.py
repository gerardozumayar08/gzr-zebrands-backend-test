from fastapi import APIRouter, Body, Depends, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

# Containers
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
from app.api.v1.request.schemas.iam.users import CreateUserRequest, UpdateUserRequest
from app.api.v1.responses.schemas.iam.users import (
    GetUsersSuccessResponse,
    CreateUserSuccessResponse,
    UpdateUserSuccessResponse,
)
from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.domain.constants.users_messages import messages
from app.src.iam.infrastructure.containers.users_container import UsersContainer

api_router = APIRouter()


auth_scheme = HTTPBearer()


@api_router.get(
    "/users",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": GetUsersSuccessResponse},
    },
    summary=messages.summary_endpoint_read_user,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/admin/users", action=PermissionActionsEnum.read
)
async def get_users(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: UsersContainer = Depends(container_manager(UsersContainer)),
):
    use_case = await container_use_case.get_users()
    response_uc, num_rows = await use_case()
    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=response_uc,
        num_rows=num_rows,
    )
    return domain_response


@api_router.post(
    "/users",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": CreateUserSuccessResponse},
    },
    summary=messages.summary_endpoint_create_user,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/admin/users", action=PermissionActionsEnum.create
)
async def create_users(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    body: CreateUserRequest = Body(),
    container_use_case: UsersContainer = Depends(container_manager(UsersContainer)),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.create_user()
        respose_uc = await use_case(body)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=respose_uc,
        num_rows=None,
    )
    return domain_response


@api_router.patch(
    "/users/{user_id}",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": UpdateUserSuccessResponse},
    },
    summary=messages.summary_endpoint_update_user,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/admin/users", action=PermissionActionsEnum.update
)
async def update_users(
    request: Request,
    response: Response,
    user_id: int,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    body: UpdateUserRequest = Body(),
    container_use_case: UsersContainer = Depends(container_manager(UsersContainer)),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.update_user()
        respose_uc = await use_case(user_id, body)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=respose_uc,
        num_rows=None,
    )
    return domain_response


@api_router.delete(
    "/users/{user_id}",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": UpdateUserSuccessResponse},
    },
    summary=messages.summary_endpoint_delete_user,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/admin/users", action=PermissionActionsEnum.delete
)
async def delete_users(
    request: Request,
    response: Response,
    user_id: int,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: UsersContainer = Depends(container_manager(UsersContainer)),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        use_case = await container_use_case.delete_user()
        _ = await use_case(user_id)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_delete_success_message,
        data=None,
        num_rows=None,
    )
    return domain_response