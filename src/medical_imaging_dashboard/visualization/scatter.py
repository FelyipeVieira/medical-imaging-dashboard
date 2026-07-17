"""Interactive feature scatter plots."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def scatter(frame: pd.DataFrame, x: str, y: str, color: str | None = None) -> go.Figure:
    """Plot two feature columns with an optional group color."""
    return px.scatter(frame, x=x, y=y, color=color)
