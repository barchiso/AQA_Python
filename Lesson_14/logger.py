"""Create logger."""

import logging


def configure_logging():
    """Logger configuration.

    Returns:
        logging.Logger: Logging Logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(
        ('%(asctime)s. %(msecs)03d: %(module)-12s: '
         '%(lineno)3d %(levelname)-7s - %(message)s'),
        '%Y-%m-%d %H:%M:%S',
    )

    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    return logger
