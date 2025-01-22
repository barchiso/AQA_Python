"""Homework #28. User registration check using selenium."""
import os
from datetime import datetime

import pytest

from Pages.pom_garage_page import GaragePage

PASSWORD = os.getenv('TEST_PASSWORD', 'Password1')
EMAIL = f'example+{int(datetime.now().timestamp())}@mail.com'
login_email = EMAIL


class TestRegistration:
    """Test cases for user registration functionality."""

    @pytest.mark.parametrize(
        ('browser_and_form, name, last_name, email, password, '
         'confirm_password, expected_message'),
        [
            ('signup_form', '', 'Bravo', EMAIL,
             PASSWORD, PASSWORD, 'Name required'),
            ('signup_form', 'Johnny', '', EMAIL,
             PASSWORD, PASSWORD, 'Last name required'),
            ('signup_form', 'Johnny', 'Bravo', '',
             PASSWORD, PASSWORD, 'Email required'),
            ('signup_form', 'Johnny', 'Bravo', 'EMAIL', PASSWORD, PASSWORD,
             'Email is incorrect'),
            ('signup_form', 'Johnny', 'Bravo', EMAIL,
             '', PASSWORD, 'Password required'),
            ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD, '',
             'Re-enter password required'),
            ('signup_form', 'Johnny', 'Bravo', EMAIL, 'short', '',
             'Password has to be from 8 to 15 characters long and contain at '
             'least one integer, one capital, and one small letter'),
            ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD,
             'Mismatch1', 'Passwords do not match'),
            ('signup_form', 'Johnny', 'Bravo', EMAIL, PASSWORD,
             PASSWORD, 'Registration complete'),
        ],
        indirect=['browser_and_form'],
    )
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
        # browser_and_form is the fixture for SignUpForm
        signup_form = browser_and_form
        signup_form.fill_form(
            name, last_name, email, password, confirm_password)

        # Wait for success/error message
        if expected_message in signup_form.ERROR_LOCATORS:
            # Handle error message display
            error_message = signup_form.get_error_message(expected_message)
            assert error_message == expected_message, f'Expected error: {
                expected_message}, Found: {error_message}'
        else:
            signup_form.click_register()  # Click the Register button
            # Handle successful login
            success_message = signup_form.get_success_message()
            assert success_message == expected_message, f'Expected success: {
                expected_message}, Found: {success_message}'


class TestLogin:
    """Test cases for user login and logout functionality."""

    @pytest.mark.parametrize(
        'browser_and_form, email, password, expected_message',
        [
            ('signin_form', '', PASSWORD, 'Email required'),
            ('signin_form', 'invalid_email', PASSWORD, 'Email is incorrect'),
            ('signin_form', 'valid_email', '', 'Password required'),
            ('signin_form', login_email, PASSWORD,
             'You have been successfully logged in'),
        ],
        indirect=['browser_and_form'],
    )
    def test_user_login(self, browser_and_form, email,
                        password, expected_message):
        """Test user login functionality.

        Args:
            browser_and_form: The browser and form fixture for SignInForm.
            email: Email address used to log in.
            password: Password for the account.
            expected_message: Expected success or error message.

        """
        # browser_and_form is the fixture for SignInForm
        signin_form = browser_and_form
        signin_form.fill_form(email, password)

        # Wait for success/error message
        if expected_message in signin_form.ERROR_LOCATORS:
            # Handle error message display
            error_message = signin_form.get_error_message(expected_message)
            assert error_message == expected_message, f'Expected error: {
                expected_message}, Found: {error_message}'
        else:
            signin_form.click_login()  # Click the login button
            # Handle successful login
            success_message = signin_form.get_success_message()
            assert success_message == expected_message, f'Expected success: {
                expected_message}, Found: {success_message}'

    @pytest.mark.parametrize('browser_and_form', ['signin_form'],
                             indirect=True)
    def test_logout(self, browser_and_form):
        """Test logout functionality.

        Args:
            browser_and_form: The browser and form fixture for SignInForm.
        """
        # Assuming the user is already logged in
        signin_form = browser_and_form
        signin_form.fill_form(login_email, PASSWORD)
        signin_form.click_login()

        # Navigate to the garage page and perform logout
        garage_page = GaragePage(signin_form.page)
        garage_page.click_logout()

        # Verify the user is logged out
        assert garage_page.is_logged_out(), 'Logout was not successful.'
