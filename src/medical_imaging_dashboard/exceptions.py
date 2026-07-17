"""Application-specific exception hierarchy."""


class DashboardError(Exception):
    """Base error for controlled dashboard failures."""


class ImageLoadError(DashboardError):
    """Raised when a medical image cannot be loaded or validated."""


class PluginError(DashboardError):
    """Raised when plugin discovery or execution fails."""
