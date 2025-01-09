"""Fixtures and setup code for the test suite."""
import logging


import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8080'
USERNAME = 'test_user'  # Moved to constants
# Default password if not set
PASSWORD = 'test_pass'


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
    try:
        # Make the authentication request
        response = requests.post(
            f'{BASE_URL}/auth',
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=5,
        )
        response.raise_for_status()

        # Extract token from response and create a session
        try:
            token = response.json()['access_token']
        except KeyError:
            pytest.fail('Access token not found in authentication response.')

        # Create a session and set the authorization header
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {token}'})

        yield session

    except requests.exceptions.Timeout:
        # Explicit timeout handling
        pytest.fail('Authentication request timed out.')

    except requests.exceptions.HTTPError as http_err:
        error_msg = f'HTTP error occurred: {http_err}'
        pytest.fail(error_msg)  # Fail the test with the error message

    except requests.exceptions.RequestException as req_err:
        error_msg = f'Request error occurred: {req_err}'
        pytest.fail(error_msg)  # Fail the test with the error message

    finally:
        # Cleanup: Close the session after the test
        if 'session' in locals():
            session.close()
