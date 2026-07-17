"""CT-style window and level transformations."""

import numpy as np
import numpy.typing as npt


def apply_window(
    pixels: npt.NDArray[np.generic], level: float, width: float
) -> npt.NDArray[np.float32]:
    """Clip pixels around level/width and normalize them to ``[0, 1]``."""
    if width <= 0:
        raise ValueError("Window width must be positive")
    lower, upper = level - width / 2, level + width / 2
    return np.asarray(
        np.clip((pixels - lower) / (upper - lower), 0, 1), dtype=np.float32
    )
