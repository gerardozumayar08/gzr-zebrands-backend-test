import asyncio.exceptions
import logging
import time

import aiohttp

from app.src.shared.domain.exceptions import AsyncHTTPClientException
from app.src.shared.domain.schemas import AsyncHTTPClientResponse
from app.src.shared.settings import settings

logger = logging.getLogger(settings.title)


class AsyncHTTPClient:
    async def __call__(self, **kwargs) -> AsyncHTTPClientResponse:
        try:
            client_timeout = aiohttp.ClientTimeout(
                total=settings.http_client_timeout,
            )
            async with aiohttp.ClientSession(timeout=client_timeout) as session:
                start_time = time.time()
                async with session.request(**kwargs) as response:
                    result = await response.json()
                    duration = time.time() - start_time
                    logger.info(
                        "HTTP Client Response",
                        extra={
                            "http_request": {
                                "latency": str(duration),
                                "requestUrl": kwargs["url"],
                                "status": str(response.status),
                            },
                            "json_fields": {
                                "data": kwargs["data"],
                                "headers": kwargs["headers"],
                                "params": kwargs.get("params", {}),
                                "result": result,
                            },
                        },
                    )
                    return AsyncHTTPClientResponse(
                        result=result, status=response.status
                    )
        except (asyncio.exceptions.TimeoutError, TimeoutError) as e:
            logger.error(
                "Client Error",
                extra={
                    "json_fields": {
                        "error": str(e),
                        "argumentos_error": str(e.args),
                        "kwargs": kwargs,
                    }
                },
            )
            raise AsyncHTTPClientException(f"Timeout, {kwargs['url']}")
        except aiohttp.ClientError as e:
            logger.error(
                "Client Error",
                extra={
                    "json_fields": {
                        "error": str(e),
                        "args_error": str(e.args),
                        "kwargs": kwargs,
                    }
                },
            )
            raise AsyncHTTPClientException(str(e))
