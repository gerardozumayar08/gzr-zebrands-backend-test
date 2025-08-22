from functools import wraps

from fastapi import Request

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum


def permission_validator_handler(endpoint: str, action: PermissionActionsEnum):
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            container_use_case = kwargs.get("container_use_case")
            token = kwargs.get("token")
            validation = await container_use_case.validate_permissions()
            await validation(token, endpoint, action)
            return await func(request, *args, **kwargs)
        return wrapper

    return decorator
