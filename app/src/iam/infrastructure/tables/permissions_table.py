from sqlalchemy import (
    Integer,
    Column,
    String,
    Table,
    Enum,
)

from app.src.shared.infrastructure.control_columns_generator import (
    date_control_columns_generator,
    user_control_columns_generator,
)
from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.shared.infrastructure.mapper_registry import mapper_registry


permissions_table = Table(
    "permissions",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("action", Enum(PermissionActionsEnum)),
    Column("resource", String(128)),
)
