"""Image summary metric cards."""

import numpy as np
import numpy.typing as npt
import streamlit as st


def render_image_metrics(pixels: npt.NDArray[np.generic]) -> None:
    """Render size, range, mean, and standard deviation cards."""
    columns = st.columns(4)
    columns[0].metric("Shape", " × ".join(map(str, pixels.shape)))
    columns[1].metric("Range", f"{pixels.min():.1f} – {pixels.max():.1f}")
    columns[2].metric("Mean", f"{pixels.mean():.2f}")
    columns[3].metric("Std", f"{pixels.std():.2f}")
