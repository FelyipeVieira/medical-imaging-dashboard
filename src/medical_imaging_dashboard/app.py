"""Streamlit application entry point and page router."""

from collections.abc import Callable

import streamlit as st

from medical_imaging_dashboard.components.footer import render_footer
from medical_imaging_dashboard.components.sidebar import render_sidebar
from medical_imaging_dashboard.pages import (
    about,
    classification,
    dicom_viewer,
    home,
    patient_browser,
    radiomics,
    reconstruction,
    reports,
    segmentation,
    settings,
)
from medical_imaging_dashboard.session import DashboardSession


def run() -> None:
    """Configure Streamlit, initialize session state, and render a page."""
    st.set_page_config(
        page_title="Medical Imaging Dashboard",
        page_icon="🩻",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    if "dashboard" not in st.session_state:
        st.session_state.dashboard = DashboardSession()
    pages: dict[str, Callable[[], None]] = {
        "Home": home.render,
        "Patient & Study Explorer": patient_browser.render,
        "Medical Image Viewer": dicom_viewer.render,
        "Segmentation & ROI": segmentation.render,
        "Classification & AI": classification.render,
        "Radiomics & Statistics": radiomics.render,
        "3D Reconstruction": reconstruction.render,
        "Reports": reports.render,
        "Settings & Plugins": settings.render,
        "About": about.render,
    }
    selected = render_sidebar(list(pages))
    try:
        pages[selected]()
    except Exception as error:
        st.error(f"The selected module could not complete: {error}")
        st.exception(error)
    render_footer()


if __name__ == "__main__":
    run()
