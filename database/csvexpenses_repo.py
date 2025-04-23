from database.csvbase_repo import CSVRepositoryBase

class CSVExpenseRepository(CSVRepositoryBase):
    def __init__(self):
        super().__init__(
            file_path="csv/expense.csv",
            fieldnames=["id", "category", "amount", "date"]
        )
