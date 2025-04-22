from repo_interface import RepositoryInterface
from database import SessionLocal
from income_model import Income

class IncomeRepository(RepositoryInterface):
    def __init__(self) -> None:
        self.session = SessionLocal()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()