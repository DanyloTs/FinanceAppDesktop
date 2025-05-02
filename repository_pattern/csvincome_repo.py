from repository_pattern.csvbase_repo import CSVRepositoryBase

class CSVIncomeRepository(CSVRepositoryBase):
    def __init__(self):
        super().__init__(
            file_path="csv/income.csv",
            fieldnames=["id", "source", "amount", "date"]
        )
