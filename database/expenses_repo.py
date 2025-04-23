from repo_interface import RepositoryInterface
from expenses_model import Expense
from database.engine import SessionLocal


class ExpenseRepository(RepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_all(self):
        return self.session.query(Expense).all()

    def update(self, entity_id, **kwargs):
        obj = self.session.query(Expense).get(entity_id)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()

    def delete(self, entity_id):
        obj = self.session.query(Expense).get(entity_id)
        self.session.delete(obj)
        self.session.commit()