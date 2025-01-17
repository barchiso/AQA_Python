"""Page Object Model for the Nova Post tracking page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://tracking.novaposhta.ua/#/uk'


class TrackingPage:
    """Represent the tracking page of the Nova Post website."""

    def __init__(self, driver):
        """Initialize the TrackingPage object.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.invoice_input = (By.XPATH, '//input[@id = "en"]')
        self.search_button = (By.XPATH, '//input[@type= "submit"]')
        self.status_text = (By.XPATH, '//div[@class="header__status-text"]')
        self.error_message = (
            By.XPATH,
            '//span[contains(text(), "Ми не знайшли посилку")]',
        )

    def load(self):
        """Load the Nova Post tracking page."""
        self.driver.get(BASE_URL)

    def set_invoice(self, invoice):
        """Enter the invoice number in the input field.

        Args:
            invoice (str): The invoice number.
        """
        self.driver.find_element(*self.invoice_input).clear()
        self.driver.find_element(*self.invoice_input).send_keys(invoice)

    def click_search(self):
        """Click the search button to start tracking."""
        self.driver.find_element(*self.search_button).click()

    def get_status(self):
        """Retrieve the status of the parcel.

        Returns:
            str: The parcel's status text if found, else None.
        """
        try:
            status = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(self.status_text),
            )
            return status.text
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
            error_message = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(self.error_message),
            )
            return error_message.text
        except Exception as exc:
            raise RuntimeError(
                f'Error retrieving error message: {exc}') from exc
