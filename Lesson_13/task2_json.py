"""Validate all JSON files.

Validate that all files in the ideas_for_test/work_with_json folder
are valid json. Output the result for an invalid file through the logger
at the error level to the file json__<your_second_name>.log.
"""
import json
from pathlib import Path

from logger import configure_logging

_log = configure_logging(log_file='json_result.log')


def validate_json_files(folder_path):
    """Validate JSON files in folder.

    Args:
        folder_path (str): Path to folder with files.

    Raises:
        FileNotFoundError: Error if folder isn't found.

    Returns:
        str: Path to folder with files.
    """
    if not folder_path.is_dir():
        raise FileNotFoundError(
            f'Error: The folder {folder_path} does not exist.')

    for file_path in folder_path.iterdir():
        if file_path.is_file():
            try:
                with open(file_path, mode='r', encoding='utf-8') as json_file:
                    # Attempt to load the file as JSON
                    json.load(json_file)
                    message = f'JSON file is valid: {file_path}'
                    _log.info(message)

            except json.decoder.JSONDecodeError as j_err:
                error = f'Invalid JSON in file: {file_path}. Error: {j_err}'
                _log.error(error)
            except Exception as j_err:
                # Log any other unexpected errors
                error = f'Unexpected error with file {file_path}: {j_err}'
                _log.error(error)

    return folder_path


folder = Path('ideas_for_test/work_with_json')

validate_json_files(folder)
