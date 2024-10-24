"""Homework 06_2.

Wait for letter.
"""

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

# Create a loop that will prompt the user to enter a word
# that contains the letter 'h' (both large and small are considered)
# The loop shouldn't terminate if entered word is without the letter 'h'.
while True:
    word = input('Enter word: ')
    if 'h' in word.lower():
        _log.info('Letter "h" or "H" is in word.')
        break
