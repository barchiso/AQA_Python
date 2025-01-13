"""Fixtures and setup code for the test suite."""
import logging
import os

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8080'
USERNAME = 'test_user'  # Moved to constants
# Default password if not set
PASSWORD = os.getenv('TEST_PASSWORD', 'test_pass')


def _send_request(method, endpoint, auth=None, timeout=5, headers=None,
                  **kwargs):
    """Send HTTP requests with consistent error handling.

    Args:
        method (str): HTTP method (e.g., 'GET', 'POST').
        endpoint (str): The endpoint of the API to request.
        auth (tuple or None): Optional authentication tuple for basic auth.
        timeout (int, optional): Timeout in seconds for the request.
        headers (dict, optional): Optional headers to send with the request.
        kwargs: Additional parameters to pass to the request method.

    Returns:
        dict: JSON response if available.
    """
    url = f'{BASE_URL}{endpoint}'
    try:
        response = requests.request(
            method,
            url,
            timeout=timeout,
            auth=auth,
            headers=headers,
            **kwargs,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        error_message = f'Request to {url} timed out.'
        return pytest.fail(error_message)
    except requests.exceptions.HTTPError as http_err:
        error_message = f'HTTP error occurred: {http_err}'
        return pytest.fail(error_message)
    except requests.exceptions.RequestException as req_err:
        error_message = f'Request error occurred: {req_err}'
        return pytest.fail(error_message)


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    """Set up logging to both console and file.

    Returns:
        logging.Logger: A logger configured to log to both console and a file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('test_search.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Return the logger in case tests need to use it
    return logger


@pytest.fixture(scope='class')
def auth_session():
    """Fixture to authenticate and get an access token.

    Yields:
        requests.Session: A session with the Authorization header set to
                          'Bearer <access_token>' for authenticated requests.
    """
    auth_response = _send_request(
        'POST',
        '/auth',
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
    )

    # Extract token from response and create a session
    token = auth_response['access_token']

    # Create a session and set the authorization header
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token}'})

    yield session

    # Cleanup: Close the session after the test
    if 'session' in locals():
        session.close()
