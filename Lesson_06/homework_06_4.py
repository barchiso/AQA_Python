"""Homework 06_2.

Sum of all EVEN numbers in this list.
"""

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


# There is some list with numbers input()
# Count sum of all EVEN numbers in this list.

# Creating list of numbers from entered by the user.
entered_numbers = []
while True:
    # Gather entered numbers by user.
    number = input('Enter a number or "exit" to stop: ')
    if number == 'exit':
        break  # exit the loop if user types 'exit'

    try:
        # Convert string into integer.
        number = int(number)
    except ValueError:
        # Message if invalid data is entered.
        print('Only numbers are valid.')
        continue  # Continue with new iteration if input was invalid.

    entered_numbers.append(number)  # add integer to the list.

_log.info(entered_numbers)  # displayed list of numbers.

# Calculate sum of all Even number in list 'entered_numbers.
even_numbers_sum = 0
for number in entered_numbers:
    if number % 2 == 0:
        even_numbers_sum += number

# Display calculated sum of all Even number in list 'entered_numbers.
sum_text = f'Even number sum is: {even_numbers_sum}'
_log.info(sum_text)
