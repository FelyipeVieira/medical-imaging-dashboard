"""Unified image-loading facade with metadata preservation."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import cv2
import numpy as np
import numpy.typing as npt
import SimpleITK as sitk

from medical_imaging_dashboard.exceptions import ImageLoadError
from medical_imaging_dashboard.io.dicom import DicomService


@dataclass(slots=True)
class MedicalImage:
    """Loaded medical image and source context.

    Example:
        >>> item = MedicalImage(sitk.Image(4, 4, sitk.sitkUInt8), "png")
        >>> item.array.shape
        (4, 4)
    """

    image: sitk.Image
    format: str
    source: Path | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def array(self) -> npt.NDArray[np.generic]:
        """Return image pixels in NumPy axis order."""
        return sitk.GetArrayFromImage(self.image)


class ImageLoader:
    """Load supported clinical and conventional image formats.

    Example:
        >>> volume = ImageLoader().load("scan.nii.gz")  # doctest: +SKIP
    """

    def load(self, source: str | Path) -> MedicalImage:
        """Load a path as DICOM, NIfTI, PNG, TIFF, or JPEG."""
        path = Path(source)
        if path.is_dir():
            return MedicalImage(DicomService().read_series(path), "dicom", path)
        if not path.exists():
            raise ImageLoadError(f"Source does not exist: {path}")
        name = path.name.lower()
        if name.endswith((".nii", ".nii.gz")):
            try:
                return MedicalImage(sitk.ReadImage(str(path)), "nifti", path)
            except RuntimeError as error:
                raise ImageLoadError(f"Invalid NIfTI image: {path}") from error
        if path.suffix.lower() in {".png", ".tif", ".tiff", ".jpg", ".jpeg"}:
            pixels = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
            if pixels is None:
                raise ImageLoadError(f"Unable to decode raster image: {path}")
            if pixels.ndim == 3:
                pixels = cv2.cvtColor(pixels, cv2.COLOR_BGR2RGB)
                image = sitk.GetImageFromArray(pixels, isVector=True)
            else:
                image = sitk.GetImageFromArray(pixels)
            return MedicalImage(image, path.suffix[1:].lower(), path)
        if name == "dicomdir":
            raise ImageLoadError("Use DicomService.dicomdir_records for DICOMDIR")
        try:
            return MedicalImage(
                sitk.ReadImage(str(path)), "dicom", path, DicomService().metadata(path)
            )
        except RuntimeError as error:
            raise ImageLoadError(f"Unsupported or invalid image: {path}") from error
