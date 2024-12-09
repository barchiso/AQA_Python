"""Homework # 17. Find and fix the error in the watch module."""

# There is a module with a suboptimal and erroneous code.
# Your task is to find and correct errors in the module.
# Execution stroke: Download the repository of the randominfo.zip module
# Copy to folder on your computer
# Open the folder in the new IDE project Create a test.py file in the project.
# Run the file and get an error Fix the error and run into your own branch.

# Steps to fix errors:
# 1. Install next modules pytz and PIL(Pillow).
# pip install pytz
# pip install Pillow
# 2. Override the original `get_country` and `get_address` functions
# that has default value if empty.

import csv
from random import choice

import randominfo


# Override the original `get_country` with default value if empty.
def get_country_with_default(first_name=None):
    """Fetch the country based on the first name or use a default if not found.

    Args:
        first_name (str, optional): The first name to search for in the CSV.

    Returns:
        str: The country for the given first name, or 'USA' if not found.
    """
    country_file = csv.reader(
        open('randominfo/data.csv', 'r', encoding='utf-8'))
    country = ''
    if first_name is not None:
        for data in country_file:
            if data[0] != '' and data[0] == first_name:
                country = 'Unknown Country'  # Default country
    return country


# # # Override the original `get_address` with default value if empty.
def get_address_with_default():
    """Generate an address with fallback to "Unknown" if any field is empty.

    Returns:
        dict: A dictionary containing address components.
    """
    full_addr = []
    addr_param = ['street', 'landmark', 'area',
                  'city', 'state', 'pin code', 'country']
    for i in range(4, 11):
        # Adjust the file path as necessary
        addr_file = csv.reader(
            open('randominfo/data.csv', 'r', encoding='utf-8'))
        all_addresses = []
        for addr in addr_file:
            try:
                if addr[i] != '':
                    all_addresses.append(addr[i])
            except IndexError:
                pass
        # Add check if all_addresses is empty, append "Unknown" if true
        # first_name = data[0] != '' and data[0] == first_name
        if not all_addresses:
            all_addresses.append('Unknown Country')
        full_addr.append(choice(all_addresses))

    full_addr = dict(zip(addr_param, full_addr))
    return full_addr


# # # Override the original `get_country` and `get_address` functions.
randominfo.get_country = get_country_with_default
randominfo.get_address = get_address_with_default


person = randominfo.Person()

print(person.full_name, person.gender, person.country, person.address)
