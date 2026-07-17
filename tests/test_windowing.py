"""Window/level transformation tests."""

import numpy as np
import pytest

from medical_imaging_dashboard.preprocessing.windowing import apply_window


def test_window_clips_and_normalizes() -> None:
    """Values outside the selected window are clipped to zero and one."""
    output = apply_window(np.array([-100, 0, 100]), level=0, width=100)
    assert np.allclose(output, [0.0, 0.5, 1.0])


def test_window_rejects_invalid_width() -> None:
    """Nonpositive window width fails early."""
    with pytest.raises(ValueError):
        apply_window(np.array([1]), level=0, width=0)
