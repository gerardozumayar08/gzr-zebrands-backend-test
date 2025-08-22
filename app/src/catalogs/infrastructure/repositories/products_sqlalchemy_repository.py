from typing import Optional, Tuple, List

from sqlalchemy import select

from sqlalchemy import func
from sqlalchemy.sql.selectable import Select

from app.src.catalogs.domain.repositories.products_repository import ProductsRepository
from app.src.catalogs.domain.product import Product
from app.src.shared.infrastructure.repositories.base_sqlalchemy_repository import (
    BaseSqlAlchemyRepository,
)


class ProductsSQLAlchemyRepository(BaseSqlAlchemyRepository, ProductsRepository):
    async def get_by(self, id: int) -> Optional[Product]:
        query = select(Product).where(Product.id == id)
        return self.session.execute(query).scalar()

    async def save(self, entity: Product):
        self.session.add(entity)
        self.session.flush()

    async def update(self, entity: Product):
        self.session.add(entity)

    async def get_all(
        self,
    ) -> Tuple[List[Product], int]:
        query = select(Product)
        num_rows = await self.count_rows(query)
        rows = self.session.execute(query).scalars().all()
        return rows, num_rows

    async def count_rows(self, query: Select):
        numero_registros = select(func.count()).select_from(query.subquery())
        return self.session.execute(numero_registros).scalar_one()
    
    async def delete(self, entity: Product):
        self.session.delete(entity)
