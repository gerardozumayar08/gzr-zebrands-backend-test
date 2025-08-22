from dependency_injector import providers

from app.src.shared.domain.unit_of_work import UnitOfWork
from app.src.shared.domain.bus.publish_handler import PublishHandler


class UnitOfWorkProvider(providers.Singleton):
    provider_type = UnitOfWork


class PublishHandlerProvider(providers.Singleton):
    provider_type = PublishHandler