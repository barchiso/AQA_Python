"""Page Object Model for Registration form."""
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SignUpForm():
    """Represent the Registration form of the qauto2 website."""

    def __init__(self, driver):
        """Initialize the Registration form object.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.FIELD_LOCATORS = {
            'name': (By.XPATH, '//input[@id="signupName"]'),
            'last_name': (By.XPATH, '//input[@id="signupLastName"]'),
            'email': (By.XPATH, '//input[@id="signupEmail"]'),
            'password': (By.XPATH, '//input[@id="signupPassword"]'),
            'confirm': (By.XPATH, '//input[@id="signupRepeatPassword"]'),
        }
        self.ERROR_LOCATORS = {
            'Name required': (By.XPATH, '//p[text()="Name required"]'),
            'Last name required':
            (By.XPATH, '//p[text()="Last name required"]'),
            'Email required': (By.XPATH, '//p[text()="Email required"]'),
            'Email is incorrect':
            (By.XPATH, '//p[text()="Email is incorrect"]'),
            'Password required': (By.XPATH, '//p[text()="Password required"]'),
            ('Password has to be from 8 to 15 characters long and contain at '
             'least one integer, one capital, and one small letter'):
            (By.XPATH, '//div[4]//div[1]//p[1]'),
            'Re-enter password required':
            (By.XPATH, '//p[text()="Re-enter password required"]'),
            'Passwords do not match':
            (By.XPATH, '//p[text()="Passwords do not match"]'),
        }
        self.register_button = (By.XPATH, '//button[text()="Register"]')
        self.success_message = (
            By.XPATH, '//p[text()="Registration complete"]')

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
        """Fill a specific field in the signup form.

        Args:
            field_name: The name of the field to fill (e.g., 'name', 'email').
            value: The value to enter into the field.
        """
        field_locator = self.FIELD_LOCATORS[field_name]
        field_element = self.wait_for_element(field_locator)
        field_element.clear()
        field_element.send_keys(value)

    def fill_form(self, name, last_name, email, password, confirm_password):
        """Fill in the registration form.

        Args:
            name: The user's first name.
            last_name: The user's last name.
            email: The user's email address.
            password: The user's chosen password.
            confirm_password: The user's confirmation of the password.
        """
        self.fill_field('name', name)
        self.fill_field('last_name', last_name)
        self.fill_field('email', email)
        self.fill_field('password', password)
        self.fill_field('confirm', confirm_password)

    def click_register(self):
        """Click the Register button."""
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        """Retrieve the success message after registration.

        Returns:
            str: The success message text.
        """
        return self.wait_for_element(self.success_message).text

    def get_error_locator(self, message):
        """Return the locator for the error message.

        Args:
            message(str): The error message key to retrieve the locator.

        Returns:
            tuple: The locator(By, value) for the corresponding error message.
        """
        # Return the error locator from the dictionary if message exists
        return self.ERROR_LOCATORS.get(message)
