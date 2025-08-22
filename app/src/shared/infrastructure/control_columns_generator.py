from datetime import datetime

from sqlalchemy import Column, DateTime, String


def date_control_columns_generator():
    return [
        Column(
            "created_at",
            DateTime(timezone=True),
            default=datetime.now,
        ),
        Column(
            "updated_at",
            DateTime(timezone=True),
            default=datetime.now,
            onupdate=datetime.now,
        ),
    ]


def user_control_columns_generator():
    return [
        Column("created_by", String(128)),
        Column("modified_by", String(128)),
    ]


def location_control_columns_generator():
    return [
        Column("user_latitude", String(24)),
        Column("user_longitude", String(24)),
    ]
