"""Feature and radiomics heatmap visualization."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def correlation_heatmap(features: pd.DataFrame) -> go.Figure:
    """Plot numeric feature correlations."""
    return px.imshow(
        features.corr(numeric_only=True),
        zmin=-1,
        zmax=1,
        color_continuous_scale="RdBu_r",
    )
