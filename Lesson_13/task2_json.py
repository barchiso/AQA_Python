"""Validate all JSON files.

Validate that all files in the ideas_for_test/work_with_json folder
are valid json. Output the result for an invalid file through the logger
at the error level to the file json__<your_second_name>.log.
"""
import json
from pathlib import Path

from logger import configure_logging

_log = configure_logging(log_file='json_result.log')


def validate_folder_exists(folder_path):
    """Check if the folder exists and is valid.

    Args:
        folder_path (str): Path to folder with files.

    Raises:
        FileNotFoundError: Error if folder isn't found.
    """
    if not folder_path.is_dir():
        raise FileNotFoundError(
            f'Error: The folder {folder_path} does not exist.')


def validate_json_file(file_path):
    """Validate a single JSON file.

    Args:
        file_path (str): Path to folder with files.

    Returns:
        str: Path to folder with files.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as json_file:
            json.load(json_file)  # Attempt to load the file as JSON
            message = f'JSON file is valid: {file_path}'
            _log.info(message)
            return ''

    except json.JSONDecodeError as j_err:
        error = f'Invalid JSON in file: {file_path}. Error: {j_err}'
        _log.error(error)
    except Exception as ex:
        error = f'Unexpected error with file {file_path}: {ex}'
        _log.error(error)
    return ''


def validate_json_files(folder_path):
    """Validate JSON files in a folder.

    Args:
        folder_path (str): Path to folder with files.

    Returns:
        str: Path to folder with files.
    """
    validate_folder_exists(folder_path)

    results = {
        'valid_files': [],
        'invalid_files': [],
    }

    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix == '.json':
            (results['valid_files'] if validate_json_file(file_path)
             else results['invalid_files']).append(file_path)
            # >>> if validate_json_file(file_path):
            #     >>>> results['valid_files'].append(file_path)
            # >>> else:
            #     >>> results['invalid_files'].append(file_path)

    return results


folder = Path('ideas_for_test/work_with_json')

validate_json_files(folder)
