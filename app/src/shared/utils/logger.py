import logging

from app.src.shared.settings import settings


def get_logger():
    logging.getLogger(settings.title)
    return logging.getLogger(settings.title)
