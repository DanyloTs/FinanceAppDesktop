from repository_pattern.repo_interface import RepositoryInterface
from database.engine import SessionLocal
from database.income_model import Income

class IncomeRepository(RepositoryInterface):
    ALLOWED_UPDATE_FIELDS = frozenset({"income_category", "income_money", "income_date"})

    def __init__(self) -> None:
        self.session = SessionLocal()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_all(self):
        return self.session.query(Income).all()

    def update(self, entity_id, **kwargs):
        for key in kwargs:
            if key not in self.ALLOWED_UPDATE_FIELDS:
                raise ValueError(f"Field '{key}' is not allowed to be updated")
        obj = self.session.get(Income, entity_id)
        if obj is None:
            raise LookupError(f"Income with id {entity_id} not found")
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()

    def delete(self, entity_id):
        obj = self.session.get(Income, entity_id)
        if obj is None:
            raise LookupError(f"Income with id {entity_id} not found")
        self.session.delete(obj)
        self.session.commit()

    
    