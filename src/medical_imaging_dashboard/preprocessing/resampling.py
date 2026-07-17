"""Image and mask resampling in physical space."""

import SimpleITK as sitk


def resample(
    image: sitk.Image, spacing: tuple[float, ...], is_mask: bool = False
) -> sitk.Image:
    """Resample an image to target spacing with mask-safe interpolation."""
    if len(spacing) != image.GetDimension() or any(item <= 0 for item in spacing):
        raise ValueError("Spacing must be positive and match image dimensions")
    size = [
        max(1, round(old_size * old_spacing / new_spacing))
        for old_size, old_spacing, new_spacing in zip(
            image.GetSize(), image.GetSpacing(), spacing, strict=True
        )
    ]
    return sitk.Resample(
        image,
        size,
        sitk.Transform(),
        sitk.sitkNearestNeighbor if is_mask else sitk.sitkLinear,
        image.GetOrigin(),
        spacing,
        image.GetDirection(),
        0.0,
        image.GetPixelID(),
    )
