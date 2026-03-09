"""
Logging system for platform
"""

import logging
import os


def setup_logger(name="systems_biology_logger"):

    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "platform.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()
