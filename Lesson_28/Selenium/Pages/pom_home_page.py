"""Page Object Model for Home page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space'


class HomePage:
    """Represent the home page of the qauto2 website."""

    def __init__(self, driver):
        """Initialize the Home page object.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.signup_button = (By.XPATH, '//button[text()="Sign up"]')
        self.signin_button = (By.XPATH, '//button[text()="Sign In"]')

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

    def load(self):
        """Open the home page in the browser."""
        self.driver.get(BASE_URL)

    def click_signup(self):
        """Click the Sign up button."""
        self.wait_for_element(self.signup_button).click()

    def click_signin(self):
        """Click the Sign In button."""
        self.wait_for_element(self.signin_button).click()
