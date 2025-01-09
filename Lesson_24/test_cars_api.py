"""Homework #24. Cars API search."""
# There is a Flask app that allows you to authenticate
# and then search for cars via a GET request.
# You need to organize testing of this app
# using parameterization(5-7 data sets) with different GET request
# parameters **sort_by** and **limit ** through Pytest.
# The test should use the **request** module.
# The initial authentication should be organized
# in the form of a **scope = 'class'** fixture.
# The test itself should be able to log not only to the console
# but also to the **test_search.log** file

# Initial data
# download the attached Flask app(backend API testing).txt file
# Starting the backend
# To run the Flask application, you first need to install Flask,
# using pip: **pip install Flask , pip install flask_jwt_extended**
# Open a command prompt or terminal,
# navigate to the folder where your Python file is located,
# and run the command: **python cars_app.py**
# This will run your app on port 8080
# and be accessible at http://127.0.0.1:8080/.
# Setting the debug=True flag
# will allow you to receive error messages in the browser during development.

# Flask app API doc
# The Flask API documentation for the above app:
# Authentication: URL: /auth  Method: POST
# Description:
# This endpoint is used to authenticate users and obtain an access token.
# Query parameters: username: Username, password: User password
# Response:
# Successful authentication returns a JSON object
#  with an access token: { 'access_token': '<access_token>' }

# Search for cars: URL: /cars, Method: GET
# Description:
# This endpoint allows you to search for cars in the database.
# Query parameters:
# sort_by: Field by which to sort the search results (optional)
# limit: Number of records to return (optional)
# Headers:
# Authorization: Access token obtained during authentication
# Response:
# A list of cars in JSON format. Each car contains information about the make,
# year of manufacture, engine capacity, and price.

# Usage example:
# Authentication: POST /auth auth: HTTPBasicAuth('test_user', 'test_pass')
# Getting an access token:  {'access_token': '<access_token>'}
# Searching for cars: GET /cars?sort_by=price&limit=10
# Headers are: {'Authorization': 'Bearer <access_token>'}
# Response:[ {'brand':'BMW', 'year':2018, 'engine_volume': 2.0, 'price':50000},
# {'brand':'Audi', 'year':2020, 'engine_volume':1.8, 'price':45000},  ... ]
# Car data
# download the file Car data.txt

# Tips
# Auth
# You will need to use request.Session
# For the initial login you
# will need **from requests.auth import HTTPBasicAuth**
# After receiving the access_token from the response,
# it can be registered for the entire
# Session session.headers.update({'Authorization': 'Bearer ' + access_token})

import pytest
import requests

BASE_URL = 'http://127.0.0.1:8080'


class TestCarSearchAPI:
    """Cars API search functionality test with logging."""

    @pytest.fixture(autouse=True)
    def setup_class(self, setup_logging):
        """Use the logger set up in conftest.py.

        Args:
            setup_logging (Logger): The logger instance set up in conftest.py.
        """
        self.logger = setup_logging

    def _send_request(self, session, endpoint, params=None):
        """Send an API request and handle errors.

        Args:
            session (requests.Session): Authenticated session with token.
            endpoint (str): The API endpoint.
            params (dict or None): Query parameters for the request.

        Returns:
            dict: JSON response from the API.
        """
        try:
            response = session.get(
                f'{BASE_URL}{endpoint}', params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            error_message = 'Request timed out.'
            self.logger.error(error_message)
            return pytest.fail(error_message)  # Directly fail the test
        except requests.exceptions.HTTPError as http_err:
            error_message = f'HTTP error occurred: {http_err}'
            self.logger.error(error_message)
            return pytest.fail(error_message)  # Directly fail the test
        except Exception as err:
            error_message = f'An unexpected error occurred: {err}'
            self.logger.error(error_message)
            return pytest.fail(error_message)  # Directly fail the test

    @pytest.mark.parametrize(
        'sort_by,limit,expected_brands',
        [
            ('brand', 10, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet',
                           'Ferrari', 'Ford', 'Honda', 'Hyundai', 'Infiniti']),
            ('year', 3, ['Toyota', 'Ford', 'Honda']),
            ('engine_volume', 6, ['Tesla', 'Nissan', 'Honda',
                                  'Hyundai', 'Audi', 'Chevrolet']),
            ('price', 5, ['Chevrolet', 'Hyundai', 'Kia', 'Ford', 'Honda']),
            (None, 5, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet']),
            (None, None, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet']),
            ('brand', None, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet']),
            ('year', None, ['Toyota', 'Ford', 'Honda']),
            ('engine_volume', None, ['Acura', 'Audi', 'BMW', 'Bugatti']),
            ('price', None, ['Chevrolet', 'Hyundai', 'Kia', 'Volkswagen',
                             'Ford', 'Mazda', 'Nissan', 'Subaru']),
        ],
    )
    def test_search_cars(self, auth_session, sort_by, limit, expected_brands):
        """Test the Cars API search functionality.

        Args:
            auth_session (requests.Session): The Auth session with token.
            sort_by (str or None): The field to sort the results by.
            limit (int or None): The limit of cars to return in the result.
            expected_brands (list): The expected list of car brands.
        """
        params = {'sort_by': sort_by} if sort_by else {}
        if limit:
            params['limit'] = limit

        # Log the full response and brands for debugging
        cars = self._send_request(auth_session, '/cars', params)
        brands = [car['brand'] for car in cars]

        self._log_response(sort_by, limit, expected_brands, brands)

        # Ensure expected brands are in the result (order doesn't matter)
        self._verify_brands(expected_brands, brands)

    def _log_response(self, sort_by, limit, expected_brands, brands):
        """Log the full response and brand comparison.

        Args:
            sort_by (str or None): The field used to sort the results.
            limit (int or None): The limit of cars to return.
            expected_brands (list): List of expected car brands.
            brands (list): List of brands returned in the response.
        """
        response_message = (f'Full response for sort_by={sort_by}, '
                            f'limit={limit}: {brands}')
        actual_message = (f'Tested sort_by={sort_by}, limit={limit}. '
                          f'Expected brands: {expected_brands}, '
                          f'Got brands: {brands}')
        self.logger.info(response_message)
        self.logger.info(actual_message)

    def _verify_brands(self, expected_brands, brands):
        """Verify if the expected brands are in the result.

        Args:
            expected_brands (list): The expected brands to find.
            brands (list): The list of car brands returned by the API.
        """
        for brand in expected_brands:
            if brand not in brands:
                error_message = f'{brand} not found in the results'
                self.logger.error(error_message)
                pytest.fail(error_message)
