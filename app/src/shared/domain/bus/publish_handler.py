import abc
from abc import abstractmethod


class PublishHandler(abc.ABC):
    def __init__(self, settings: dict):
        self.settings = settings

    @abstractmethod
    async def __call__(self):
        pass
