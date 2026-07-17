"""Application header component."""

import streamlit as st


def render_header(title: str, subtitle: str = "") -> None:
    """Render a consistent page heading and optional subtitle."""
    st.title(title)
    if subtitle:
        st.caption(subtitle)
