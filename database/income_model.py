from sqlalchemy import Column, Date, Float, String, Date, Integer
from database.engine import Base


class Income(Base):
    __tablename__ = "income"
    idincome = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    income_category = Column(String, nullable=False)
    income_money = Column(Float, nullable=False)
    income_date = Column(Date, nullable=False)
