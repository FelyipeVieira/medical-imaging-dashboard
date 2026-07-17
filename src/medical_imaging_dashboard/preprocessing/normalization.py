"""Image intensity normalization."""

import numpy as np
import numpy.typing as npt


def z_score(pixels: npt.NDArray[np.generic]) -> npt.NDArray[np.float32]:
    """Return zero-mean, unit-variance pixels."""
    values = np.asarray(pixels, dtype=np.float32)
    deviation = float(values.std())
    if deviation == 0:
        return np.zeros_like(values)
    return (values - float(values.mean())) / deviation
