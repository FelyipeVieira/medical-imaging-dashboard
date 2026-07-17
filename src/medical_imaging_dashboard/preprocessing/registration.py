"""Registration extension interface."""

from typing import Protocol

import SimpleITK as sitk


class RegistrationBackend(Protocol):
    """Contract implemented by future registration algorithms.

    Example:
        >>> backend.register(fixed, moving)  # doctest: +SKIP
    """

    def register(self, fixed: sitk.Image, moving: sitk.Image) -> sitk.Image:
        """Register moving data onto the fixed physical grid."""
        ...
