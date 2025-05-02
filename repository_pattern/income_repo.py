from repository_pattern.repo_interface import RepositoryInterface
from database.engine import SessionLocal
from database.income_model import Income

class IncomeRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.session = SessionLocal()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()

    def get_all(self):
        return self.session.query(Income).all()

    def update(self, entity_id, **kwargs):
        obj = self.session.get(Income, entity_id)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        self.session.commit()


    def delete(self, entity_id):
        obj = self.session.query(Income).get(entity_id)
        self.session.delete(obj)
        self.session.commit()

    
    