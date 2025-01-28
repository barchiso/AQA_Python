"""Page Object Model for Garage page."""
from playwright.sync_api import Page


class GaragePage:
    """Represent the garage page of the qauto2 website."""

    LOGOUT_BUTTON = '//a[contains(text(), "Log out")]'

    def __init__(self, page: Page):
        """Initialize the Garage page object.

        Args:
            page: Playwright Page instance.
        """
        self.page = page

    def wait_for_element(self, locator, timeout=5000):
        """Wait for an element to be visible on the page.

        Args:
            locator: The locator of the element to wait for.
            timeout: Maximum time to wait for the element (in milliseconds).

        Returns:
            ElementHandle: The element that becomes visible.
        """
        return self.page.wait_for_selector(locator, timeout=timeout)

    def click_logout(self):
        """Click the Log out button."""
        self.wait_for_element(self.LOGOUT_BUTTON)
        self.page.click(self.LOGOUT_BUTTON)

    def is_logged_out(self):
        """Check if the user is logged out.

        Returns:
            bool: True if logout was successful, False otherwise.
        """
        # Check for the presence of login/sign-in button after logout
        self.wait_for_element('//button[text()="Sign In"]')
        return self.page.is_visible('//button[text()="Sign In"]')
