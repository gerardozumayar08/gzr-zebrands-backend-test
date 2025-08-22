from typing import Callable, List, Optional

from app.src.shared.domain.bus.email import EmailSchema


class PublishNotificationBus:
    def __init__(self, notifier_handler: Callable = None):
        self._notifier_handler: Optional[Callable] = notifier_handler
        self.emails = []

    def save_mail(self, emails: List[EmailSchema]) -> None:
        if self.emails:
            self.emails.append(emails)
        else:
            self.emails = emails

    def send(self) -> None:
        for email in self.emails:
            self._notifier_handler(email)
