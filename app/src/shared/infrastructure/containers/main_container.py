from dependency_injector import containers, providers

from app.src.shared.infrastructure.async_http_client import AsyncHTTPClient
from app.src.shared.infrastructure.containers.custom_providers import (
    UnitOfWorkProvider,
    PublishHandlerProvider,
)

from app.src.shared.infrastructure.db_connections import database

from app.src.shared.infrastructure.sqla_unit_of_work import (
    SqlAlchemyUnitOfWork,
)
from app.src.shared.infrastructure.bus.aws_ses import (
    SESNotifier,
)
from app.src.shared.domain.bus.publisher_notification_bus import PublishNotificationBus

from app.src.shared.settings import settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict(settings.model_dump())
    session = providers.Resource(database.get_db)
    
    notification_publish_handler = PublishHandlerProvider(
        SESNotifier, settings=settings
    )
    notification_bus = providers.Singleton(
        PublishNotificationBus, notifier_handler=notification_publish_handler
    )
    http_client = providers.Factory(
        AsyncHTTPClient,
    )
    unit_of_work = UnitOfWorkProvider(
        SqlAlchemyUnitOfWork,
        session=session,
        notification_bus=notification_bus
    )
