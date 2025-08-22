from app.src.shared.domain.unit_of_work import UnitOfWork
from sqlalchemy.orm import Session
from app.src.shared.domain.bus.publisher_notification_bus import PublishNotificationBus

class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: Session, notification_bus: PublishNotificationBus):
        self.session = session
        self.notification_bus = notification_bus

    async def __aenter__(self):
        enter = await super().__aenter__()
        return enter

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        self.session.close()
        await self.send_notifications()

    async def _commit(self):
        self.session.commit()

    async def rollback(self):
        self.session.rollback()

    async def send_notifications(self):
        self.notification_bus.send()