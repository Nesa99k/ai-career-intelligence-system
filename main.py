from pathlib import Path

from analyzers.dataset_analyzer import DatasetAnalyzer
from loaders.csv_loader import CSVLoader
from validators.dataset_validator import DatasetValidator
from exporters.report_exporter import ReportExporter


# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).parent
DATASET_PATH = (
    BASE_DIR
    / "data"
    / "raw"
    / "ai_jobs_market_2025_2026.csv"
)


# =====================================================
# Load Dataset
# =====================================================

loader = CSVLoader(DATASET_PATH)
jobs = loader.load()


# =====================================================
# Validate Dataset
# =====================================================

validator = DatasetValidator()
validator.validate(jobs)

print("Dataset validation passed.")


# =====================================================
# Analyze Dataset
# =====================================================

analyzer = DatasetAnalyzer(jobs)

report = {

    "dataset_overview": {

        "total_jobs": analyzer.total_jobs(),

        "average_salary": analyzer.average_salary(),

        "highest_paying_jobs": analyzer.highest_paying_jobs()
    },

    "market_analysis": {

        "jobs_by_country": analyzer.jobs_by_country(),

        "jobs_by_category": analyzer.jobs_by_category(),

        "remote_work_distribution": analyzer.remote_work_distribution(),

        "titles_by_category": analyzer.titles_by_category(),

    },

    "skills_analysis": {

        "most_common_skills": analyzer.most_common_skills(),

        "python_jobs": analyzer.skill_frequency("Python"),

        "top_llm_skills": analyzer.top_llm_skills()

    },

    "salary_analysis": {

        "average_salary_by_country": analyzer.average_salary_by_country(),

        "average_salary_by_category": analyzer.average_salary_by_category(),

        "salary_by_experience": analyzer.salary_by_experience()

    },

    "demand_analysis": {

        "top_demand_jobs": analyzer.top_demand_jobs(),

        "average_demand_score": analyzer.average_demand_score(),

        "llm_jobs_percentage": analyzer.llm_jobs_percentage()

    },

    "education_analysis": {

        "education_distribution": analyzer.education_distribution(),

        "average_salary_by_education": analyzer.average_salary_by_education()
    }

}


# =====================================================
# Display Report
# =====================================================

print()
print("=" * 60)
print("AI CAREER INTELLIGENCE REPORT")
print("=" * 60)
print()


# -----------------------------------------------------
# Dataset Overview
# -----------------------------------------------------

overview = report["dataset_overview"]

print()
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print()

print(f"Total Jobs      : {overview['total_jobs']}")
print(f"Average Salary  : ${overview['average_salary']:,.0f}")

print()
print("-" * 40)
print("Top Paying Jobs")
print("-" * 40)
print()

for job in overview["highest_paying_jobs"]:
    print(job)

# -----------------------------------------------------
# Market Analysis
# -----------------------------------------------------

market = report["market_analysis"]

print()
print("=" * 60)
print("MARKET ANALYSIS")
print("=" * 60)

print()
print("-" * 40)
print("Top Countries")
print("-" * 40)
print()

for country, count in market["jobs_by_country"]:
    print(f"{country:<20}{count}")

print()
print("-" * 40)
print("Top Categories")
print("-" * 40)
print()

for category, count in market["jobs_by_category"]:
    print(f"{category:<20}{count}")

print()
print("-" * 40)
print("Remote Work Distribution")
print("-" * 40)
print()

for work_type, percentage in market["remote_work_distribution"]:
    print(f"{work_type:<20}{percentage:.1f}%")

print()
print("-" * 40)
print("Job Titles By Category")
print("-" * 40)
print()

for category, titles in market["titles_by_category"]:
    print()
    print(category)

    for title in titles:
        print(f"   • {title}")

# -----------------------------------------------------
# Skills Analysis
# -----------------------------------------------------

skills = report["skills_analysis"]

print()
print("=" * 60)
print("SKILLS ANALYSIS")
print("=" * 60)
print()

print("-" * 40)
print("Most Common Skills")
print("-" * 40)
print()

for skill, count in skills["most_common_skills"]:
    print(f"{skill:<25}{count}")

print()

print(f"Python Jobs : {skills['python_jobs']}")

print()
print("-" * 40)
print("Top LLM Skills")
print("-" * 40)
print()

for skill, count in skills["top_llm_skills"]:
    print(f"{skill:<25}{count}")

# -----------------------------------------------------
# Salary Analysis
# -----------------------------------------------------

salary = report["salary_analysis"]

print()
print("=" * 60)
print("SALARY ANALYSIS")
print("=" * 60)
print()

print("-" * 40)
print("Average Salary By Country")
print("-" * 40)
print()

for country, avg_salary in salary["average_salary_by_country"]:
    print(f"{country:<20}${avg_salary:,.0f}")

print()
print("-" * 40)
print("Average Salary By Category")
print("-" * 40)
print()

for category, avg_salary in salary["average_salary_by_category"]:
    print(f"{category:<20}${avg_salary:,.0f}")

print()
print("-" * 40)
print("Average Salary By Experience")
print("-" * 40)
print()


for level, avg_salary in salary["salary_by_experience"]:
    print(f"{level:<20}${avg_salary:,.0f}")


# -----------------------------------------------------
# Demand Analysis
# -----------------------------------------------------

demand = report["demand_analysis"]

print()
print("=" * 60)
print("DEMAND ANALYSIS")
print("=" * 60)
print()

print(
    f"Average Demand Score : "
    f"{demand['average_demand_score']:.1f}"
)

print()

print(
    f"LLM Jobs Percentage : "
    f"{demand['llm_jobs_percentage']:.1f}%"
)

print()
print("-" * 40)
print("Top Demand Jobs")
print("-" * 40)
print()

for job in demand["top_demand_jobs"]:
    print(job)

# -----------------------------------------------------
# Education Analysis
# -----------------------------------------------------

education = report["education_analysis"]

print()
print("=" * 60)
print("EDUCATION ANALYSIS")
print("=" * 60)

print()
print("-" * 40)
print("Education Distribution")
print("-" * 40)
print()


for education_level, count in education["education_distribution"]:
    print(f"{education_level:<25} {count}")

print()
print("-" * 40)
print("Average Salary By Education")
print("-" * 40)
print()

for education_level, salary in education["average_salary_by_education"]:
    print(f"{education_level:<25}${salary:,.0f}")

exporter = ReportExporter(
    BASE_DIR/"reports"
)
exporter.export_json(report)
exporter.export_csv(report)
exporter.export_markdown(report)

print()
print("Reports exported successfully.")
