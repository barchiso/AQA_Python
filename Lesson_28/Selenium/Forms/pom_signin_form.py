"""Page Object Model for Login form."""
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SignInForm:
    """Represent the Login form of the qauto2 website."""

    def __init__(self, driver):
        """Initialize the Login forme object.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.FIELD_LOCATORS = {
            'email': (By.XPATH, '//input[@id="signinEmail"]'),
            'password': (
                By.XPATH, '//input[@id="signinPassword"]'),
        }
        self.ERROR_LOCATORS = {
            'Email required': (By.XPATH, '//p[text()="Email required"]'),
            'Email is incorrect':
            (By.XPATH, '//p[text()="Email is incorrect"]'),
            'Password required': (By.XPATH, '//p[text()="Password required"]'),


            'password': (By.XPATH, '//p[text()="Password required"]'),
        }
        self.signin_button = (By.XPATH, '//button[text()="Login"]')
        self.success_message = (
            By.XPATH, '//p[text()="You have been successfully logged in"]')
        self.error_message = (
            By.XPATH, '//p[@class="alert alert-danger"]')

    def wait_for_element(self, locator, timeout=5):
        """Wait for an element to be visible on the page.

        Args:
            locator: The locator of the element to wait for.
            timeout: Maximum time to wait for the element (in seconds).

        Returns:
            WebElement: The web element that becomes visible.

        Raises:
            NoSuchElementException: If the element is not found.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator),
            )
        except TimeoutException as exc:
            raise NoSuchElementException(
                f'Element with locator {
                    locator} not found within {timeout} seconds.',
            ) from exc

    def fill_field(self, field_name, value):
        """Fill a specific field in the login form.

        Args:
            field_name (str): The name of the field (email or password).
            value (str): The value to enter into the field.
        """
        field_locator = self.FIELD_LOCATORS[field_name]
        field_element = self.wait_for_element(field_locator)
        field_element.clear()
        field_element.send_keys(value)

    def fill_form(self, email, password):
        """Fill in the Login form.

        Args:
            email(str): The user's email address.
            password(str): The user's password.
        """
        self.fill_field('email', email)
        self.fill_field('password', password)

    def click_login(self):
        """Click the Login button."""
        self.wait_for_element(self.signin_button).click()

    def get_success_message(self):
        """Retrieve the success message after Login.

        Returns:
            str: The success message text.
        """
        return self.wait_for_element(self.success_message).text

    def get_error_locator(self, message):
        """Return the locator for the error message.

        Args:
            message (str): The error message key to retrieve the locator.

        Returns:
            tuple: The locator (By, value) for the corresponding error message.
        """
        # Return the error locator from the dictionary if message exists
        return self.ERROR_LOCATORS.get(message)
