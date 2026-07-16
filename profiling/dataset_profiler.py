from pathlib import Path
import csv


class DatasetProfiler:
    """Profile a CSV dataset."""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def _load_rows(self) -> list[dict]:
        """
        Read CSV file into memory.
        """
        with self.file_path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def profile(self) -> None:

        rows = self._load_rows()

        print("=" * 50)
        print("AI JOB DATASET PROFILE")
        print("=" * 50)

        print()

        print("Rows:")
        print(len(rows))

        print()

        print("Columns:")
        print(len(rows[0]))

        print()

        for column in rows[0]:
            self._profile_column(rows, column)

    def _profile_column(self, rows: list[dict], column: str):
        values = [
            row[column] for row in rows
        ]

        missing = sum(
            value.strip() == ""
            for value in values
        )
        unique = len(
            set(values)
        )

        print("-" * 50)

        print(column)

        print()

        print(f"Missing : {missing}")

        print(f"Unique  : {unique}")

        print()

        print("Examples:")

        for value in list(set(values))[:5]:
            print(value)

        print()
