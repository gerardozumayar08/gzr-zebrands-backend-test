from sqlalchemy.orm import registry

from app.src.catalogs.domain.product import Product
from app.src.catalogs.infrastructure.tables.products_table import products_table


def products_mapper(mapper_registry: registry):
    mapper_registry.map_imperatively(
        Product,
        products_table,
    )
