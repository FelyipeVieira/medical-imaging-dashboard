"""Application footer component."""

import streamlit as st


def render_footer() -> None:
    """Render the research-use and privacy notice."""
    st.divider()
    st.caption(
        "Research and education use • Not a certified medical device • "
        "Do not upload PHI to untrusted deployments"
    )
