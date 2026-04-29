from __future__ import annotations

from collections import defaultdict
from datetime import date

from services.finance_service import FinanceService


class StatisticsService:
    def __init__(self, finance_service: FinanceService | None = None):
        self.finance_service = finance_service or FinanceService()

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _filter_by_date(self, records, date_attr: str, start: date | None, end: date | None):
        """Return records whose `date_attr` falls within [start, end] (inclusive)."""
        result = []
        for record in records:
            rec_date = getattr(record, date_attr)
            if start is not None and rec_date < start:
                continue
            if end is not None and rec_date > end:
                continue
            result.append(record)
        return result

    def _sum_field(self, records, field: str) -> float:
        return sum(getattr(r, field) for r in records)

    # ------------------------------------------------------------------
    # Totals
    # ------------------------------------------------------------------

    def total_income(self, start_date: date | None = None, end_date: date | None = None) -> float:
        records = self._filter_by_date(
            self.finance_service.get_all_income(), "income_date", start_date, end_date
        )
        return self._sum_field(records, "income_money")

    def total_expense(self, start_date: date | None = None, end_date: date | None = None) -> float:
        records = self._filter_by_date(
            self.finance_service.get_all_expense(), "expenses_date", start_date, end_date
        )
        return self._sum_field(records, "expenses_money")

    def net_balance(self, start_date: date | None = None, end_date: date | None = None) -> float:
        return self.total_income(start_date, end_date) - self.total_expense(start_date, end_date)

    # ------------------------------------------------------------------
    # Grouped by category
    # ------------------------------------------------------------------

    def income_by_category(self, start_date: date | None = None, end_date: date | None = None) -> dict[str, float]:
        records = self._filter_by_date(
            self.finance_service.get_all_income(), "income_date", start_date, end_date
        )
        totals: dict[str, float] = defaultdict(float)
        for r in records:
            totals[r.income_category] += r.income_money
        return dict(totals)

    def expense_by_category(self, start_date: date | None = None, end_date: date | None = None) -> dict[str, float]:
        records = self._filter_by_date(
            self.finance_service.get_all_expense(), "expenses_date", start_date, end_date
        )
        totals: dict[str, float] = defaultdict(float)
        for r in records:
            totals[r.expenses_category] += r.expenses_money
        return dict(totals)

    # ------------------------------------------------------------------
    # Grouped by month
    # ------------------------------------------------------------------

    def income_by_month(self, year: int | None = None) -> dict[str, float]:
        records = self.finance_service.get_all_income()
        if year is not None:
            records = [r for r in records if r.income_date.year == year]
        totals: dict[str, float] = defaultdict(float)
        for r in records:
            key = r.income_date.strftime("%Y-%m")
            totals[key] += r.income_money
        return dict(totals)

    def expense_by_month(self, year: int | None = None) -> dict[str, float]:
        records = self.finance_service.get_all_expense()
        if year is not None:
            records = [r for r in records if r.expenses_date.year == year]
        totals: dict[str, float] = defaultdict(float)
        for r in records:
            key = r.expenses_date.strftime("%Y-%m")
            totals[key] += r.expenses_money
        return dict(totals)

    # ------------------------------------------------------------------
    # Averages
    # ------------------------------------------------------------------

    def average_income(self, start_date: date | None = None, end_date: date | None = None) -> float:
        records = self._filter_by_date(
            self.finance_service.get_all_income(), "income_date", start_date, end_date
        )
        if not records:
            return 0.0
        return self._sum_field(records, "income_money") / len(records)

    def average_expense(self, start_date: date | None = None, end_date: date | None = None) -> float:
        records = self._filter_by_date(
            self.finance_service.get_all_expense(), "expenses_date", start_date, end_date
        )
        if not records:
            return 0.0
        return self._sum_field(records, "expenses_money") / len(records)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self, start_date: date | None = None, end_date: date | None = None) -> dict:
        income_records = self._filter_by_date(
            self.finance_service.get_all_income(), "income_date", start_date, end_date
        )
        expense_records = self._filter_by_date(
            self.finance_service.get_all_expense(), "expenses_date", start_date, end_date
        )

        total_inc = self._sum_field(income_records, "income_money")
        total_exp = self._sum_field(expense_records, "expenses_money")
        income_count = len(income_records)
        expense_count = len(expense_records)

        return {
            "total_income": total_inc,
            "total_expense": total_exp,
            "net_balance": total_inc - total_exp,
            "income_count": income_count,
            "expense_count": expense_count,
            "average_income": total_inc / income_count if income_count else 0.0,
            "average_expense": total_exp / expense_count if expense_count else 0.0,
        }
