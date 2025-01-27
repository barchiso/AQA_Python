"""Homework #30. Write a test and add Allure reports."""
# Add Allure to run in Docker container.
# Tests must have a feature decorator.
# Tests should consist of steps.

import os
from datetime import datetime

import allure
import pytest

from Pages.pom_garage_page import GaragePage

PASSWORD = os.getenv('TEST_PASSWORD', 'Password1')
EMAIL = f'example+{int(datetime.now().timestamp())}@mail.com'
login_email = EMAIL

REGISTRATION_TEST_DATA = [
    ('signup_form', '', 'Bravo', EMAIL, PASSWORD, PASSWORD, 'Name required'),
    ('signup_form', 'Johnny', '', EMAIL, PASSWORD, PASSWORD,
     'Last name required'),
    ('signup_form', 'Johnny', 'Bravo', '', PASSWORD, PASSWORD,
     'Email required'),
    ('signup_form', 'Johnny', 'Bravo', 'EMAIL', PASSWORD, PASSWORD,
     'Email is incorrect'),
    ('signup_form', 'Johnny', 'Bravo', EMAIL, '', PASSWORD,
     'Password required'),
    ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD, '',
     'Re-enter password required'),
    ('signup_form', 'Johnny', 'Bravo', EMAIL, 'short', 'short',
     'Password has to be from 8 to 15 characters long and contain at '
     'least one integer, one capital, and one small letter'),
    ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD,
     'Mismatch1', 'Passwords do not match'),
    ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD,
     PASSWORD, 'Registration complete'),
]

LOGIN_TEST_DATA = [
    ('signin_form', '', PASSWORD, 'Email required'),
    ('signin_form', 'invalid_email', PASSWORD, 'Email is incorrect'),
    ('signin_form', 'valid_email', '', 'Password required'),
    ('signin_form', login_email, PASSWORD,
     'You have been successfully logged in'),
]


@allure.feature('User Registration')
class TestRegistration:
    """Test cases for user registration functionality."""

    @pytest.mark.parametrize(
        ('browser_and_form, name, last_name, email, password, '
         'confirm_password, expected_message'),
        REGISTRATION_TEST_DATA,
        indirect=['browser_and_form'],
    )
    @allure.story('Test registration with various inputs')
    def test_user_registration(self, browser_and_form, name, last_name, email,
                               password, confirm_password, expected_message):
        """Test user registration with various valid and invalid inputs.

        Args:
            browser_and_form: The browser and form fixture for SignUpForm.
            name: First name of the user.
            last_name: Last name of the user.
            email: Email address of the user.
            password: Password for the account.
            confirm_password: Password confirmation.
            expected_message: Expected success or error message.
        """
        # Step 1: Fill out the form
        signup_form = browser_and_form
        signup_form.fill_form(
            name, last_name, email, password, confirm_password)

        # Step 2: Check if expected error or success message is displayed
        if expected_message in signup_form.ERROR_LOCATORS:
            # Handle error message display
            error_message = signup_form.get_error_message(expected_message)
            assert error_message == expected_message, (
                f'Expected error: {expected_message}, Found: {error_message}',
            )
        else:
            signup_form.click_register()  # Click the Register button
            # Handle successful login
            success_message = signup_form.get_success_message()
            assert success_message == expected_message, (
                f'Expected success: {expected_message}, Found: {
                    success_message}',
            )


@allure.feature('User Login')
class TestLogin:
    """Test cases for user login and logout functionality."""

    @pytest.mark.parametrize(
        'browser_and_form, email, password, expected_message',
        LOGIN_TEST_DATA,
        indirect=['browser_and_form'],
    )
    @allure.story('Test login functionality')
    def test_user_login(self, browser_and_form, email,
                        password, expected_message):
        """Test user login functionality.

        Args:
            browser_and_form: The browser and form fixture for SignInForm.
            email: Email address used to log in.
            password: Password for the account.
            expected_message: Expected success or error message.
        """
        # Step 1: Fill out the login form
        signin_form = browser_and_form
        signin_form.fill_form(email, password)

        # Step 2: Check if expected error or success message is displayed
        if expected_message in signin_form.ERROR_LOCATORS:
            # Handle error message display
            error_message = signin_form.get_error_message(expected_message)
            assert error_message == expected_message, (
                f'Expected error: {expected_message}, Found: {error_message}',
            )
        else:
            signin_form.click_login()  # Click the login button
            # Handle successful login
            success_message = signin_form.get_success_message()
            assert success_message == expected_message, (
                f'Expected success: {expected_message}, Found: {
                    success_message}',
            )


@allure.feature('User Logout')
class TestLogout:
    """Test case for user logout functionality."""

    @pytest.mark.parametrize('browser_and_form', ['signin_form'],
                             indirect=True)
    @allure.story('Test logout functionality')
    @allure.title("User Logout - Verify logout functionality")
    def test_logout(self, browser_and_form):
        """Test logout functionality.

        Args:
            browser_and_form: The browser and form fixture for SignInForm.
        """
        # Step 1: Log in
        signin_form = browser_and_form
        signin_form.fill_form(login_email, PASSWORD)
        signin_form.click_login()

        # Step 2: Navigate to the garage page and perform logout
        garage_page = GaragePage(signin_form.page)
        garage_page.click_logout()

        # Step 3: Verify the user is logged out
        assert garage_page.is_logged_out(), 'Logout was not successful.'
