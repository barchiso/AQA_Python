"""Homework #28. User registration check using selenium."""
import os
from datetime import datetime

import pytest

from Forms.pom_signin_form import SignInForm
from Forms.pom_signup_form import SignUpForm
from Pages.pom_garage_page import GaragePage
from Pages.pom_home_page import HomePage

PASSWORD = os.getenv('TEST_PASSWORD', 'Password1')
EMAIL = f'example+{int(datetime.now().timestamp())}@mail.com'
login_email = EMAIL


class TestRegistration:
    """Test cases for user registration functionality."""

    @pytest.mark.parametrize(
        'name, last_name, email, password, confirm_password, expected_message',
        [
            ('', 'Bravo', EMAIL, PASSWORD, PASSWORD, 'Name required'),
            ('Johnny', '', EMAIL, PASSWORD, PASSWORD, 'Last name required'),
            ('Johnny', 'Bravo', '', PASSWORD, PASSWORD, 'Email required'),
            ('Johnny', 'Bravo', 'EMAIL', PASSWORD, PASSWORD,
             'Email is incorrect'),
            ('Johnny', 'Bravo', EMAIL, '', PASSWORD, 'Password required'),
            ('Johnny', 'Bravo', EMAIL, PASSWORD, '',
             'Re-enter password required'),
            ('Johnny', 'Bravo', EMAIL, 'short', 'short',
             'Password has to be from 8 to 15 characters long and contain at '
             'least one integer, one capital, and one small letter'),
            ('Johnny', 'Bravo', EMAIL, PASSWORD,
             'Mismatch1', 'Passwords do not match'),
            ('Johnny', 'Bravo', EMAIL, PASSWORD,
             PASSWORD, 'Registration complete'),
        ],
    )
    def test_user_registration(self, browser_driver, name, last_name, email,
                               password, confirm_password, expected_message):
        """Test user registration with various valid and invalid inputs.

        Args:
            browser_driver: WebDriver instance for browser automation.
            name: First name of the user.
            last_name: Last name of the user.
            email: Email address of the user.
            password: Password for the account.
            confirm_password: Password confirmation.
            expected_message: Expected success or error message.
        """
        # Initialize the pages and driver
        home_page = HomePage(browser_driver)
        signup_form = SignUpForm(browser_driver)

        # Load the homepage and navigate to the signup form
        home_page.load()
        home_page.click_signup()

        # Fill out the signup form
        signup_form.fill_form(name, last_name, email,
                              password, confirm_password)

        # Click on the Register button
        signup_form.click_register()

        # Check the expected error or success message
        if expected_message == 'Registration complete':
            success_message = signup_form.get_success_message()
            assert success_message == expected_message, (
                f'Expected: {expected_message}, but got: {success_message}')

        else:
            error_message_locator = signup_form.get_error_locator(
                expected_message)

            if error_message_locator is None:
                pytest.fail(
                    f'Error message locator for'
                    f'{expected_message} not found in the form.')

            try:
                error_message = signup_form.wait_for_element(
                    error_message_locator).text
            except Exception as e:
                pytest.fail(
                    f'Failed to find error message for'
                    f'{expected_message}: {str(e)}')

            assert expected_message in error_message, (
                f'Expected: {expected_message}, but got: {error_message}')


class TestLogin:
    """Test cases for user login and logout functionality."""

    @pytest.mark.parametrize(
        'email, password, expected_message',
        [
            ('', PASSWORD, 'Email required'),
            ('invalid_email', PASSWORD,
             'Email is incorrect'),
            ('valid_email', '', 'Password required'),
            (login_email, PASSWORD, 'You have been successfully logged in'),
        ],
    )
    def test_user_login(self, browser_driver, email,
                        password, expected_message):
        """Test user login with various valid and invalid inputs.

        Args:
            browser_driver: WebDriver instance for browser automation.
            email: Email address used for login.
            password: Password used for login.
            expected_message: Expected success or error message.
        """
        # Initialize the pages and driver
        home_page = HomePage(browser_driver)
        signin_form = SignInForm(browser_driver)
        garage_page = GaragePage(browser_driver)
        # Load the homepage and navigate to the signup form
        home_page.load()
        home_page.click_signin()
        # Load the login page
        signin_form.fill_form(email, password)
        # Click on the Login button
        signin_form.click_login()
        # Check the expected error or success message
        if expected_message == 'You have been successfully logged in':
            success_message = signin_form.get_success_message()
            assert success_message == expected_message, (
                f'Expected: {expected_message}, but got: {success_message}')
            # Perform logout
            garage_page.click_logout()
        else:
            error_message_locator = signin_form.get_error_locator(
                expected_message)
            if error_message_locator is None:
                pytest.fail(
                    f'Error message locator for {expected_message}'
                    f' not found in the form.')
            try:
                error_message = signin_form.wait_for_element(
                    error_message_locator).text
            except Exception as e:
                pytest.fail(
                    f'Failed to find error message for'
                    f'{expected_message}: {str(e)}')
            assert expected_message in error_message, (
                f'Expected: {expected_message}, but got: {error_message}')

    def test_logout(self, browser_driver):
        """Test logout functionality.

        Args:
            browser_driver: WebDriver instance for browser automation.

        """
        # Initialize the pages
        home_page = HomePage(browser_driver)
        signin_form = SignInForm(browser_driver)
        garage_page = GaragePage(browser_driver)

        # Perform login
        home_page.load()
        home_page.click_signin()
        signin_form.fill_form(login_email, PASSWORD)
        signin_form.click_login()

        # Perform logout
        garage_page.click_logout()

        # Verify that the "Sign In" button is visible again on the homepage
        try:
            signin_button = home_page.wait_for_element(home_page.signin_button)
            assert signin_button.is_displayed(), (
                'Sign In button not visible after logout.')
        except Exception as e:
            pytest.fail(f'Logout failed: {str(e)}')
