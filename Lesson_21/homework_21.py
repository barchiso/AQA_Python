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


class HeartbeatAnalyzer:
    """Analyzes heartbeat differences in a log file."""

    TIME_FORMAT = '%H:%M:%S'
    WARNING_THRESHOLD = 31
    ERROR_THRESHOLD = 33

    def __init__(self, log_file, key, output_log='hb_test.log',
                 encoding='utf-8'):
        """Initialize the analyzer with log file details.

        Args:
            log_file (str): Path to the log file.
            key (str): Key to filter log lines.
            output_log (str): File to write the analysis logs.
            encoding (str): Encoding used for the log file.
        """
        self.log_file = log_file
        self.key = key
        self.encoding = encoding
        self.logger = self._configure_logging(output_log)

    @staticmethod
    def _configure_logging(log_file='hb_test.log'):
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

    def _get_filtered_log_lines(self):
        """Extract log lines containing the specified key.

        Returns:
            list: Filtered log lines.
        """
        with open(self.log_file, 'rt', encoding=self.encoding) as l_fh:
            log_file_lines = l_fh.readlines()

        return [line for line in log_file_lines if self.key in line]

    @staticmethod
    def extract_timestamp(line):
        """Extract the timestamp and converts it to a `datetime` object.

        Args:
            line (str): A line from the log file that contains the timestamp.

        Returns:
            datetime: A `datetime` object representing the timestamp.
        """
        start_index = line.find('Timestamp ') + len('Timestamp ')
        time_str = line[start_index:start_index + 8]  # Extract HH:MM:SS
        return datetime.strptime(time_str, HeartbeatAnalyzer.TIME_FORMAT)

    def analyze_log(self):
        """Perform the analysis of the log file."""
        filtered_list = self._get_filtered_log_lines()

        parsed_time_list = [self.extract_timestamp(
            line) for line in filtered_list]

        # Iterate through all timestamps in the list except the last one.
        # The loop stops at len(parsed_time_list) - 1
        # because each iteration compares the current timestamp
        # with the next one (i + 1), which would cause an
        # IndexError if i reached the last element.
        for i in range(len(parsed_time_list) - 1):
            current_time = parsed_time_list[i]
            next_time = parsed_time_list[i + 1]
            self.log_difference(current_time, next_time)

    def log_difference(self, time_a, time_b):
        """Compare two timestamps and logs an error or warning.

        Args:
            time_a (datetime): The first timestamp to compare.
            time_b (datetime): The second timestamp to compare.

        Returns:
            float: The time difference in seconds between the two timestamps.
        """
        time_difference = (time_a - time_b).total_seconds()

        time_a_str = time_a.strftime(self.TIME_FORMAT)
        time_b_str = time_b.strftime(self.TIME_FORMAT)

        if time_difference >= self.ERROR_THRESHOLD:
            message = (f'Heartbeat between {time_a_str} and '
                       f'{time_b_str} is {time_difference} seconds. '
                       f'Greater than {self.ERROR_THRESHOLD} seconds.')
            return self.logger.error(message)
        if self.WARNING_THRESHOLD < time_difference < self.ERROR_THRESHOLD:
            message = (f'Heartbeat between {time_a_str} and '
                       f'{time_b_str} is {time_difference} seconds. '
                       f'Greater than {self.WARNING_THRESHOLD} seconds.')
            return self.logger.warning(message)

        return time_difference


if __name__ == '__main__':
    log_analyzer = HeartbeatAnalyzer(
        log_file='hblog.txt',
        key='Key TSTFEED0300|7E3E|0400',
    )

    # Perform the analysis
    log_analyzer.analyze_log()
