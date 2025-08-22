from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

# Containers
from app.api.v1.dependencies.container_manager import container_manager
from app.api.v1.dependencies.domain_exception_handler import domain_exception_handler
from app.api.v1.dependencies.exception_handler import exception_handler
from app.api.v1.errors.schemas.base import (
    GenericExceptionResponse,
    GenericResponse,
)
from app.api.v1.responses.schemas.iam.auth import LoginSuccessResponse
from app.src.iam.application.schemas.login import LoginRequest
from app.src.iam.domain.constants.login_messages import messages
from app.src.iam.infrastructure.containers.login_container import LoginContainer

api_router = APIRouter()


@api_router.post(
    "/login",
    response_model={},
    status_code=status.HTTP_200_OK,
    responses={
        400: {"model": GenericExceptionResponse},
        200: {"model": LoginSuccessResponse},
    },
    summary=messages.summary_endpoint_login,
)
@exception_handler
@domain_exception_handler(
    error_message=messages.generic_error_message,
)
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    container_use_case: LoginContainer = Depends(container_manager(LoginContainer)),
):
    async with await container_use_case.main_container.unit_of_work() as uow:
        data_input = LoginRequest(
            username=form_data.username, password=form_data.password
        )
        use_case = await container_use_case.use_case()
        response = await use_case(data_input)
        await uow.commit()

    domain_response = GenericResponse(
        message=messages.generic_success_message,
        data=response,
        num_rows=1,
    )
    return domain_response
