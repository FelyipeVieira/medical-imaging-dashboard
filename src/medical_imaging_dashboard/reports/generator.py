"""Portable report generation for dashboard data."""

import json
from pathlib import Path
from typing import Any

import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


class ReportGenerator:
    """Export structured results to common research formats.

    Example:
        >>> report = ReportGenerator(pd.DataFrame({"feature": [1.0]}))
        >>> report.to_csv("outputs/report.csv")
    """

    def __init__(
        self, data: pd.DataFrame, metadata: dict[str, Any] | None = None
    ) -> None:
        """Create a report with optional de-identified context."""
        self.data = data.copy()
        self.metadata = metadata or {}

    def _path(self, path: str | Path) -> Path:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        return destination

    def to_csv(self, path: str | Path) -> Path:
        """Export tabular data to CSV."""
        destination = self._path(path)
        self.data.to_csv(destination, index=False)
        return destination

    def to_excel(self, path: str | Path) -> Path:
        """Export data and metadata to an Excel workbook."""
        destination = self._path(path)
        with pd.ExcelWriter(destination) as writer:
            self.data.to_excel(writer, sheet_name="data", index=False)
            pd.DataFrame(self.metadata.items(), columns=["key", "value"]).to_excel(
                writer, sheet_name="metadata", index=False
            )
        return destination

    def to_json(self, path: str | Path) -> Path:
        """Export metadata and records to JSON."""
        destination = self._path(path)
        payload = {
            "metadata": self.metadata,
            "records": self.data.to_dict(orient="records"),
        }
        destination.write_text(
            json.dumps(payload, indent=2, default=str), encoding="utf-8"
        )
        return destination

    def to_html(self, path: str | Path, title: str = "Medical Imaging Report") -> Path:
        """Export a self-contained HTML report."""
        destination = self._path(path)
        metadata = pd.DataFrame(self.metadata.items(), columns=["Field", "Value"])
        destination.write_text(
            f"<html><body><h1>{title}</h1>{metadata.to_html(index=False)}{self.data.to_html(index=False)}</body></html>",
            encoding="utf-8",
        )
        return destination

    def to_pdf(self, path: str | Path, title: str = "Medical Imaging Report") -> Path:
        """Export a concise PDF summary without embedding identifying pixels."""
        destination = self._path(path)
        canvas = Canvas(str(destination), pagesize=A4)
        canvas.setTitle(title)
        canvas.drawString(50, 800, title)
        y = 775
        for key, value in self.metadata.items():
            canvas.drawString(50, y, f"{key}: {value}"[:110])
            y -= 18
        canvas.drawString(
            50, y - 10, f"Rows: {len(self.data)} | Columns: {len(self.data.columns)}"
        )
        canvas.save()
        return destination
