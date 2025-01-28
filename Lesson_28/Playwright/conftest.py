"""Fixtures and setup code for the test suite."""

import pytest
from playwright.sync_api import sync_playwright

from Forms.pom_signin_form import SignInForm
from Forms.pom_signup_form import SignUpForm
from Pages.pom_home_page import HomePage


@pytest.fixture(scope='class')
def browser_and_form(request):
    """Fixture to set up the browser, context, and form.

    Args:
        request: The pytest request object.

    Yields:
        An instance of either SignUpForm or SignInForm, depending on the test.

    Raises:
        ValueError: If an unsupported form type is specified in the test.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        home_page = HomePage(context)

        # Load the home page and decide which form to initialize
        home_page.load()

        # Get the form_type parameter explicitly passed via test parametrize
        form_type = request.param

        if form_type == 'signup_form':
            home_page.click_signup()
            form = SignUpForm(home_page.page)
        elif form_type == 'signin_form':
            home_page.click_signin()
            form = SignInForm(home_page.page)
        else:
            raise ValueError(f'Unsupported form type: {form_type}')

        yield form

        context.close()
        browser.close()
