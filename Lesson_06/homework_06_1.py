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
unique_symbols = set(entered_text.lower().replace(' ', ''))
_log.info(unique_symbols)

# Log into console info about unique symbols quantity.
# unique_symbols_quantity >= 10 ==> True
# unique_symbols_quantity < 10 ==> False
if len(unique_symbols) >= 10:
    _log.info(True)
else:
    _log.info(False)
