"""Interactive medical image viewer page."""

import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import numpy as np
import streamlit as st

from medical_imaging_dashboard.components.header import render_header
from medical_imaging_dashboard.components.metrics import render_image_metrics
from medical_imaging_dashboard.exceptions import DashboardError
from medical_imaging_dashboard.io.loaders import ImageLoader, MedicalImage
from medical_imaging_dashboard.preprocessing.windowing import apply_window
from medical_imaging_dashboard.visualization.plots import histogram, image_figure
from medical_imaging_dashboard.visualization.volume import project, slice_at


def _uploaded_image() -> MedicalImage | None:
    """Persist an upload temporarily and decode it through the unified loader."""
    example_path = os.getenv("MEDICAL_IMAGING_EXAMPLE_PATH")
    if example_path:
        source = Path(example_path)
        if source.exists():
            st.caption(f"Example study: {source.name} · NSCLC-Radiomics")
            return ImageLoader().load(source)
        st.warning(f"Example study path does not exist: {source}")
    upload = st.file_uploader(
        "Upload image", type=["dcm", "nii", "gz", "png", "tif", "tiff", "jpg", "jpeg"]
    )
    if upload is None:
        return None
    suffix = (
        ".nii.gz"
        if upload.name.lower().endswith(".nii.gz")
        else Path(upload.name).suffix
    )
    with NamedTemporaryFile(delete=False, suffix=suffix) as temporary:
        temporary.write(upload.getbuffer())
        path = Path(temporary.name)
    image = ImageLoader().load(path)
    image.source = Path(upload.name)
    return image


def render() -> None:
    """Render slice navigation, MPR, projections, W/L, zoom, and pan."""
    render_header("Medical Image Viewer", "DICOM • NIfTI • PNG • TIFF • JPEG")
    try:
        loaded = _uploaded_image()
    except DashboardError as error:
        st.error(str(error))
        return
    if loaded is None:
        st.info("Upload a de-identified image to begin.")
        return
    pixels = loaded.array
    render_image_metrics(pixels)
    mode = st.segmented_control(
        "View", ["Slice", "MIP", "MinIP", "Average"], default="Slice"
    )
    axis = st.selectbox(
        "Plane", ["axial", "coronal", "sagittal"], disabled=pixels.ndim < 3
    )
    if pixels.ndim >= 3 and mode == "Slice":
        axis_number = {"axial": 0, "coronal": 1, "sagittal": 2}[axis]
        index = st.slider(
            "Slice", 0, pixels.shape[axis_number] - 1, pixels.shape[axis_number] // 2
        )
        view = slice_at(pixels, axis, index)
    elif pixels.ndim >= 3:
        method = {"MIP": "maximum", "MinIP": "minimum", "Average": "average"}[mode]
        view = project(pixels, method)
    else:
        view = pixels
    minimum, maximum = float(np.min(view)), float(np.max(view))
    default_level = (
        float(np.clip(-600.0, minimum, maximum))
        if loaded.format == "dicom"
        else float((minimum + maximum) / 2)
    )
    level = (
        st.slider("Window level", minimum, maximum, default_level)
        if maximum > minimum
        else minimum
    )
    available_width = max(1.0, maximum - minimum)
    default_width = (
        min(1500.0, available_width)
        if loaded.format == "dicom"
        else available_width
    )
    width = st.slider(
        "Window width", 1.0, available_width, default_width
    )
    adjusted = apply_window(view, level, width)
    st.plotly_chart(
        image_figure(adjusted, title=f"{mode} • {axis}"),
        use_container_width=True,
        config={"scrollZoom": True, "toImageButtonOptions": {"format": "png"}},
    )
    with st.expander("Intensity distribution"):
        st.plotly_chart(histogram(view), use_container_width=True)
    st.session_state.dashboard.add_recent(loaded.source or Path("uploaded-image"))
