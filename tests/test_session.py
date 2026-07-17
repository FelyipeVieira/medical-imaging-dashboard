"""Session history and favorite tests."""

from pathlib import Path

from medical_imaging_dashboard.session import DashboardSession


def test_recent_studies_are_unique() -> None:
    """Opening the same study moves it instead of duplicating it."""
    session = DashboardSession()
    session.add_recent(Path("one"))
    session.add_recent(Path("one"))
    assert session.recent_studies == ["one"]


def test_favorite_toggle() -> None:
    """Favorite toggle reports and changes state."""
    session = DashboardSession()
    assert session.toggle_favorite("study") is True
    assert session.toggle_favorite("study") is False
