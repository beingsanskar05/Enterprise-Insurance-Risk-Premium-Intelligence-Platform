"""
Central Logger
Enterprise Insurance Risk & Premium Intelligence Platform
"""

import logging

LOGGER_NAME = "EIRPI"

logger = logging.getLogger(LOGGER_NAME)

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)