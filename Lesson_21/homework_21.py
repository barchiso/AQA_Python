"""Homework #21. Testing the "heartbeat" time."""

# The client's monitoring system sends a signal that it is operational
# every 30-31 seconds - for example, Timestamp 05:45:40,
# and in the next message - Timestamp 05:45:09
# (here the heartbeat difference is 31 seconds)
#
# There are several duplicate streams that send data simultaneously,
# so we can analyze only one stream - Key TSTFEED0300|7E3E|0400

# Using automation tools, analyze the log provided to us: hblog.txt

# 1. Select only lines with the specified key Key TSTFEED0300|7E3E|0400

# 2. Create a function that will return a log file
# where the correctness of the requirements will be analyzed:
# a) for each case where heartbeat is more than 31 seconds but less than 33,
# log WARNING to the hb_test.log file
# b) for each case where heartbeat is more than exactly 33,
# log ERROR to the hb_test.log file

# 3. Please note that for error analysis it would be good
# for us to know the time at which the error occurred.

# Be sure to include the result of the work - the hb_test.log file in the PR.

import logging
from datetime import datetime


def configure_logging(log_file='hb_test.log'):
    """Logger configuration.

    Args:
        log_file (str): The name of log file where logs will be written.

    Returns:
        logging.Logger: Logging Logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a formatter for the logs
    log_formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d : %(module)-12s:%(lineno)3d'
        ' %(levelname)-7s - %(message)s',
        '%Y-%m-%d %H:%M:%S',
    )

    # Create a handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(log_formatter)

    # Create a handler for logging to file
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


_log = configure_logging()


def analyze_log(log_file, encoding='utf-8', key='Key TSTFEED0300|7E3E|0400'):
    """Parse and analyze log file.

    Args:
        log_file (str): The path to the log file to be analyzed.
        encoding (str, optional): The encoding used to read the log file.
        key (str, optional): The key to filter the lines from the log file.
    """
    with open(log_file, 'rt', encoding=encoding) as l_fh:
        log_file_lines = l_fh.readlines()

    filtered_list = [line for line in log_file_lines if key in line]

    parsed_time_list = [extract_timestamp(line) for line in filtered_list]

    for i in range(len(parsed_time_list) - 1):
        current_time = parsed_time_list[i]
        next_time = parsed_time_list[i + 1]
        log_difference(current_time, next_time)


def extract_timestamp(line):
    """Extract the timestamp and converts it to a `datetime` object.

    Args:
        line (str): A line from the log file that contains the timestamp.

    Returns:
        datetime: A `datetime` object representing the timestamp.
    """
    start_index = line.find('Timestamp ') + len('Timestamp ')
    time_str = line[start_index:start_index + 8]  # Extract HH:MM:SS
    return datetime.strptime(time_str, '%H:%M:%S')


def log_difference(time_a, time_b):
    """Compare two timestamps and logs an error or warning.

    Args:
        time_a (datetime): The first timestamp to compare.
        time_b (datetime): The second timestamp to compare.

    Returns:
        float: The time difference in seconds between the two timestamps.
    """
    time_difference = (time_a - time_b).total_seconds()

    time_a_str = time_a.strftime('%H:%M:%S')
    time_b_str = time_b.strftime('%H:%M:%S')

    if time_difference >= 33:
        message = (f'Heartbeat between {time_a_str} and '
                   f'{time_b_str} is {time_difference} seconds. '
                   f'Greater than 33 seconds.')
        return _log.error(message)
    if 31 < time_difference < 33:
        message = (f'Heartbeat between {time_a_str} and '
                   f'{time_b_str} is {time_difference} seconds. '
                   f'Greater than 31 seconds.')
        return _log.warning(message)

    return time_difference


if __name__ == '__main__':
    analyze_log('hblog.txt')
