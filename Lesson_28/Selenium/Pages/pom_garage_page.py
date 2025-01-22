"""Page Object Model for Garage page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class GaragePage:
    """Represent the garage page of the qauto2 website."""

    def __init__(self, driver):
        """Initialize the Garage page object.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.logout_button = (By.XPATH, '//a[contains(text(), "Log out")]')

    def wait_for_element(self, locator, timeout=5):
        """Wait for an element to be visible on the page.

        Args:
            locator: The locator of the element to wait for.
            timeout: Maximum time to wait for the element (in seconds).

        Returns:
            WebElement: The web element that becomes visible.
        """
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator),
        )

    def click_logout(self):
        """Click the Log out button."""
        self.wait_for_element(self.logout_button).click()
