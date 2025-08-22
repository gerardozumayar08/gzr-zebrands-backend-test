from app.src.iam.application.schemas.login import LoginRequest, LoginResponse
from app.src.iam.domain.exceptions.login import (
    InvalidaCredentialsException,
    UserNotFoundException,
)
from app.src.iam.domain.repositories.users_repository import UsersRepository


class LoginUseCase:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    async def __call__(self, login_request: LoginRequest) -> LoginResponse:
        user = await self.users_repository.get_by_username(login_request.username)
        if not user:
            raise UserNotFoundException
        if not user.verify_password(login_request.password):
            raise InvalidaCredentialsException
        token = user.create_access_token()
        return LoginResponse(access_token=token)
