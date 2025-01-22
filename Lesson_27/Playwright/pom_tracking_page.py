"""Page Object Model for the Nova Post tracking page."""

BASE_URL = 'https://tracking.novaposhta.ua/#/uk'


class TrackingPage:
    """Represent the tracking page of the Nova Post website."""

    def __init__(self, context):
        """Initialize the TrackingPage object.

        Args:
            context: Playwright browser context object.
        """
        self.page = context.new_page()
        self.invoice_input = '//input[@id = "en"]'
        self.search_button = '//input[@type= "submit"]'
        self.status_text = '//div[@class="header__status-text"]'
        self.error_msg = '//span[contains(text(), "Ми не знайшли посилку")]'

    def load(self):
        """Load the Nova Post tracking page."""
        self.page.goto(BASE_URL)

    def set_invoice(self, invoice):
        """Enter the invoice number in the input field.

        Args:
            invoice (str): The invoice number.
        """
        self.page.fill(self.invoice_input, invoice)

    def click_search(self):
        """Click the search button to start tracking."""
        self.page.click(self.search_button)

    def get_status(self):
        """Retrieve the status of the parcel.

        Returns:
            str: The parcel's status text if found, else None.
        """
        try:
            return self.page.wait_for_selector(
                self.status_text,
                timeout=10000,
            ).inner_text()
        except Exception:
            return self.get_error_message()

    def get_error_message(self):
        """Retrieve the error message if no parcel is found.

        Returns:
            str: The error message text if found, else None.

        Raises:
            RuntimeError: The error message from the page.
        """
        try:
            return self.page.wait_for_selector(
                self.error_msg,
                timeout=10000,
            ).inner_text()
        except Exception as exc:
            raise RuntimeError(
                f'Error retrieving error message: {exc}') from exc
