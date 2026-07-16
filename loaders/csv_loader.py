import csv
from pathlib import Path
from models.job import Job


class CSVLoader:
    """Load AI job postings from a CSV file."""

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self) -> list[Job]:
        """Load jobs from a CSV file."""

        jobs: list[Job] = []

        with self.file_path.open(
            mode="r",
            encoding="utf-8",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                jobs.append(self._create_job(row))
        return jobs

    def _create_job(self, row) -> Job:
        job = Job(
            # ---------- Identity ----------
            job_id=row["job_id"],
            title=row["job_title"],
            category=row["job_category"],

            # ---------- Location ----------
            city=row["city"],
            country=row["country"],

            # ---------- Experience ----------
            experience_level=row["experience_level"],
            years_of_experience=int(row["years_of_experience"]),
            education=row["education_required"],

            # ---------- Salary ----------
            salary=float(row["annual_salary_usd"]),
            salary_min=float(row["salary_min_usd"]),
            salary_max=float(row["salary_max_usd"]),
            salary_tier=row["salary_tier"],

            # ---------- Company ----------
            company_size=row["company_size"],
            industry=row["industry"],

            # ---------- Skills ----------
            skills=self._parse_skills(row["required_skills"]),

            # ---------- Market Metrics ----------
            salary_premium=float(row["ai_salary_premium_pct"]),
            demand_score=float(row["demand_score"]),
            demand_growth=float(row["demand_growth_yoy_pct"]),
            benefits_score=float(row["benefits_score_10"]),

            # ---------- Posting ----------
            posting_year=int(row["posting_year"]),
            posting_month=int(row["posting_month"]),

            # ---------- Flags ----------
            remote_work=row["remote_work"].strip(),
            is_senior=self._to_bool(row["is_senior"]),
            is_remote_friendly=self._to_bool(
                row["is_remote_friendly"]),
            is_llm_role=self._to_bool(row["is_llm_role"]),
        )
        return job

    def _parse_skills(self, value: str) -> list[str]:
        """Convert a comma-separated string into a list of skills."""
        if not value:
            return []
        return [
            skill.strip() for skill in value.split("|")
        ]

    def _to_bool(self, value: str) -> bool:
        """Convert different text values to bool."""
        return str(value).strip().lower() in {
            "true",
            "yes",
            "1"
        }
