"""Report generation page."""

import pandas as pd
import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render patient/session/radiomics report configuration and exports."""
    render_header("Report Generator", "PDF • CSV • Excel • JSON • HTML • PNG")
    report_type = st.selectbox("Report", ["Session", "Patient", "Radiomics"])
    st.checkbox("Remove identifying metadata", value=True)
    st.text_area("Clinical/research notes")
    st.dataframe(
        pd.DataFrame(
            {
                "section": ["Study", "Images", "Results", "Provenance"],
                "included": [True] * 4,
            }
        ),
        hide_index=True,
    )
    st.button(f"Generate {report_type} report", type="primary")
