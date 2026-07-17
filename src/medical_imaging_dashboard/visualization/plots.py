"""Interactive Plotly medical-image figures."""

import numpy as np
import numpy.typing as npt
import plotly.express as px
import plotly.graph_objects as go


def image_figure(
    pixels: npt.NDArray[np.generic],
    mask: npt.NDArray[np.generic] | None = None,
    title: str = "Medical image",
) -> go.Figure:
    """Create a zoomable/pannable grayscale image with optional ROI contour."""
    figure = px.imshow(pixels, color_continuous_scale="gray", aspect="equal")
    figure.update_layout(title=title, coloraxis_showscale=False, dragmode="pan")
    if mask is not None:
        figure.add_trace(
            go.Contour(
                z=np.asarray(mask),
                contours={"start": 0.5, "end": 0.5, "size": 1},
                line={"color": "#00ff88", "width": 2},
                showscale=False,
                hoverinfo="skip",
            )
        )
    return figure


def histogram(pixels: npt.NDArray[np.generic], bins: int = 100) -> go.Figure:
    """Create an interactive intensity histogram."""
    return px.histogram(
        x=np.asarray(pixels).ravel(), nbins=bins, labels={"x": "Intensity"}
    )
