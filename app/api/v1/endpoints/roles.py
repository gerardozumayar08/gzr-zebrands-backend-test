from fastapi import APIRouter, Depends, Request, Response
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
from app.api.v1.responses.schemas.iam.roles import GetRolesSuccessResponse
from app.src.iam.domain.constants.roles_messages import messages
from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.infrastructure.containers.roles_container import RolesContainer

api_router = APIRouter()


auth_scheme = HTTPBearer()


@api_router.get(
    "/roles",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": GetRolesSuccessResponse},
    },
    summary=messages.summary_endpoint_read_role,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
@permission_validator_handler(
    endpoint="/admin/roles", action=PermissionActionsEnum.read
)
async def get_roles(
    request: Request,
    response: Response,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    container_use_case: RolesContainer = Depends(container_manager(RolesContainer)),
):
    use_case = await container_use_case.get_roles()
    response_uc, num_rows = await use_case()
    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=response_uc,
        num_rows=num_rows,
    )
    return domain_response
