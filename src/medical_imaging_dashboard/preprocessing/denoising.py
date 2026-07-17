"""Edge-aware medical-image noise reduction."""

import SimpleITK as sitk


def denoise(image: sitk.Image, iterations: int = 5) -> sitk.Image:
    """Apply curvature-flow denoising."""
    return sitk.CurvatureFlow(
        sitk.Cast(image, sitk.sitkFloat32),
        timeStep=0.0625,
        numberOfIterations=iterations,
    )
