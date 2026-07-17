"""Project, citation, privacy, and license page."""

import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render publication and responsible-use information."""
    render_header("About")
    st.markdown(
        "**medical-imaging-dashboard** is an open-source research and "
        "education platform."
    )
    st.warning(
        "Not a certified medical device. Validate all algorithms independently "
        "before clinical translation."
    )
    st.markdown("Citation metadata: `CITATION.cff`  \nLicense: MIT")
