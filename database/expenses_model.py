from sqlalchemy import Column, Date, Float, String, Date, Integer
from database.engine import Base


class Expense(Base):
    __tablename__ = "expenses"
    idexpenses = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    expenses_category = Column(String, nullable=False)
    expenses_money = Column(Float, nullable=False)
    expenses_date = Column(Date, nullable=False)
