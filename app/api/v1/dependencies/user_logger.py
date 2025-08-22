from functools import wraps

from fastapi import Request


def admin_user_handler():
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            container_use_case = kwargs.get("container_use_case")
            token = kwargs.get("token")
            user_logger = await container_use_case.logger_admin_user()
            await user_logger(token)
            return await func(request, *args, **kwargs)

        return wrapper

    return decorator
