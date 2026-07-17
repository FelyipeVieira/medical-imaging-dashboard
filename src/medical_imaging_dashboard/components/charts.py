"""Shared Plotly chart display component."""

from typing import Any

import streamlit as st


def render_chart(figure: Any) -> None:
    """Render an interactive chart with PNG export and responsive sizing."""
    st.plotly_chart(
        figure,
        use_container_width=True,
        config={"toImageButtonOptions": {"format": "png"}},
    )
