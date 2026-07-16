"""
Job
│
├── Attributes
│
├── summary()
│
├── has_skill()
│
├── salary_range()
│
├── is_high_paying()
│
├── __str__()
│
└── __repr__()
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Job:

    """
    Represents a single AI job posting.
    """

    # ---------- Identity ----------
    job_id: str
    title: str
    category: str

    # ---------- Location ----------
    city: str
    country: str
    # ---------- Experience ----------
    experience_level: str
    years_of_experience: int
    education: str
    # ---------- Salary ----------
    salary: float
    salary_min: float
    salary_max: float
    salary_tier: str
    # ---------- Company ----------
    company_size: str
    industry: str
    # ---------- Skills ----------
    skills: list[str]

    # ---------- Market Metrics ----------
    salary_premium: float
    demand_score: float
    demand_growth: float
    benefits_score: float
    # ---------- Posting ----------
    posting_year: int
    posting_month: int

    # ---------- Flags ----------
    remote_work: str
    is_senior: bool
    is_remote_friendly: bool
    is_llm_role: bool

    # ---------- Summary method ----------

    def summary(self) -> str:
        """Return a short summary of the job."""
        return (
            f"{self.title}|"
            f"{self.country}|"
            f"{self.salary:,.0f}"
        )

    # ---------- Has_skill method ----------

    def has_skill(self, skill: str) -> bool:
        """Check whether a required skill exists."""
        return skill.lower() in (item.lower() for item in self.skills)

    # ---------- Salary_range method ----------

    def salary_range(self) -> str:
        """Return the salary range."""
        return (
            f"${self.salary_min:,.0f}"
            f"${self.salary_max:,.0f}"
        )
    # ---------- Is_high_paying method ----------

    def is_high_paying(self, threshold: float = 180000) -> bool:
        """Return True if salary is above the threshold."""
        return self.salary >= threshold
    # ---------- __str__ Magic Method ----------

    def __str__(self) -> str:
        """Human-readable representation."""
        return (
            f"{self.title} | "
            f"{self.country} | "
            f"${self.salary:,.0f}"
        )
    # ---------- __repr__ Magic Method ----------

    def __repr__(self):
        """Developer-friendly representation."""
        return (
            f"Job("
            f"title='{self.title}', "
            f"country='{self.country}', "
            f"salary={self.salary:,.0f}"
            f")"
        )
