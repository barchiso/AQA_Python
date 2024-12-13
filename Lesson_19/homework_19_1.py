"""Homework # 19.1. Mars Rover “Curiosity” photos."""

# There is an open NASA API that allows you to get JSON data about
# photos taken by the Curiosity rover on Mars based on certain parameters.
# Among this data are links to photos that need to be parsed and then,
# using additional queries, download and save
# these photos as local files mars_photo1.jpg, mars_photo2.jpg.
# The task needs to be done using the requests module
import json
import logging

import requests


def configure_logging():
    """Logger configuration.

    Returns:
        logging.Logger: Logging Logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(
        ('%(asctime)s.%(msecs)03d : %(module)-12s: '
         '%(lineno)3d %(levelname)-5s - %(message)s'),
        '%Y-%m-%d %H:%M:%S',
    )

    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    return logger


_log = configure_logging()


class MarsRoverPhotos:
    """A class to interact with NASA's Mars Rover Photos API.

    Attributes:
        url (str): The API endpoint URL.
        params (dict): Parameters to be sent with the API request.
        timeout (int): Timeout duration for HTTP requests in seconds.
    """

    def __init__(self, url, params):
        """Initialize the MarsRoverPhotos instance.

        Args:
            url (str): The API endpoint URL.
            params (dict): Parameters to be sent with the API request.
        """
        self.url = url
        self.params = params
        self.timeout = 5

    def fetch_photos(self):
        """Fetch photos metadata from NASA API."""
        try:
            # Send request to NASA API to get photos data
            response = requests.get(
                self.url, self.params, timeout=self.timeout)
            response.raise_for_status()  # Rase an exception if code is not 2xx

            # Get JSON data from response
            try:
                data = response.json()
                photos = data.get('photos')

                if photos:
                    self.download_photos(photos)
                else:
                    _log.info('No photos found.')

            except json.JSONDecodeError as error:
                error = 'Error serializing JSON: {error}'
                _log.error(error)
        except requests.exceptions.HTTPError as error:
            error = f'HTTP Error: {error}'
            _log.error(error)
        except requests.exceptions.ConnectionError as error:
            error = f'Connection Error: {error}'
            _log.error(error)
        except requests.exceptions.Timeout as error:
            error = f'Timeout Error: {error}'
            _log.error(error)
        except requests.exceptions.RequestException as error:
            error = f'Request failed: {error}'
            _log.error(error)

    def download_photos(self, photos):
        """Download photos from their URLs and saves them locally.

        Args:
            photos (list): List of photo metadata dictionaries.
        """
        for index, photo in enumerate(photos, start=1):
            img_url = photo.get('img_src')
            if img_url:
                self.save_image(img_url, index)
            else:
                message = f'Photo {index} has no image URL.'
                _log.info(message)

    def save_image(self, img_url, index):
        """Save an image locally from its URL.

        Args:
            img_url (str): URL of the image to download.
            index (int): Index for naming the file.
        """
        try:
            # Send a request to download the image
            img_response = requests.get(img_url, timeout=self.timeout)
            img_response.raise_for_status()
            with open(f'mars_photo{index}.jpg', 'wb') as img_file:
                img_file.write(img_response.content)
                message = f'Mars_photo{index}.jpg downloaded successfully.'
                _log.info(message)
        except requests.exceptions.HTTPError as error:
            error = f'HTTP Error: {error}'
            _log.error(error)
        except requests.exceptions.ConnectionError as error:
            error = f'Connection Error: {error}'
            _log.error(error)
        except requests.exceptions.Timeout as error:
            error = f'Timeout Error: {error}'
            _log.error(error)
        except requests.exceptions.RequestException as error:
            error = f'Request failed: {error}'
            _log.error(error)


if __name__ == '__main__':

    url1 = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params1 = {'api_key': 'DEMO_KEY', 'sol': 1000, 'camera': 'fhaz'}

    download_photos = MarsRoverPhotos(url1, params1)
    download_photos.fetch_photos()
