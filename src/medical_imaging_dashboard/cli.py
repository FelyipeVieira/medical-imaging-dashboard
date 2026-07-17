"""Command-line launcher for the Streamlit dashboard."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Launch Streamlit with the packaged application entry point."""
    app = Path(__file__).with_name("app.py")
    raise SystemExit(
        subprocess.call([sys.executable, "-m", "streamlit", "run", str(app)])
    )


if __name__ == "__main__":
    main()
