"""Homework_09 task.

create list that will store such values
list_target = [(1,1), (3,4), (5,5), (7,0)]
"""

# we have two lists with equal or different size
# ex. l1=[1,3,5,7]  l2=[1,4,5]
# task:
# create list that will store such values
# list target: [(1,1), (3,4), (5,5), (7,0)]
# zero (0) is our default value that we set
# if no such element by index was found in certain list.
# code should work and vise versa
# ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce
# list target: [(1,1), (4,3), (5,5), (0,7)]
# your solution should include comprehension constructions
#
# Advices:
# set of (list1 indexes union list2 indexes) could be helpful
# to get larger indexes scope ( or use if-else)
# dict as you remember has default value if key was not found d1.get(key, 0)

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

l1 = [2, 4, 6, 8, 10]
l2 = [1, 2, 3]

l3 = [1, 2, 3]
l4 = [2, 4, 6, 8, 10]


def if_else_target_list(list1, list2):
    """Create list using (if-else) construction.

    Args:
        list1 (list): List #1 data.
        list2 (list): List #2 data.

    Returns:
        list: List with data from list1 and list2
              with default value zero (0) to handle missing indexes.
    """
    return [(list1[index] if index < len(list1) else 0,
             list2[index] if index < len(list2) else 0)
            for index in range(max(len(list1), len(list2)))]


target_list = f'Option #1 Output: {if_else_target_list(l1, l2)}'
_log.info(l1)
_log.info(l2)
_log.info(target_list)  # Output: [(2, 1), (4, 2), (6, 3), (8, 0), (10, 0)]


def set_dict_target_list(list1, list2):
    """Create list using set of indexes and dictionaries.get().

    Args:
        list1 (list): List #1 data.
        list2 (list): List #2 data.

    Returns:
        list: List with data from list1 and list2
              with default value zero (0) to handle missing indexes.
    """
    # Create a set of indexes from both lists.
    indexes_set = sorted(set(range(len(list1))).union(set(range(len(list2)))))

    # Create dictionaries for list1 and list2
    # with default value of 0 if index is out of range.
    d1 = {value: list1[value] for value in range(len(list1))}
    d2 = {value: list2[value] for value in range(len(list2))}

    # Construct list by using d1.get() and d2.get() to handle missing indexes.
    return [(d1.get(key, 0), d2.get(key, 0)) for key in indexes_set]


list_target = f'Option #2 Output: {set_dict_target_list(l3, l4)}'
_log.info(l3)
_log.info(l4)
_log.info(list_target)  # Output: [(1, 2), (2, 4), (3, 6), (0, 8), (0, 10)]
