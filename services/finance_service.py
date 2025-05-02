from database.income_model import Income
from database.expenses_model import Expense
from repository_pattern.expenses_repo import ExpenseRepository
from repository_pattern.income_repo import IncomeRepository
from datetime import date

class FinanceService:
    def __init__(self):
        self.income_repo = IncomeRepository()
        self.expense_repo = ExpenseRepository()

    def add_income(self, source: str, amount: float, d: date):
        income = Income(income_category=source, income_money=amount, income_date=d)
        self.income_repo.add(income)

    def add_expense(self, category: str, amount: float, d: date):
        expense = Expense(expenses_category=category, expenses_money=amount, expenses_date=d)
        self.expense_repo.add(expense)

    def get_all_income(self):
        return self.income_repo.get_all()

    def get_all_expense(self):
        return self.expense_repo.get_all()

    def update_income(self, id: int, **kwargs):
        self.income_repo.update(id, **kwargs)

    def delete_income(self, id: int):
        self.income_repo.delete(id)

    def update_expense(self, id: int, **kwargs):
        self.expense_repo.update(id, **kwargs)

    def delete_expense(self, id: int):
        self.expense_repo.delete(id)
