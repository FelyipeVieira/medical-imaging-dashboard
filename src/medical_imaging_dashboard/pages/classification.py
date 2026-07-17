"""Classification, AI prediction, and model comparison page."""

import pandas as pd
import plotly.express as px
import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render prediction probabilities, comparison, and explainability hooks."""
    render_header("Classification & AI Predictions", "PyTorch/MONAI provider interface")
    frame = pd.DataFrame(
        {"class": ["Class A", "Class B", "Class C"], "probability": [0.72, 0.19, 0.09]}
    )
    st.plotly_chart(
        px.bar(frame, x="class", y="probability", range_y=[0, 1]),
        use_container_width=True,
    )
    st.warning(
        "Demonstration values only. Register a validated model provider for inference."
    )
    tabs = st.tabs(["Attention / Grad-CAM", "Model comparison", "Quality metrics"])
    tabs[0].info(
        "Attention-map and Grad-CAM overlays are exposed through prediction plugins."
    )
    tabs[1].dataframe(
        pd.DataFrame(columns=["model", "AUC", "sensitivity", "specificity"])
    )
    tabs[2].write(
        "PSNR, SSIM, SNR, contrast and artifact metrics can be added per modality."
    )
