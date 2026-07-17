"""Sidebar navigation and appearance controls."""

import os

import streamlit as st


def render_sidebar(pages: list[str]) -> str:
    """Render navigation, search, and global display preferences."""
    st.sidebar.title("MedImaging")
    st.sidebar.text_input("Search studies", placeholder="Patient, study, modality…")
    requested = os.getenv("MEDICAL_IMAGING_DEFAULT_PAGE", pages[0])
    index = pages.index(requested) if requested in pages else 0
    page = st.sidebar.radio("Navigation", pages, index=index)
    st.sidebar.selectbox("Theme", ["System", "Light", "Dark"])
    st.sidebar.caption("v0.1.0")
    return page
