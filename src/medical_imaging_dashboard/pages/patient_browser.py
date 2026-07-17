"""Patient, study, and series browser page."""

from pathlib import Path

import pandas as pd
import streamlit as st

from medical_imaging_dashboard.components.header import render_header


def render() -> None:
    """Render searchable local study records and favorites."""
    render_header("Patient & Study Explorer", "Use de-identified identifiers only")
    root = Path(st.text_input("Study directory", "data"))
    query = st.text_input("Filter", placeholder="Name, modality, identifier…").lower()
    records = []
    if root.exists():
        for path in list(root.iterdir())[:500]:
            if not query or query in path.name.lower():
                records.append(
                    {
                        "study": path.name,
                        "path": str(path),
                        "type": "directory" if path.is_dir() else path.suffix,
                    }
                )
    st.dataframe(pd.DataFrame(records), use_container_width=True, hide_index=True)
    st.caption(
        "PACS/RIS and FHIR adapters can implement the same browser contract "
        "in future releases."
    )
