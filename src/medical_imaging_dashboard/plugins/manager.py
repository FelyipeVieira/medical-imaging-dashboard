"""Entry-point-based dashboard plugin architecture."""

from importlib.metadata import entry_points
from typing import Protocol

from medical_imaging_dashboard.exceptions import PluginError


class DashboardPlugin(Protocol):
    """Contract implemented by third-party dashboard modules.

    Example:
        >>> plugin.render()  # doctest: +SKIP
    """

    name: str
    version: str
    description: str

    def render(self) -> None:
        """Render the plugin UI in the active Streamlit page."""
        ...


class PluginManager:
    """Discover plugins registered under the package entry-point group.

    Example:
        >>> plugins = PluginManager().discover()
    """

    group = "medical_imaging_dashboard.plugins"

    def discover(self) -> list[DashboardPlugin]:
        """Load all valid plugins without failing the entire application."""
        loaded: list[DashboardPlugin] = []
        for point in entry_points(group=self.group):
            try:
                plugin = point.load()()
                loaded.append(plugin)
            except Exception as error:
                raise PluginError(f"Plugin {point.name} could not be loaded") from error
        return loaded
