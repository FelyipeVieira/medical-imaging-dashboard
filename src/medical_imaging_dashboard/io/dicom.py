"""DICOM series, DICOMDIR, and metadata readers."""

from pathlib import Path
from typing import Any

import pydicom
import SimpleITK as sitk

from medical_imaging_dashboard.exceptions import ImageLoadError


class DicomService:
    """Discover and read DICOM studies and series.

    Example:
        >>> service = DicomService()
        >>> ids = service.series_ids("data/study")  # doctest: +SKIP
    """

    def series_ids(self, directory: str | Path) -> list[str]:
        """Return series identifiers found under a directory."""
        return list(sitk.ImageSeriesReader.GetGDCMSeriesIDs(str(directory)) or [])

    def read_series(
        self, directory: str | Path, series_id: str | None = None
    ) -> sitk.Image:
        """Read one spatially sorted DICOM series."""
        identifiers = self.series_ids(directory)
        if not identifiers:
            raise ImageLoadError(f"No DICOM series found in {directory}")
        selected = series_id or identifiers[0]
        if selected not in identifiers:
            raise ImageLoadError(f"Unknown DICOM series: {selected}")
        files = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(str(directory), selected)
        reader = sitk.ImageSeriesReader()
        reader.SetFileNames(files)
        reader.MetaDataDictionaryArrayUpdateOn()
        try:
            return reader.Execute()
        except RuntimeError as error:
            raise ImageLoadError(f"Unable to read DICOM series: {error}") from error

    def metadata(self, path: str | Path) -> dict[str, Any]:
        """Return display-safe metadata from a DICOM instance."""
        dataset = pydicom.dcmread(str(path), stop_before_pixels=True, force=True)
        return {
            element.keyword or str(element.tag): str(element.value)
            for element in dataset
            if element.VR != "SQ"
        }

    def dicomdir_records(self, path: str | Path) -> list[dict[str, str]]:
        """Flatten patient, study, series, and image DICOMDIR records."""
        dataset = pydicom.dcmread(str(path))
        records = []
        for item in getattr(dataset, "DirectoryRecordSequence", []):
            records.append(
                {
                    "type": str(getattr(item, "DirectoryRecordType", "UNKNOWN")),
                    "patient_id": str(getattr(item, "PatientID", "")),
                    "study_id": str(getattr(item, "StudyID", "")),
                    "series_number": str(getattr(item, "SeriesNumber", "")),
                }
            )
        return records
