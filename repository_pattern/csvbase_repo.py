import csv
from pathlib import Path
from repository_pattern.repo_interface import RepositoryInterface

_CSV_INJECTION_PREFIXES = ("=", "+", "-", "@", "\t", "\r")

def _sanitize_csv_value(value):
    """Escape values to prevent CSV/formula injection (CWE-1236).

    If the stringified value starts with a character a spreadsheet
    application may interpret as a formula, prepend a single quote.
    """
    if value is None:
        return value
    text = str(value)
    if text.startswith(_CSV_INJECTION_PREFIXES):
        return "'" + text
    return text

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
            safe_entity = {k: _sanitize_csv_value(v) for k, v in entity.items()}
            writer.writerow(safe_entity)

    def get_all(self):
        with open(self.file_path, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def update(self, entity_id, **kwargs):
        for key in kwargs:
            if key == "id" or key not in self.fieldnames:
                raise ValueError(f"Field '{key}' is not allowed to be updated")
        rows = self.get_all()
        updated = False
        for row in rows:
            if row["id"] == str(entity_id):
                safe_kwargs = {k: _sanitize_csv_value(v) for k, v in kwargs.items()}
                row.update(safe_kwargs)
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


