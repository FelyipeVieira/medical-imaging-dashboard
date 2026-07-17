"""Optional PyVista-based volume rendering."""

from typing import Any

import numpy as np
import numpy.typing as npt

from medical_imaging_dashboard.exceptions import DashboardError


def build_volume_grid(
    volume: npt.NDArray[np.generic], spacing: tuple[float, float, float]
) -> Any:
    """Create a PyVista image grid suitable for volume rendering."""
    try:
        import pyvista as pv
    except ImportError as error:
        raise DashboardError("Install medical-imaging-dashboard[volume]") from error
    grid = pv.ImageData()
    grid.dimensions = np.asarray(volume.shape[::-1]) + 1
    grid.spacing = spacing
    grid.cell_data["intensity"] = np.asarray(volume).flatten(order="C")
    return grid
