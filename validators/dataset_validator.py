from models.job import Job


class DatasetValidator:
    """
    Validate a list of Job objects.
    """

    def validate(self, jobs: list[Job]) -> None:
        """Validate the dataset."""
        self._check_not_empty(jobs)
        self._check_salary(jobs)
        self._check_posting_year(jobs)
        self._check_title(jobs)

    # ---------- _check_not_empty Method ----------

    def _check_not_empty(self, jobs: list[Job]) -> None:
        """Ensure the dataset is not empty."""
        if not jobs:
            raise ValueError("Dataset is empty.")

    # ---------- _check_salary Method ----------

    def _check_salary(self, jobs: list[Job]) -> None:
        """Ensure salaries are valid."""
        for job in jobs:
            if job.salary < 0:
                raise ValueError(f"Negative salary found: {job.title}")

    # ---------- _check_salary Method ----------

    def _check_posting_year(self, jobs: list[Job]) -> None:
        """Validate posting year."""

        for job in jobs:
            if not (2020 <= job.posting_year <= 2030):
                raise ValueError(f"Invalid year: {job.posting_year}")

    # ---------- _check_salary Method ----------
    def _check_title(self, jobs: list[Job]) -> None:
        """Ensure every job has a title."""
        for job in jobs:
            if not job.title.strip():
                raise ValueError("Empty job title found.")
