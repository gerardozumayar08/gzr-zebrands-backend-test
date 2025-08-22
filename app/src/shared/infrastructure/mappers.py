from functools import lru_cache

from app.src.catalogs.infrastructure.mappers.products import products_mapper
from app.src.iam.infrastructure.mappers.permissions import permissions_mapper
from app.src.iam.infrastructure.mappers.roles import roles_mapper
from app.src.iam.infrastructure.mappers.users import users_mapper
from app.src.catalogs.infrastructure.mappers.product_views import product_views_mapper
from app.src.shared.infrastructure.mapper_registry import mapper_registry


@lru_cache(maxsize=None)
def start_mappers():
    permissions_mapper(mapper_registry)
    roles_mapper(mapper_registry)
    users_mapper(mapper_registry)
    products_mapper(mapper_registry)
    product_views_mapper(mapper_registry)

    return mapper_registry
