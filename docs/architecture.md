# Architecture

The interface layer contains Streamlit pages and reusable components. Domain
services own IO, preprocessing, visualization, reports, session state, and error
semantics. Integration protocols accept external classification, segmentation,
radiomics, and future foundation-model implementations. Plugins are discovered
through Python package entry points.

Heavy dependencies are extras: the base dashboard supports 2D/MPR workflows;
`ai` provides PyTorch/MONAI/PyRadiomics and `volume` provides PyVista/VTK.
Separating these environments improves startup time and deployment portability.

