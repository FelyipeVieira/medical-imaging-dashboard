"""Volume slicing, MPR, and projection calculations."""

from typing import Literal

import numpy as np
import numpy.typing as npt

Axis = Literal["axial", "coronal", "sagittal"]
Projection = Literal["maximum", "minimum", "average"]


def slice_at(
    volume: npt.NDArray[np.generic], axis: Axis, index: int
) -> npt.NDArray[np.generic]:
    """Extract an axial, coronal, or sagittal slice from ``(z, y, x)`` data."""
    if volume.ndim == 2:
        return volume
    axes = {"axial": 0, "coronal": 1, "sagittal": 2}
    selected_axis = axes[axis]
    maximum = volume.shape[selected_axis] - 1
    if not 0 <= index <= maximum:
        raise IndexError(f"Slice {index} outside 0..{maximum}")
    return np.take(volume, index, axis=selected_axis)


def project(
    volume: npt.NDArray[np.generic], method: Projection, axis: int = 0
) -> npt.NDArray[np.generic]:
    """Compute maximum, minimum, or average intensity projection."""
    if method == "maximum":
        return np.max(volume, axis=axis)
    if method == "minimum":
        return np.min(volume, axis=axis)
    return np.mean(volume, axis=axis)
