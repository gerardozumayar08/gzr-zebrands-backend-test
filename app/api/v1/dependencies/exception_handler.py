from functools import wraps

from fastapi import HTTPException, status


def exception_handler(endpoint):
    @wraps(endpoint)
    async def wrapper(*args, **kwargs):
        try:
            return await endpoint(*args, **kwargs)
        except HTTPException as exc:
            raise exc
        except Exception as exc:
            raise HTTPException(
                detail=f"Internal error: {exc}, {exc.args}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    return wrapper
