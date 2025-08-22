from sqlalchemy import Integer, Column, String, Table, Boolean, ForeignKey

from app.src.shared.infrastructure.control_columns_generator import (
    date_control_columns_generator,
    user_control_columns_generator,
)
from app.src.shared.infrastructure.mapper_registry import mapper_registry


users_table = Table(
    "users",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, unique=True, index=True),
    Column("fullname", String),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String),
    Column("is_active", Boolean, default=True),
)

user_roles_table = Table(
    "user_roles",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)
