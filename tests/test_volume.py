"""Slice and projection tests."""

import numpy as np

from medical_imaging_dashboard.visualization.volume import project, slice_at


def test_slice_axes() -> None:
    """MPR planes select their documented array axes."""
    volume = np.arange(24).reshape(2, 3, 4)
    assert slice_at(volume, "axial", 1).shape == (3, 4)
    assert slice_at(volume, "coronal", 1).shape == (2, 4)
    assert slice_at(volume, "sagittal", 1).shape == (2, 3)


def test_projections() -> None:
    """Projection methods aggregate along the selected axis."""
    volume = np.arange(8).reshape(2, 2, 2)
    assert np.array_equal(project(volume, "maximum"), np.max(volume, axis=0))
    assert np.array_equal(project(volume, "minimum"), np.min(volume, axis=0))
    assert np.array_equal(project(volume, "average"), np.mean(volume, axis=0))
