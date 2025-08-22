

from app.src.shared.domain.bus.publish_handler import PublishHandler


class PublishHandlerAWSSES(PublishHandler):
    async def __call__(self):
        ...


