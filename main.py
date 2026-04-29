from services.finance_service import FinanceService
from services.statistics_service import StatisticsService
from datetime import date


if __name__ == "__main__":
    fs = FinanceService()
    stats = StatisticsService(fs)
