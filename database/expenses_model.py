from sqlalchemy import Column, Date, Float, String, Date, Integer
from engine import Base


class Income(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    expenses_category = Column(String, nullable=False)
    expenses_money = Column(Float, nullable=False)
    expenses_date = Column(Date, nullable=False)
