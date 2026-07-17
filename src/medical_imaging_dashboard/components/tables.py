"""Shared searchable table component."""

import pandas as pd
import streamlit as st


def render_table(frame: pd.DataFrame) -> None:
    """Render a responsive dataframe without its numeric index."""
    st.dataframe(frame, use_container_width=True, hide_index=True)
