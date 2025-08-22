import jwt
from jwt import PyJWTError

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.domain.exceptions.login import (
    InvalidaTokenException,
    PermissionDeniedException,
    UserNotFoundException,
)
from app.src.iam.domain.repositories.users_repository import UsersRepository
from app.src.iam.domain.user import User
from app.src.shared.settings import settings


class ValidatePermissionsUseCase:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    async def __call__(self, token: str, endpoint, action):
        user = await self.validate_token(token.credentials)
        self.validate_permission(user, endpoint, action)

    def validate_permission(
        self, current_user: User, endpoint: str, action: PermissionActionsEnum
    ):
        if not current_user.has_permission(endpoint, action):
            raise PermissionDeniedException

    async def validate_token(self, token) -> User:
        try:
            payload = jwt.decode(
                token, settings.secret_key, algorithms=[settings.algorithm]
            )
        except PyJWTError:
            raise InvalidaTokenException

        user_id: int = payload.get("sub")
        if user_id is None:
            raise InvalidaTokenException

        user = await self.users_repository.get_by(user_id)
        if not user:
            raise UserNotFoundException
        return user
