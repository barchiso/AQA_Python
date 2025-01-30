"""Page Object Model for Home page."""

BASE_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space'


class HomePage:
    """Represent the home page of the qauto2 website."""

    SIGNUP_BUTTON = '//button[text()="Sign up"]'
    SIGNIN_BUTTON = '//button[text()="Sign In"]'

    def __init__(self, context):
        """Initialize the Home page object.

        Args:
            context: Playwright BrowserContext instance.
        """
        self.context = context
        self.page = context.new_page()

    def wait_for_element(self, selector: str, timeout=5000):
        """Wait for an element to be visible on the page.

        Args:
            selector: The CSS selector or XPath of the element to wait for.
            timeout: Maximum time to wait for the element (in milliseconds).

        Returns:
            ElementHandle: The element that becomes visible.
        """
        return self.page.wait_for_selector(selector, timeout=timeout)

    def load(self):
        """Open the home page in the browser."""
        self.page.goto(BASE_URL)

    def click_signup(self):
        """Click the Sign up button."""
        self.wait_for_element(self.SIGNUP_BUTTON)
        self.page.click(self.SIGNUP_BUTTON)

    def click_signin(self):
        """Click the Sign In button."""
        self.wait_for_element(self.SIGNIN_BUTTON)
        self.page.click(self.SIGNIN_BUTTON)
