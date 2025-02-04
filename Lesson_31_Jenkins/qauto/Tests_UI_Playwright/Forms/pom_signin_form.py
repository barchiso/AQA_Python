"""Page Object Model for Login form."""
from playwright.sync_api import Page


class SignInForm:
    """Represent the Login form of the qauto2 website."""

    FIELD_LOCATORS = {
        'email': '#signinEmail',
        'password': '#signinPassword',
    }
    ERROR_LOCATORS = {
        'Email required': 'text=Email required',
        'Email is incorrect': 'text=Email is incorrect',
        'Password required': 'text=Password required',
    }
    SIGNIN_BUTTON = 'button:has-text("Login")'
    SUCCESS_MESSAGE = 'text=You have been successfully logged in'
    ERROR_MESSAGE = '.alert-danger'

    def __init__(self, page: Page):
        """Initialize the Login form object.

        Args:
            page (Page): Playwright page object.
        """
        self.page = page

    def fill_field(self, field_name, value):
        """Fill a specific field in the login form.

        Args:
            field_name (str): The name of the field to fill.
            value (str): The value to enter into the field.
        """
        self.wait_for_element(self.FIELD_LOCATORS[field_name])
        self.page.fill(self.FIELD_LOCATORS[field_name], value)
        self.page.press(self.FIELD_LOCATORS[field_name], 'Tab')

    def fill_form(self, email, password):
        """Fill in the Login form.

        Args:
            email (str): The email address to enter.
            password (str): The password to enter.
        """
        self.fill_field('email', email)
        self.fill_field('password', password)

    def click_login(self):
        """Click the Login button."""
        self.wait_for_element(self.SIGNIN_BUTTON)
        self.page.click(self.SIGNIN_BUTTON)

    def get_success_message(self):
        """Retrieve the success message after Login.

        Returns:
            str: The success message text.
        """
        # Wait for the success message to appear
        self.wait_for_element(self.SUCCESS_MESSAGE)
        return self.page.text_content(self.SUCCESS_MESSAGE)

    def get_error_message(self, message):
        """Retrieve the error message after Login.

        Args:
            message (str): The error message key to look for.

        Returns:
            str: The error message text.
        """
        # Wait for the error message to appear
        self.wait_for_element(self.ERROR_LOCATORS[message])
        return self.page.text_content(self.ERROR_LOCATORS[message])

    def wait_for_element(self, locator, timeout=5000):
        """Wait for an element to appear.

        Args:
            locator (str): The CSS selector or XPath of the element to wait.
            timeout (int, optional): Maximum time to wait for the element.
        """
        self.page.wait_for_selector(locator, timeout=timeout)
