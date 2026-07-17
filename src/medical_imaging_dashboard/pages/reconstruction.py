"""CT and 3D reconstruction page."""

import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render reconstruction controls and volume-backend status."""
    render_header("3D Reconstruction", "Volume rendering and surface extraction")
    st.selectbox("Rendering", ["Volume", "Iso-surface", "MIP", "MinIP"])
    st.select_slider("Quality", ["Interactive", "Balanced", "Publication"])
    st.info(
        "Install the `volume` extra for PyVista/VTK rendering. The viewer "
        "remains usable without GPU dependencies."
    )
