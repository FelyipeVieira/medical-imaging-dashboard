"""Application settings and plugin manager page."""

import streamlit as st

from medical_imaging_dashboard.components.header import render_header
from medical_imaging_dashboard.plugins.manager import PluginManager


def render() -> None:
    """Render appearance, storage, privacy, caching, and plugin settings."""
    render_header("Settings & Plugin Manager")
    st.selectbox("Appearance", ["System", "Light", "Dark"])
    st.number_input("Cache TTL (seconds)", min_value=0, value=3600)
    st.checkbox("Anonymize all exports", value=True)
    st.subheader("Installed plugins")
    try:
        plugins = PluginManager().discover()
        st.write(
            [{"name": item.name, "version": item.version} for item in plugins]
            or "No external plugins installed."
        )
    except Exception as error:
        st.error(str(error))
