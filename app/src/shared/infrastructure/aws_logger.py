import json
import logging
from datetime import datetime

import boto3
import watchtower

from app.src.shared.settings import settings


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        if record.args and isinstance(record.args, dict):
            log_record.update(record.args)

        return json.dumps(log_record)


def setup_logger():
    logger = logging.getLogger(settings.title)
    logger.setLevel(logging.INFO)

    # Avoid multiple headers
    if logger.hasHandlers():
        return logger

    log_group = settings.cloud_watch_log_group
    region_name = settings.aws_region

    # CloudWatch handler
    cloudwatch_handler = watchtower.CloudWatchLogHandler(
        log_group=log_group,
        stream_name=f"{datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')}",
        boto3_session=boto3.Session(region_name=region_name),
    )

    formatter = JsonFormatter(datefmt="%Y-%m-%d %H:%M:%S")
    cloudwatch_handler.setFormatter(formatter)

    logger.addHandler(cloudwatch_handler)

    return logger
