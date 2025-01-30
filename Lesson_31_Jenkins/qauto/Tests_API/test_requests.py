"""Homework #31. Jenkins - Write a test and add Allure reports."""
# Add Allure to run in Docker container.
# Tests must have a feature decorator.
# Tests should consist of steps.

from datetime import datetime

import allure
import pytest
import requests

BASE_URL = 'https://qauto.forstudy.space/api'
TIMEOUT = 10

CARS_BRANDS = [
    {'id': 1, 'title': 'Audi', 'logoFilename': 'audi.png'},
    {'id': 2, 'title': 'BMW', 'logoFilename': 'bmw.png'},
    {'id': 3, 'title': 'Ford', 'logoFilename': 'ford.png'},
    {'id': 4, 'title': 'Porsche', 'logoFilename': 'porsche.png'},
    {'id': 5, 'title': 'Fiat', 'logoFilename': 'fiat.png'},
]

CARS_MODELS = [
    {'id': 3, 'carBrandId': 1, 'title': 'Q7'},
    {'id': 8, 'carBrandId': 2, 'title': 'X5'},
    {'id': 12, 'carBrandId': 3, 'title': 'Focus'},
    {'id': 16, 'carBrandId': 4, 'title': '911'},
    {'id': 21, 'carBrandId': 5, 'title': 'Panda'},
]

SIGNUP_PAYLOAD = {
    'name': 'Johnny',
    'lastName': 'Bravo',
    'email': f'example+{int(datetime.now().timestamp())}@mail.com',
    'password': 'Password1',
    'repeatPassword': 'Password1',
}

SIGNIN_PAYLOAD = {
    'email': 'example+111233@gmail.com',
    'password': 'Password1',
    'remember': True,
}


