"""Compare two CSV files.

Take two files from the ideas_for_test/work_with_csv folder,
compare them for duplicates and remove them.
Write the result in the result_<your_second_name>.csv file.
"""

import csv
from pathlib import Path

from logger import configure_logging

_log = configure_logging(log_file='csv_result.log')


def read_from_csv(path_file, encoding='utf-8'):
    """Read a CSV file and returns its data as a list of dictionaries.

    Args:
        path_file (str): Path to the CSV file.
        encoding (str, optional): The encoding used to decode the file.

    Returns:
        list[dict]: List of rows as dictionaries.
    """
    try:
        with open(path_file, mode='r', encoding=encoding) as csv_file:
            # Read content from the file.
            content = csv_file.read()
            # Replace semicolons with comas to delimiters standards.
            # The rmc.csv file delimiters are displayed as semicolons.
            content = content.replace(';', ',')
            # Return content to csv file rows formats
            csv_file = content.splitlines()

            # Read csv file and returns its data as a list of dictionaries.
            reader = csv.DictReader(csv_file)

            # Verify file's headers are valid
            if not reader.fieldnames:
                raise ValueError(
                    f'The CSV file "{path_file}" is empty or has no headers.')

            # Check if the file has valid headers
            data = [{key: value for key, value in row.items() if key.strip()}
                    for row in reader]

            if not data:
                raise ValueError(
                    f'The CSV file {path_file} has no data lines.',
                )

            return data  # If success.

    except FileNotFoundError:
        error = f'Error: The specified CSV file "{path_file}" does not exist.'
        _log.error(error)
    except ValueError as e:
        error = f'Data Error: {e}'
        _log.error(error)
    except csv.Error as e:
        error = f'CSV Parsing Error: {e}'
        _log.error(error)
    except Exception as e:
        error = f'An unexpected error occurred: {e}'
        _log.error(error)

    return error  # If any errors occurred.


def write_to_csv(path_file, data, fieldnames, encoding='utf-8'):
    """Write into CSV file.

    Args:
        path_file (str): Path to the CSV file.
        data (list[dict]): List of rows to be written as dictionaries.
        fieldnames (list[str]): List of column headers for the CSV file.
        encoding (str, optional): The encoding used to decode the file.

    Returns:
        str: Path to the CSV file.
        None: Logs a success message if writing is successful;
        logs an error otherwise.
    """
    try:
        with open(
            path_file, mode='w', encoding=encoding, newline='',
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(data)
        message = f'Data successfully written to file: "{path_file}".'
        _log.info(message)

        return path_file  # If success.

    except Exception as e:
        error = f'An unexpected error occurred: {e}'
        _log.error(error)

    return error  # If any errors occurred.


def compare_csv_files(file1, file2, output_file):
    """Compare two CSV files.

    Removes duplicates and writes the result to a new file.

    Args:
        file1 (str): Path to the CSV file.
        file2 (str): Path to the CSV file.
        output_file (str): Path to the CSV file.

    Returns:
        None: Logs the result of the comparison or any encountered errors.
        boolean: True if success, False if any errors occurs.
    """
    try:
        # Read csv files into list of dictionaries.
        data1 = read_from_csv(file1)
        data2 = read_from_csv(file2)

        if not data1 or not data2:
            raise ValueError(
                'One or both files are empty. No operation performed.')

        # Get headers (assume headers are the same for both files)
        fieldnames = data1[0].keys()
        if fieldnames != data2[0].keys():
            raise ValueError('Headers of the two files do not match.')

        # Find and remove duplicates by converting to sets of tuples.
        unique_data = {tuple(row.items()) for row in data1} | (
            {tuple(row.items()) for row in data2})

        # Convert back to list of dictionaries.
        result_data = [dict(row) for row in unique_data]

        # Write results to the output file.
        message = f'CSV files: "{file1}" and "{file2}" were compared.'
        _log.info(message)
        result = write_to_csv(output_file, result_data, fieldnames)

        return result  # If success.

    except FileNotFoundError as fnf_error:
        error = f'File error: {fnf_error}'
        _log.error(error)
    except ValueError as value_error:
        error = f'Data error: {value_error}'
        _log.error(error)
    except Exception as e:
        error = f'Unexpected error: {e}'
        _log.error(error)

    return error  # If any errors occurred.


# Paths to the files
file1_path = 'ideas_for_test/work_with_csv/random.csv'
file2_path = 'ideas_for_test/work_with_csv/random-michaels.csv'
file11_path = Path('ideas_for_test/work_with_csv/rmc.csv')
file22_path = Path('ideas_for_test/work_with_csv/r-m-c.csv')

output_path = 'ideas_for_test/work_with_csv/result.csv'
output_path2 = Path('ideas_for_test/work_with_csv/result2.csv')

# Run the function
compare_csv_files(file1_path, file2_path, output_path)
compare_csv_files(file11_path, file22_path, output_path2)
