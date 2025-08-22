import logging
import time
import uuid

from fastapi import Request

from app.src.shared.settings import settings

logger = logging.getLogger(settings.title)


async def log_requests_middleware(request: Request, call_next):
    trace = str(uuid.uuid4())
    start_time = time.time()

    path = request.url.path
    url = str(request.url)
    headers = dict(request.headers)
    params = dict(request.query_params)
    logger.info(
        "Init request",
        extra={
            "http_request": {
                "requestMethod": request.method,
                "requestUrl": url,
                "requestHeaders": headers,
                "requestParams": params,
            },
            "trace": trace,
        },
    )
    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        f"Request to {path} took {duration} seconds",
        extra={
            "http_request": {
                "requestMethod": request.method,
                "latency": str(duration),
                "requestUrl": url,
                "status": str(response.status_code),
                "requestHeaders": headers,
                "requestParams": params,
                "response": response,
            },
            "labels": {
                "duration_time": duration,
            },
            "trace": trace,
        },
    )
    return response
