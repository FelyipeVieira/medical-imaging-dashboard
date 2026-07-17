"""Raster image export utilities."""

from pathlib import Path

import cv2
import numpy as np
import numpy.typing as npt


def save_png(array: npt.NDArray[np.generic], path: str | Path) -> Path:
    """Normalize an array and save it as an eight-bit PNG figure."""
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    values = np.asarray(array, dtype=float)
    minimum, maximum = values.min(), values.max()
    scaled = (
        np.zeros(values.shape, dtype=np.uint8)
        if maximum == minimum
        else ((values - minimum) * 255 / (maximum - minimum)).astype(np.uint8)
    )
    if not cv2.imwrite(str(destination), scaled):
        raise OSError(f"Could not write PNG: {destination}")
    return destination
