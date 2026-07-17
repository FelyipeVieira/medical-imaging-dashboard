"""Reusable secure-upload guidance component."""

import streamlit as st


def render_upload_notice() -> None:
    """Remind users to upload only approved de-identified data."""
    st.caption("Upload only de-identified data approved for this environment.")
