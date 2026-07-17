"""Stable contracts for external AI and imaging frameworks."""

from typing import Any, Protocol

import numpy.typing as npt


class PredictionProvider(Protocol):
    """Classification or segmentation provider contract.

    Example:
        >>> result = provider.predict(volume)  # doctest: +SKIP
    """

    name: str

    def predict(self, image: npt.NDArray[Any]) -> dict[str, Any]:
        """Run inference and return serializable predictions."""
        ...


class FeatureProvider(Protocol):
    """Radiomics feature-provider contract.

    Example:
        >>> features = provider.extract(image, mask)  # doctest: +SKIP
    """

    name: str

    def extract(self, image: Any, mask: Any) -> dict[str, float]:
        """Extract named numeric features."""
        ...
