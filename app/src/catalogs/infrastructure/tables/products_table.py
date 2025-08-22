from sqlalchemy import Column, Integer, Numeric, String, Table

from app.src.shared.infrastructure.control_columns_generator import (
    date_control_columns_generator,
    user_control_columns_generator,
)
from app.src.shared.infrastructure.mapper_registry import mapper_registry

products_table = Table(
    "products",
    mapper_registry.metadata,
    *date_control_columns_generator(),
    *user_control_columns_generator(),
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(128), unique=True, index=True),
    Column("name", String(128)),
    Column("price", Numeric(16, 4)),
    Column("brand", String(128)),
)
