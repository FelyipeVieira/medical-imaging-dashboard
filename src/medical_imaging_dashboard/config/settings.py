"""Typed application configuration."""

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    """Validated runtime settings.

    Example:
        >>> settings = AppSettings(theme="dark")
        >>> settings.page_title
        'Medical Imaging Dashboard'
    """

    page_title: str = "Medical Imaging Dashboard"
    theme: Literal["light", "dark", "system"] = "system"
    data_directory: Path = Path("data")
    output_directory: Path = Path("outputs")
    anonymize_exports: bool = True
    max_upload_mb: int = Field(default=500, ge=1)
    cache_ttl_seconds: int = Field(default=3600, ge=0)
