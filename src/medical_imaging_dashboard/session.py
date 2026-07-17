"""Serializable dashboard session state."""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path


@dataclass(slots=True)
class DashboardSession:
    """Track current data, favorites, bookmarks, and recent studies.

    Example:
        >>> session = DashboardSession()
        >>> session.add_recent(Path("study"))
        >>> len(session.recent_studies)
        1
    """

    current_image: Path | None = None
    current_mask: Path | None = None
    favorites: set[str] = field(default_factory=set)
    bookmarks: dict[str, str] = field(default_factory=dict)
    recent_studies: list[str] = field(default_factory=list)
    history: list[str] = field(default_factory=list)

    def add_recent(self, path: Path) -> None:
        """Move a study to the front of the bounded recent list."""
        value = str(path)
        self.recent_studies = [
            value,
            *[item for item in self.recent_studies if item != value],
        ][:20]
        self.history.append(f"{datetime.now(UTC).isoformat()} opened {value}")

    def toggle_favorite(self, identifier: str) -> bool:
        """Toggle a favorite and return its new state."""
        if identifier in self.favorites:
            self.favorites.remove(identifier)
            return False
        self.favorites.add(identifier)
        return True
