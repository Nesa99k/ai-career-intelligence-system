from models.job import Job
from collections import Counter
from collections import defaultdict


class DatasetAnalyzer:
    """Analyze AI job postings."""

    def __init__(self, jobs: list[Job]):
        self.jobs = jobs

#     --------------------------------------------------------
#                       (Dataset Overview)
#     --------------------------------------------------------

    # ---------- total_jobs Method ----------
    def total_jobs(self) -> int:
        """Return total number of jobs."""
        return len(self.jobs)

    # ---------- average_salary Method ---------

    def average_salary(self) -> float:
        """Return average annual salary."""
        total = sum(
            job.salary
            for job in self.jobs
        )
        return total/len(self.jobs)

    # ---------- highest_paying_jobs Method ---------

    def highest_paying_jobs(self, limit: int = 5) -> list[dict]:
        """Return the highest-paying jobs."""

        unique_jobs = {
            (job.title, job.country, job.salary): job
            for job in self.jobs
        }

        sorted_jobs = sorted(
            unique_jobs.values(),
            key=lambda job: job.salary,
            reverse=True
        )

        return [
            {
                "title": job.title,
                "country": job.country,
                "salary": job.salary
            }
            for job in sorted_jobs[:limit]
        ]

#       --------------------------------------------------------
#                        (Market Analysis)
#       --------------------------------------------------------

    # ---------- jobs_by_country Method ---------

    def jobs_by_country(self, limit: int = 10) -> list[tuple[str:int]]:
        """ Return countries with the most AI job postings."""
        counter = Counter(job.country for job in self.jobs)
        return counter.most_common(limit)

    # ---------- jobs_by_category Method ---------

    def jobs_by_category(self, limit: int = 10) -> list[tuple[str, int]]:
        """Return the most common AI job categories."""
        counter = Counter(job.category for job in self.jobs)
        return counter.most_common(limit)

    # ---------- titles_by_category Method --------------

    def titles_by_category(self) -> list[tuple[str, list[str]]]:
        """Return job titles grouped by category."""

        categories = defaultdict(set)

        for job in self.jobs:
            categories[job.category].add(job.title)

        result = []
        for category, titles in categories.items():
            result.append(
                (
                    category,
                    sorted(titles)
                )
            )
        return sorted(
            result,
            key=lambda item: item[0]
        )

    # ---------- remote_work_distribution Method ---------

    def remote_work_distribution(self) -> list[tuple[str, float]]:
        """Return percentage of remote jobs."""
        counter = Counter(job.remote_work for job in self.jobs)
        total = len(self.jobs)

        distribution = [
            (
                work_type,
                (count / total) * 100
            )
            for work_type, count in counter.items()
        ]
        return sorted(
            distribution,
            key=lambda item: item[1],
            reverse=True
        )


#       --------------------------------------------------------
#                        (AI Skills Analysis)
#       --------------------------------------------------------

    # ---------- most_common_skills Method ---------

    def most_common_skills(self, limit: int = 10) -> list[tuple[str, int]]:
        """Return the most common skills across all jobs."""

        counter = Counter()

        for job in self.jobs:
            counter.update(job.skills)
        return counter.most_common(limit)

    # ---------- skill_frequency Method ---------

    def skill_frequency(self, skill: str) -> int:
        """Return how many jobs require a specific skill."""

        return sum(skill in job.skills for job in self.jobs)

    # ---------- top_llm_skills Method ---------

    def top_llm_skills(self, limit: int = 10) -> list[tuple[str, int]]:
        """Return the most common skills for LLM jobs."""

        counter = Counter()

        for job in self.jobs:
            if job.is_llm_role:
                counter.update(job.skills)
        return counter.most_common(limit)


#       --------------------------------------------------------
#                        (Salary Analysis)
#       --------------------------------------------------------

    # ---------- average_salary_by_country Method ---------


    def average_salary_by_country(self) -> list[tuple[str, float]]:
        """Return average salary grouped by country."""
        salaries = defaultdict(list)

        for job in self.jobs:
            salaries[job.country].append(job.salary)

        averages = {
            country: sum(values) / len(values)
            for country, values in salaries.items()
        }

        return sorted(
            averages.items(),
            key=lambda item: item[1],
            reverse=True
        )

    # ---------- average_salary_by_category Method ---------

    def average_salary_by_category(self) -> list[tuple[str, float]]:
        """Return average salary grouped by category."""
        salaries = defaultdict(list)

        for job in self.jobs:
            salaries[job.category].append(job.salary)

        averages = {
            category: sum(values)/len(values)
            for category, values in salaries.items()
        }

        return sorted(
            averages.items(),
            key=lambda item: item[1],
            reverse=True
        )

    # ---------- salary_by_experience Method ---------

    def salary_by_experience(self) -> list[tuple[str, float]]:
        """Return average salary grouped by experience level."""
        salaries = defaultdict(list)

        for job in self.jobs:
            salaries[job.experience_level].append(job.salary)

        averages = {
            level: sum(values) / len(values)
            for level, values in salaries.items()
        }
        return sorted(
            averages.items(),
            key=lambda item: item[1],
            reverse=True

        )

#       --------------------------------------------------------
#                        (Demand Analysis)
#       --------------------------------------------------------

    # ---------- llm_jobs_percentage Method ---------

    def llm_jobs_percentage(self) -> float:
        """Return percentage of LLM jobs."""
        llm_jobs = sum(job.is_llm_role for job in self.jobs)
        return (llm_jobs/len(self.jobs))*100

    # ---------- top_demand_jobs Method ---------

    def top_demand_jobs(self, limit: int = 10) -> list[dict]:
        """Return jobs with the highest demand."""

        unique_jobs = {
            (job.title, job.country): job
            for job in self.jobs
        }

        sorted_jobs = sorted(
            unique_jobs.values(),
            key=lambda job: job.demand_score,
            reverse=True
        )

        return [
            {
                "title": job.title,
                "country": job.country,
                "demand_score": job.demand_score
            }
            for job in sorted_jobs[:limit]
        ]

    # ---------- average_demand_score Method ---------

    def average_demand_score(self) -> float:
        """Return average market demand score."""

        return (
            sum(job.demand_score for job in self.jobs)/len(self.jobs)
        )

#       --------------------------------------------------------
#                        (Education Analysis)
#       --------------------------------------------------------

    # ---------- education_distribution Method ---------

    def education_distribution(self) -> list[tuple[str, int]]:
        """Return the number of jobs for each education level."""

        counter = Counter(
            job.education
            for job in self.jobs
        )
        return counter.most_common()

    # ---------- average_salary_by_education Method ---------

    def average_salary_by_education(self) -> list[tuple[str, float]]:
        """Return average salary for each education level."""
        salaries = defaultdict(list)

        for job in self.jobs:
            salaries[job.education].append(job.salary)
            averages = {

                education:

                sum(values) / len(values)

                for education, values
                in salaries.items()

            }
        return sorted(

            averages.items(),

            key=lambda item: item[1],

            reverse=True

        )
