"""Fixtures and setup code for the test suite."""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(params=['chromium', 'firefox', 'webkit'], scope='class')
def browser_context(request):
    """Fixture to set up the browser driver.

    Args:
        request (Fixture): Pytest fixture used to get the current browser name.

    Yields:
        WebDriver: The initialized browser driver.
    """
    with sync_playwright() as p:
        browser_name = request.param
        browser = getattr(p, browser_name).launch(headless=False)
        context = browser.new_context()

        yield context

        browser.close()
