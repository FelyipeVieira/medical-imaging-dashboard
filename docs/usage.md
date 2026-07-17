# Usage

Run `streamlit run src/app.py`, upload a de-identified image, select the plane and
slice, then adjust window and level. Plotly toolbar actions export PNG figures;
scroll zoom and pan are enabled. Feature CSV files can be analyzed on the
Radiomics page.

For local DICOM studies, point Patient & Study Explorer at a controlled data
directory. Production deployments should replace local discovery with an
authenticated PACS/DICOMweb adapter.

