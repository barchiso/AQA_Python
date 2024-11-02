"""HW 8.1. Catch incorrect characters in the list of numbers."""
# Create array(list) with strings, which contains numbers separated by coma.
# Example: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# For each list element display sum of all numbers (create new function).
# You need to catch exception and display 'Can't do it!',
# if there area symbols which aren't numbers (”qwerty1,2,3” in example).
# Use try\except block, to avoid characters other than numbers in the list.
# Correct display for this example should be - 10, 60, 'Can't do it!'.

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


def gather_data():
    """Gather entered data by user.

    Returns:
        list: List of entered data by user.
    """
    entered_list = []

    while True:
        entered_data = input('Enter numbers separated by commas or "exit"'
                             'to stop: ')
        if entered_data.lower() == 'exit':
            break
        entered_list.append(entered_data)  # Add data to the list.

    return entered_list


def sum_of_all_numbers(list_with_data):
    """Calculate sum of all numbers in entered list element.

    Args:
        list_with_data (list): List with entered by user data.

    Returns:
        list: List with displayed list element sum.
    """
    result = []
    for element in list_with_data:
        try:
            # Convert string into integer.
            result.append(sum(int(number) for number in element.split(',')))
        except ValueError:
            # Message if invalid data is entered.
            result.append("Can't do it!")
    return result


# Optimized option.
def element_list_division(data_element_string):
    """Sum of all numbers in element.

    Args:
        data_element_string (list): Element list.

    Returns:
        int: Calculation sum of all numbers in element list.
        string: Sting if error occurs.
    """
    try:
        # Convert string into integer.
        return sum(int(num) for num in data_element_string.split(','))
    except ValueError:
        return "Can't do it!"  # Message if invalid data is entered.


def optimized_sum_list(data_list):
    """Optimized sum calculation of all numbers by element in entered list.

    Args:
        data_list (list): List with entered by user data.

    Returns:
           list: List with displayed list element sum.
    """
    return [element_list_division(elm) for elm in data_list]


new_list = gather_data()
example_list = ['1,2,3,4', '1,2,3,4, 50', 'qwerty1,2,3']

_log.info(new_list)  # displayed entered_list data.
# Display entered list with non-optimized function.
_log.info(sum_of_all_numbers(new_list))
# Display entered list with non-optimized function.
_log.info(optimized_sum_list(new_list))

_log.info(example_list)  # displayed example_list data.
# Display example list with non-optimized function.
_log.info(sum_of_all_numbers(example_list))
# Display example list with non-optimized function.
_log.info(optimized_sum_list(example_list))
