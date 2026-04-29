from repository_pattern.repo_interface import RepositoryInterface
from database.expenses_model import Expense
from database.engine import SessionLocal


class ExpenseRepository(RepositoryInterface):
    ALLOWED_UPDATE_FIELDS = frozenset({"expenses_category", "expenses_money", "expenses_date"})

    def __init__(self):
        self.session = SessionLocal()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_all(self):
        return self.session.query(Expense).all()

    def update(self, entity_id, **kwargs):
        for key in kwargs:
            if key not in self.ALLOWED_UPDATE_FIELDS:
                raise ValueError(f"Field '{key}' is not allowed to be updated")
        obj = self.session.get(Expense, entity_id)
        if obj is None:
            raise LookupError(f"Expense with id {entity_id} not found")
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()

    def delete(self, entity_id):
        obj = self.session.get(Expense, entity_id)
        if obj is None:
            raise LookupError(f"Expense with id {entity_id} not found")
        self.session.delete(obj)
        self.session.commit()