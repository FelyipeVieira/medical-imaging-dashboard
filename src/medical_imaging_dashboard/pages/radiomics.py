"""Radiomics feature analysis page."""

import pandas as pd
import streamlit as st

from medical_imaging_dashboard.components.header import render_header
from medical_imaging_dashboard.visualization.heatmap import correlation_heatmap


def render() -> None:
    """Render uploaded feature tables, statistics, and heatmaps."""
    render_header(
        "Radiomics & Feature Visualization",
        "Compatible with radiomics-pipeline exports",
    )
    upload = st.file_uploader("Feature CSV", type=["csv"])
    if upload is None:
        st.info(
            "Upload a radiomics feature table to explore distributions and "
            "correlations."
        )
        return
    frame = pd.read_csv(upload)
    st.dataframe(frame.describe(include="all").transpose(), use_container_width=True)
    numeric = frame.select_dtypes("number")
    if numeric.shape[1] >= 2:
        st.plotly_chart(correlation_heatmap(numeric), use_container_width=True)
