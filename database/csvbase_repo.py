import csv
from pathlib import Path
from database.repo_interface import RepositoryInterface

class CSVRepositoryBase(RepositoryInterface):
    def __init__(self, file_path, fieldnames):
        self.file_path = Path(file_path)
        self.fieldnames = fieldnames

        if not self.file_path.exists():
            with open(self.file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()

    def add(self, entity):
        with open(self.file_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(entity)

    def get_all(self):
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def update(self, entity_id, **kwargs):
        rows = self.get_all()
        updated = False
        for row in rows:
            if row["id"] == str(entity_id):
                row.update(kwargs)
                updated = True
        if updated:
            with open(self.file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                writer.writerows(rows)

    def delete(self, entity_id):
        rows = self.get_all()
        rows = [r for r in rows if r["id"] != str(entity_id)]
        with open(self.file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)


