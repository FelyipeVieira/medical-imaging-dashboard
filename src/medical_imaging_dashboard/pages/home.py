"""Dashboard home page."""

import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render overview, recent studies, and workflow entry points."""
    render_header(
        "Medical Imaging Dashboard",
        "Imaging, quantitative analysis and AI in one workspace",
    )
    left, middle, right = st.columns(3)
    left.metric("Active studies", len(st.session_state.dashboard.recent_studies))
    middle.metric("Favorites", len(st.session_state.dashboard.favorites))
    right.metric("Plugins", "Ready")
    st.subheader("Workflow")
    st.info(
        "Open an image in Medical Image Viewer, inspect metadata and ROI, "
        "then export a report."
    )
    st.subheader("Recent studies")
    recent = st.session_state.dashboard.recent_studies
    st.write(recent if recent else "No studies opened in this session.")
