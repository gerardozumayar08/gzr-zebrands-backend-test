from sqlalchemy import Integer, Column, String, Table, Enum, ForeignKey

from app.src.shared.infrastructure.control_columns_generator import (
    date_control_columns_generator,
    user_control_columns_generator,
)
from app.src.shared.infrastructure.mapper_registry import mapper_registry


roles_table = Table(
    "roles",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(128)),
)

role_permissions_table = Table(
    "role_permissions",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)
