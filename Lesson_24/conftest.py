"""Fixtures and setup code for the test suite."""

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8080'


@pytest.fixture(scope='class')
def auth_token():
    """Fixture to authenticate and get an access token.

    Yields:
        requests.Session: A session with the Authorization header set to
                          'Bearer <access_token>' for authenticated requests.
    """
    try:
        # Make the authentication request
        response = requests.post(
            f'{BASE_URL}/auth',
            auth=HTTPBasicAuth('test_user', 'test_pass'),
            timeout=5,
        )
        response.raise_for_status()

        # Extract token from response and create a session
        token = response.json()['access_token']
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {token}'})

        yield session

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
