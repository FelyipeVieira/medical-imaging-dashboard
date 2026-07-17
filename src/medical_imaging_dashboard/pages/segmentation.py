"""Segmentation and ROI visualization page."""

import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render segmentation framework integration status and ROI tools."""
    render_header("Segmentation & ROI", "Binary/multiclass masks and MONAI adapters")
    st.info(
        "Load an image and mask through a registered segmentation plugin "
        "or prediction provider."
    )
    st.file_uploader("Mask overlay", type=["nii", "gz", "dcm", "png", "tif"])
    st.multiselect(
        "Visible labels", ["Background", "ROI 1", "ROI 2"], default=["ROI 1"]
    )
    st.slider("Overlay opacity", 0.0, 1.0, 0.45)
