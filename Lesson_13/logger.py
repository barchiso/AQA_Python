"""Logger creation."""

import logging
from pathlib import Path


def configure_logging(log_file='01.log'):
    """Logger configuration.

    Returns:
        logging.Logger: Logging Logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a formatter for the logs
    log_formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d : %(module)-12s:%(lineno)3d'
        ' %(levelname)-7s - %(message)s',
        '%Y-%m-%d %H:%M:%S',
    )

    # Create a handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(log_formatter)

    # Create a handler for logging to file
    log_folder = Path("logs")
    log_folder.mkdir(parents=True, exist_ok=True)
    filename = log_folder / log_file
    file_handler = logging.FileHandler(filename, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
