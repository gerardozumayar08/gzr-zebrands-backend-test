from typing import List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.sql.selectable import Select

from app.src.catalogs.domain.product_view import ProductView
from app.src.catalogs.domain.repositories.product_views_repository import (
    ProductViewsRepository,
)
from app.src.shared.infrastructure.repositories.base_sqlalchemy_repository import (
    BaseSqlAlchemyRepository,
)


class ProductViewsSQLAlchemyRepository(BaseSqlAlchemyRepository, ProductViewsRepository):
    async def get_by(self, id: int) -> Optional[ProductView]:
        query = select(ProductView).where(ProductView.id == id)
        return self.session.execute(query).scalar()

    async def save(self, entity: ProductView):
        self.session.add(entity)
        self.session.flush()

    async def update(self, entity: ProductView):
        self.session.add(entity)

    async def get_all(
        self,
    ) -> Tuple[List[ProductView], int]:
        query = select(ProductView)
        num_rows = await self.count_rows(query)
        rows = self.session.execute(query).scalars().all()
        return rows, num_rows

    async def count_rows(self, query: Select):
        numero_registros = select(func.count()).select_from(query.subquery())
        return self.session.execute(numero_registros).scalar_one()

    async def save_row(self, product_id, user_id):
        self.session.add(ProductView(product_id=product_id, user_id=user_id))
        self.session.flush()