@allure.feature('Car API Tests')
class TestCars:
    """Test suite for Car API."""

    @allure.story('Get car brands')
    @allure.step('Sending request to get car brands')
    def test_get_car_brands(self, timeout=TIMEOUT):
        """Test to fetch all car brands.

        Args:
            timeout (int): The timeout value for the request in seconds.
        """
        response = requests.get(
            f'{BASE_URL}/cars/brands', headers={'accept': 'application/json'},
            timeout=timeout,
        )
        response.raise_for_status()
        response_data = response.json()

        # Ensure the response contains a 'status' field with value 'ok'
        assert response_data['status'] == 'ok', 'Status should be ok'
        # Check if the 'data' field is a list
        brands = response_data['data']
        assert isinstance(brands, list)
        # Validate that each brand in the list
        for brand in brands:
            assert 'id' in brand
            assert 'title' in brand
            assert 'logoFilename' in brand
            assert isinstance(brand['title'], str) and len(brand['title']) > 0
            assert isinstance(brand['id'], int) and brand['id'] > 0
            assert isinstance(brand['logoFilename'], str) and len(
                brand['logoFilename']) > 0

    @allure.story('Get car brand by ID')
    @pytest.mark.parametrize('car_brand', CARS_BRANDS)
    @allure.step('Sending request to get car brand by ID')
    def test_get_car_brand_by_id(self, car_brand, timeout=TIMEOUT):
        """Test to fetch car brands by their IDs.

        Args:
            car_brand (dict): The car brand data to test.
            timeout (int): The timeout value for the request in seconds.
        """
        car_brand_id = car_brand['id']

        # Sending GET request
        response = requests.get(
            f'{BASE_URL}/cars/brands/{car_brand_id}',
            headers={'accept': 'application/json'},
            timeout=timeout,
        )
        response.raise_for_status()
        response_data = response.json()

        # Assertions
        assert response_data['status'] == 'ok', 'Status should be ok'
        brand_data = response_data['data']
        assert brand_data['id'] == car_brand['id'], (
            f'Expected brand ID {car_brand["id"]}, got {brand_data["id"]}')
        assert brand_data['title'] == car_brand['title'], (
            f"Expected title {car_brand['title']}, got {brand_data['title']}")
        assert brand_data['logoFilename'] == car_brand['logoFilename'], (
            f"Expected logoFilename {car_brand['logoFilename']},"
            f"got {brand_data['logoFilename']}")

    @allure.story('Get car models')
    @allure.step('Sending request to get car models')
    def test_get_car_models(self, timeout=TIMEOUT):
        """Test to fetch all car models.

        Args:
            timeout (int): The timeout value for the request in seconds.
        """
        response = requests.get(
            f'{BASE_URL}/cars/models', headers={'accept': 'application/json'},
            timeout=timeout,
        )
        response.raise_for_status()
        response_data = response.json()

        # Ensure the response contains a 'status' field with value 'ok'
        assert response_data['status'] == 'ok', 'Status should be ok'
        # Check if the 'data' field is a list
        models = response_data['data']
        assert isinstance(models, list)
        # Validate that each model in the list
        for model in models:
            assert 'id' in model
            assert 'carBrandId' in model
            assert 'title' in model
            assert isinstance(model['title'], str) and len(model['title']) > 0
            assert isinstance(model['id'], int) and model['id'] > 0
            assert isinstance(model['carBrandId'],
                              int) and model['carBrandId'] > 0

    @allure.story('Get car model by ID')
    @pytest.mark.parametrize('car_model', CARS_MODELS)
    @allure.step('Sending request to get car model by ID')
    def test_get_car_model_by_id(self, car_model, timeout=TIMEOUT):
        """Test to fetch car models by their IDs.

        Args:
            car_model (dict): The car model data to test.
            timeout (int): The timeout value for the request in seconds.
        """
        car_model_id = car_model['id']

        # Sending GET request
        response = requests.get(
            f'{BASE_URL}/cars/models/{car_model_id}',
            headers={'accept': 'application/json'},
            timeout=timeout,
        )
        response.raise_for_status()
        response_data = response.json()

        # Assertions
        assert response_data['status'] == 'ok', 'Status should be ok'
        model_data = response_data['data']
        assert model_data['id'] == car_model['id'], (
            f"Expected model ID {car_model['id']}, got {model_data['id']}")
        assert model_data['carBrandId'] == car_model['carBrandId'], (
            f"Expected carBrandId {car_model['carBrandId']},"
            f"got {model_data['carBrandId']}")
        assert model_data['title'] == car_model['title'], (
            f"Expected title {car_model['title']}, got {model_data['title']}")

    @allure.story('SignUp functionality')
    @allure.step('Sending request to sign up a new user')
    def test_signup(self, timeout=TIMEOUT):
        """Test the SignUp functionality.

        Args:
            timeout (int): The timeout value for the request in seconds.
        """
        response = requests.post(
            f'{BASE_URL}/auth/signup', json=SIGNUP_PAYLOAD,
            timeout=timeout)
        response.raise_for_status()
        response_data = response.json()

        # Check if the response contains expected data
        assert response_data.get('status') == 'ok', 'SignUp status is not ok'
        assert 'userId' in response_data['data'], (
            'UserId not found in the response')
        assert 'photoFilename' in response_data['data'], (
            'photoFilename not found in the response')
        assert 'distanceUnits' in response_data['data'], (
            'distanceUnits not found in the response')
        assert 'currency' in response_data['data'], (
            'currency not found in the response')

    @allure.story('SignIn functionality')
    @allure.step('Sending request to sign in a user')
    def test_signin(self, timeout=TIMEOUT):
        """Test the SignIn functionality.

        Args:
            timeout (int): The timeout value for the request in seconds.
        """
        response = requests.post(
            f'{BASE_URL}/auth/signin', json=SIGNIN_PAYLOAD,
            timeout=timeout,
        )
        response.raise_for_status()
        response_data = response.json()

        # Check if the response contains expected data
        assert response_data.get('status') == 'ok', 'SignIn status is not ok'
        assert 'userId' in response_data['data'], (
            'UserId not found in the response')
        assert 'photoFilename' in response_data['data'], (
            'photoFilename not found in the response')
        assert 'distanceUnits' in response_data['data'], (
            'distanceUnits not found in the response')
        assert 'currency' in response_data['data'], (
            'currency not found in the response')

    @allure.story('Logout functionality')
    @allure.step('Sending request to logout user')
    def test_logout(self, timeout=TIMEOUT):
        """Test the Logout functionality.

        Args:
            timeout (int): The timeout value for the request in seconds.
        """
        response = requests.get(f'{BASE_URL}/auth/logout',
                                timeout=timeout)
        response.raise_for_status()
        response_data = response.json()

        # Check if the response contains the expected status
        assert response_data.get('status') == 'ok', 'Logout status is not ok'
