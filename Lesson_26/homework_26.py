"""Homework #26. Work with frames in python selenium."""
# Write to python selenium code that will pass on two frames
# on the original page, enter each frame, enter the correct secret text,
# click “Convert”, compare the text of the dual window
# to confirm the success of the verification and close the dialog box.

import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Frame:
    """A class to handle operations with frames on a web page.

    Attributes:
        driver: WebDriver instance used for interacting with the browser.
        base_url: URL of the page with frames.
    """

    def __init__(self, base_url, driver):
        """Initialize the Frame class with a given base URL and browser driver.

        Args:
            base_url (str): The URL of the page containing the frames.
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver = driver
        self.base_url = base_url

    def open_browser(self):
        """Open the web browser and loads the page at the given base URL.

        Raises:
            RuntimeError: If opening the browser fails.
        """
        try:
            self.driver.get(self.base_url)
        except Exception as error:
            error_message = f'Failed to open browser at {self.base_url}'
            raise RuntimeError(error_message) from error

    def frame_verification(self, frame_id, input_id, secret_text):
        """Open frame and check alert text.

        Args:
            frame_id (str): The ID of the frame to switch to.
            input_id (str): The ID of the input field.
            secret_text (str): The secret text to enter into the input field.

        Raises:
            ValueError: If the alert message.
            RuntimeError: For error while interacting with the WebDriver.
        """
        try:

            self.driver.switch_to.frame(frame_id)
            input_field = self.driver.find_element(By.ID, input_id)
            input_field.send_keys(secret_text)
            self.driver.find_element(
                By.XPATH, '//button[text()="Перевірити"]').click()

            # Verify alert message.
            alert = Alert(self.driver)
            alert_text = alert.text
            if alert_text != 'Верифікація пройшла успішно!':
                error_message = (f'Verification failed in frame {frame_id}. '
                                 f'Expected success message but got: '
                                 f'{alert_text}')
                raise ValueError(error_message)
            alert.accept()

        except Exception as error:
            error_message = (f'Error encountered during test in '
                             f'frame {frame_id}: {str(error)}')
            raise RuntimeError(error_message) from error

        finally:
            self.driver.switch_to.default_content()

    def close_browser(self):
        """Close the web browser and quits the WebDriver instance."""
        self.driver.quit()


if __name__ == '__main__':
    import os

    url = 'http://localhost:8000/dz.html'
    frame1_secret = os.getenv('FRAME1_SECRET', 'Frame1_Secret')
    frame2_secret = os.getenv('FRAME2_SECRET', 'Frame2_Secret')
    drivers = {
        'Chrome': webdriver.Chrome(),
        'Firefox': webdriver.Firefox(),
        'Edge': webdriver.Edge(),
    }

    for browser_name, browser in drivers.items():
        try:
            start_message = f'Starting tests for browser: {browser_name}'
            end_message = f'Finished tests for browser: {browser_name}'
            print(start_message)  # To understand which browser is running.
            frame = Frame(url, browser)
            frame.open_browser()
            frame.frame_verification('frame1', 'input1', frame1_secret)
            frame.frame_verification('frame2', 'input2', frame2_secret)
            # Verify that tests for browser completed successfully.
            print(end_message)

        except Exception as error:
            message = f'Error: {error}'
            print(message)

        finally:
            time.sleep(3)
            frame.close_browser()
