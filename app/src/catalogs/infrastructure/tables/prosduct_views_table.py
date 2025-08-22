from sqlalchemy import Column, ForeignKey, Integer, Table

from app.src.shared.infrastructure.control_columns_generator import (
    date_control_columns_generator,
    user_control_columns_generator,
)
from app.src.shared.infrastructure.mapper_registry import mapper_registry

product_views_table = Table(
    "product_views",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("product_id", Integer, ForeignKey("products.id"), nullable=False),
)
