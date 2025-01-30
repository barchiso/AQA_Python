"""Page Object Model for Registration form."""
from playwright.sync_api import Page


class SignUpForm:
    """Represent the Registration form of the qauto2 website."""

    FIELD_LOCATORS = {
        'name': '//input[@id="signupName"]',
        'last_name': '//input[@id="signupLastName"]',
        'email': '//input[@id="signupEmail"]',
        'password': '//input[@id="signupPassword"]',
        'confirm': '//input[@id="signupRepeatPassword"]',
    }
    ERROR_LOCATORS = {
        'Name required': '//p[text()="Name required"]',
        'Last name required': '//p[text()="Last name required"]',
        'Email required': '//p[text()="Email required"]',
        'Email is incorrect': '//p[text()="Email is incorrect"]',
        'Password required': '//p[text()="Password required"]',
        ('Password has to be from 8 to 15 characters long and contain at least'
         ' one integer, one capital, and one small letter'):
        '//div[4]//div[1]//p[1]',
        'Re-enter password required':
        '//p[text()="Re-enter password required"]',
        'Passwords do not match': '//p[text()="Passwords do not match"]',
    }
    REGISTER_BUTTON = '//button[text()="Register"]'
    SUCCESS_MESSAGE = '//p[text()="Registration complete"]'

    def __init__(self, page: Page):
        """Initialize the Registration form object.

        Args:
            page: Playwright page object.
        """
        self.page = page

    def fill_field(self, field_name, value):
        """Fill a specific field in the signup form.

        Args:
            field_name: The name of the field to fill (e.g., 'name', 'email').
            value: The value to enter into the field.
        """
        self.wait_for_element(self.FIELD_LOCATORS[field_name])
        self.page.fill(self.FIELD_LOCATORS[field_name], value)
        self.page.press(self.FIELD_LOCATORS[field_name], 'Tab')

    def fill_form(self, name, last_name, email,
                  password, confirm_password):
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
        self.wait_for_element(self.REGISTER_BUTTON)
        self.page.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        """Retrieve the success message after registration.

        Returns:
            str: The success message text.
        """
        # Wait for the success message to appear
        self.wait_for_element(self.SUCCESS_MESSAGE)
        return self.page.text_content(self.SUCCESS_MESSAGE)

    def get_error_message(self, message):
        """Return the selector for the error message.

        Args:
            message(str): The error message key to retrieve the selector.

        Returns:
            str: The error message selector.
        """
        # Wait for the error message to appear
        self.wait_for_element(self.ERROR_LOCATORS[message])
        return self.page.text_content(self.ERROR_LOCATORS[message])

    def wait_for_element(self, locator, timeout=5000):
        """Wait for an element to appear on the page.

        Args:
            locator (str): The XPath or CSS selector of the element to wait.
            timeout (int, optional): The maximum time to wait for the element.
        """
        self.page.wait_for_selector(locator, timeout=timeout)
