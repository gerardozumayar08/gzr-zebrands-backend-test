from sqlalchemy.orm import Session


class BaseSqlAlchemyRepository:
    def __init__(self, session: Session):
        self.session = session
