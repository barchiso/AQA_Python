"""Homework 06_3.

Get what needed from the list.
"""

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

# List with data: lst1 =
# '1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'
# Create new list only with string variables from the first list.
# Data in list could be any.


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'LoremIpsum']

# Create new list only with string variables from the first list.
lst2 = [data for data in lst1 if isinstance(data, str)]
_log.info(lst2)
