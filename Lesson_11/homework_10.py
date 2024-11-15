"""Homework 11.1.

You and your team are developing a system login for a web application,
and you need to implement tests for the login function.
Given a function, write a set of tests for it.
"""

import logging


def log_event(username: str, status: str):
    """Login event logging.

    Args:
        username (str): The user name that logs in to the system.
        status (str): Login event status:

    * success - successful, logs in at info level
    * expired - the password is out of date and should be replaced,
                logs at the warning level
    * failed  - the password is incorrect, it is logged at the error level
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Logger creation and configuring
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s')
    logger = logging.getLogger('log_event')

    # Event logging
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)
