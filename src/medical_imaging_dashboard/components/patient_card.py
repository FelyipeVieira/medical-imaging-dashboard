"""Compact patient/study card component."""

import streamlit as st


def render_patient_card(identifier: str, modality: str, study_date: str) -> None:
    """Render a de-identified study summary card."""
    with st.container(border=True):
        st.subheader(identifier)
        st.caption(f"{modality} • {study_date}")
