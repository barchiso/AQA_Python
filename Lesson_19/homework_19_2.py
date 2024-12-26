"""Homework # 19.2. POST/GET/DELETE."""

# In the Python venv, install Flask using the pip install flask command
# Create a file app.py in a separate directory and copy the code of the app.py
# file that is given below in the initial data into it.
# Start the http server using the python app.py command
# The server starts at the base address http: // 127.0.0.1: 8080
# Given the documentation given below, you need to write code
# that will use the request module to POST an image to the server,
# use GET to get a link to this file,
# and then use DELETE to delete the file from the server

import requests


# POST method
# image: image file (type MIME: image/*)
# Status code : 201 (Created)
# Response: Image file URL in JSON format
def upload_image(api_url, image, timeout):
    """Upload an image to the server using the POST method.

    Args:
        api_url (str): The API endpoint for uploading images.
        image (str): Path to the image file to be uploaded.
        timeout (int): Timeout duration for the request in seconds.

    Returns:
        str: URL of the uploaded image.
    """
    with open(image, 'rb') as image_fl:
        files = {'image': image_fl}
        response = requests.post(api_url, files=files,
                                 timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(f'Uploaded successfully: {response.json().get("image_url")}')
        return response.json().get('image_url')


# GET method
# Status code : 200 (OK)
# Response: Image file URL in JSON format if Content-Type equal text
# Response: Image itself if Content-Type is equal to image.
def get_image(api_url, filename, headers, timeout):
    """Retrieve an image or its URL from the server using the GET method.

    Args:
        api_url (str): The API endpoint for retrieving images.
        filename (str): Name of the file to retrieve.
        headers (dict): Request headers to specify content type.
        timeout (int): Timeout duration for the request in seconds.

    Returns:
        Union[dict, bytes]: JSON if content type is text, or image data.
    """
    url = f'{api_url}/{filename}'
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()     # Raises HTTPError for bad responses
    if response.headers.get('Content-Type') == 'image/jpeg':
        # By default image is saved only in: <flask_app_folder>/uploads/<image>
        print(f'Image saved in: <flask_app_folder>/uploads/{filename}')
        return response.content

    print(f'Image URL: {response.json().get("image_url")}')
    return response.json()


# DELETE method
# Status code : 200 (OK)
# Response: a message about successful deletion in JSON format
def delete_image(api_url, filename, timeout):
    """Delete an image from the server using the DELETE method.

    Args:
        api_url (str): The API endpoint for deleting images.
        filename (str): Name of the file to delete.
        timeout (int): Timeout duration for the request in seconds.

    Returns:
        dict: JSON response indicating successful deletion.
    """
    url = f'{api_url}/{filename}'
    response = requests.delete(url, timeout=timeout)
    response.raise_for_status()  # Raises HTTPError for bad responses
    # Deletion from: <flask_app_folder>/uploads/<image>
    print(f'Deleted successfully: {response.json().get("message")}')
    return response.json()


if __name__ == '__main__':
    set_timeout = 5
    image_url = 'data_to_upload/squirrel.jpg'
    image_file = image_url.rsplit('/', maxsplit=1)[-1]
    post_url = 'http://127.0.0.1:8080/upload'
    get_url = 'http://127.0.0.1:8080/image'
    delete_url = 'http://127.0.0.1:8080/delete'
    content_type = [{'Content-Type': 'text'}, {'Content-Type': 'image'}]

    try:
        upload_image(post_url, image_url, set_timeout)

        for item in content_type:
            print(f'Content-Type is: {item.get("Content-Type")}')
            get_image(get_url, image_file, item, set_timeout)

        delete_image(delete_url, image_file, set_timeout)

    except requests.exceptions.RequestException as error:
        print(f'Error occurred while fetching the image: {error}')
