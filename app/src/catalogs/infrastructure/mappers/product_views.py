from sqlalchemy.orm import registry

from app.src.catalogs.domain.product_view import ProductView
from app.src.catalogs.infrastructure.tables.prosduct_views_table import product_views_table


def product_views_mapper(mapper_registry: registry):
    mapper_registry.map_imperatively(
        ProductView,
        product_views_table,
    )
