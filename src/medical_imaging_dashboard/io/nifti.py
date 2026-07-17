"""NIfTI compatibility helpers."""

from pathlib import Path

import SimpleITK as sitk


def save_nifti(image: sitk.Image, path: str | Path) -> None:
    """Write an image and physical geometry to a compressed NIfTI file."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    sitk.WriteImage(image, str(destination), True)
