"""Application logging configuration."""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure timestamped structured-enough console logging."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
