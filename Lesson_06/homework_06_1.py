"""Homework 06_1.

String unique symbols count.
"""

# Count unique symbols quantity in string.
# If symbols quantity is grater than 10 - print True, vice-versa - False.
# Get string from input function.

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


# Get some string.
entered_text = input('Enter some text: ')
_log.info(entered_text)

# Get unique symbols from the string.
# unique_symbols_quantity >= 10 ==> True
# unique_symbols_quantity < 10 ==> False
unique_symbols = len(set(entered_text.lower().replace(' ', ''))) > 10

# Log into console info about unique symbols quantity.
_log.info(unique_symbols)
