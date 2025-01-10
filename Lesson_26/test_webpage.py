"""Homework #26. Pytest tests using selenium."""
# Write to python selenium code that will pass on two frames
# on the original page, enter each frame, enter the correct secret text,
# click “Convert”, compare the text of the dual window
# to confirm the success of the verification and close the dialog box.

import os

import pytest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

FRAME1_SECRET = os.getenv('FRAME1_SECRET', 'Frame1_Secret')
FRAME2_SECRET = os.getenv('FRAME2_SECRET', 'Frame2_Secret')


class TestFrame:
    """Test the functionality of frames and alert messages."""

    @pytest.mark.parametrize(
        'frame_id, input_id, secret_text',
        [('frame1', 'input1', FRAME1_SECRET),
         ('frame2', 'input2', FRAME2_SECRET)],
    )
    def test_frame(self, browser_driver, frame_id, input_id, secret_text):
        """Open frame and check alert text.

        Args:
            browser_driver (WebDriver): The Selenium WebDriver instance.
            frame_id (str): The ID of the frame to switch to.
            input_id (str): The ID of the input field.
            secret_text (str): The secret text to enter into the input field.

        Raises:
            ValueError: If the alert message.
            WebDriverException: For error while interacting with the WebDriver.
        """
        try:

            browser_driver.switch_to.frame(frame_id)
            input_field = browser_driver.find_element(By.ID, input_id)
            input_field.send_keys(secret_text)
            browser_driver.find_element(
                By.XPATH, '//button[text()="Перевірити"]').click()

            # Verify alert message.
            alert = Alert(browser_driver)
            alert_text = alert.text
            if alert_text != 'Верифікація пройшла успішно!':
                error_message = (f'Verification failed in frame {frame_id}. '
                                 f'Expected success message but got: '
                                 f'{alert_text}')
                raise ValueError(error_message)
            alert.accept()

        except WebDriverException as error:
            error_message = (f'Error encountered during test in '
                             f'frame {frame_id}: {str(error)}')
            raise WebDriverException(error_message) from error

        finally:
            browser_driver.switch_to.default_content()
