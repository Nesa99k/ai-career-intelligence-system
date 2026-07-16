from pathlib import Path
import csv
import json


class ReportExporter:
    """Export analysis reports to different formats."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(self, report: dict) -> None:
        with (self.output_dir/"report.json").open(
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(report, file, indent=4, ensure_ascii=False)

    def export_csv(self, report: dict) -> None:
        with (self.output_dir / "report.csv").open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["Section", "Metric", "Value"])

            for section, metrics in report.items():
                for key, value in metrics.items():
                    writer.writerow([
                        section,
                        key,
                        str(value)
                    ])

    def export_markdown(self, report: dict) -> None:

        with (self.output_dir / "report.md").open(
            "w",
            encoding="utf-8"
        ) as file:

            file.write("# AI Career Intelligence Report\n\n")

            for section, metrics in report.items():

                file.write(f"## {section}\n\n")

                for key, value in metrics.items():

                    file.write(
                        f"- **{key}** : {value}\n"
                    )

                file.write("\n")
