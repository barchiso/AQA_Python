"""Search Automobile.

Solutions for homework_05.1.
"""

import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)


# Exists some car data with color, year, engine_volume, car type , price.
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements.
car_data = {'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
            'Audi': ('black', 2020, 2.0, 'sedan', 55000),
            'BMW': ('white', 2018, 3.0, 'suv', 70000),
            'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
            'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
            'Honda': ('red', 2017, 1.5, 'sedan', 30000),
            'Ford': ('green', 2019, 2.3, 'suv', 40000),
            'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
            'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
            'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
            'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
            'Kia': ('white', 2020, 2.0, 'sedan', 28000),
            'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
            'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
            'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
            'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
            'Jeep': ('green', 2021, 3.0, 'suv', 50000),
            'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
            'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
            'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
            'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
            'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
            'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
            'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
            'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
            'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
            'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
            'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
            'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
            'Acura': ('white', 2017, 2.4, 'suv', 40000),
            'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
            'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
            'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
            'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
            'Ram': ('black', 2019, 5.7, 'pickup', 40000),
            'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
            'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
            'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
            'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000),
            }

# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
search_criteria = (2017, 1.6, 36000)
year, engine_vol, price = search_criteria


# Option 01.
def is_valid_dict_value(value):
    """Check if condition is valid.

    Args:
        value (integer or float): data from search_criteria

    Returns:
        boolean: True or False
    """
    return value[1] >= year and value[2] >= engine_vol and value[4] <= price


# write code that will help us to get cars that satisfy search_criteria.
# Create new dictionary filtrated by search_criteria value condition.
filtered_cars = {key: val for key, val in car_data.items()
                 if is_valid_dict_value(val)}

# Sort by price ascending.
# We should print up to five (5) first found elements
cars = sorted(filtered_cars.items(), key=lambda value: value[1][4])

# display up to five (5) first found elements.
dict_result = f'OPTION # 1: {dict(cars[:5])}'
_log.info(dict_result)


# Option 02.
def is_valid_l_value(val):
    """Check if condition is valid.

    Args:
        val (integer or float): data from search_criteria

    Returns:
        boolean: True or False
    """
    return val[1][1] >= year and val[1][2] >= engine_vol and val[1][4] <= price


# Create new list and sort by price ascending.
filtered_cars_list = sorted(car_data.items(), key=lambda value: value[1][4])

# Filter created list by search_criteria values.
cars_list = [val for val in filtered_cars_list if is_valid_l_value(val)]

# Display up to five (5) first found elements.
list_result = f'OPTION # 2: {dict(cars_list[:5])}'
_log.info(list_result)
