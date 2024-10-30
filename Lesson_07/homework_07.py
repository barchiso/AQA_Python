"""Homework 07."""


# task 1
# Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
def multiplication_table(number):
    """Multiply number.

    Args:
        number (int): Integer number
    """
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + 'x' + str(multiplier) + '=' + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
# Написати функцію, яка обчислює суму двох чисел.
def sum_numbers(number1, number2):
    """Two numbers sum.

    Args:
        number1 (int): First number
        number2 (int): Second number

    Returns:
        int: sum of two numbers
    """
    return number1 + number2


sum_result = sum_numbers(4, 8)


# task 3
# Написати функцію, яка розрахує середнє арифметичне списку чисел.
def average_value(numbers_list):
    """Average value of numbers in list.

    Args:
        numbers_list (list): List of numbers

    Returns:
        float: List of numbers average value
    """
    return sum(numbers_list) / len(numbers_list)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average_result = average_value(numbers)


# task 4
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reversed_string(test_string):
    """Reverse somme string.

    Args:
        test_string (string): Some text

    Returns:
        string: Reversed string
    """
    return test_string[::-1]


txt = 'Hello World!'
reversed_txt = reversed_string(txt)


# task 5
# Написати функцію, яка приймає список слів
# та повертає найдовше слово у списку.
def max_word(word_list):
    """Find word with maximum length from the list.

    Args:
        word_list (list): List of words

    Returns:
        string: Word with maximum length
    """
    return max(str(word_list), key=len)


words = ['automobile', 'hi', 'pencil', 'Hello', 1]
word_result = max_word(words)


# task 6
# Написати функцію, яка приймає два рядки та повертає індекс першого входження
# другого рядка у перший рядок, якщо другий рядок є підрядком першого рядка,
# та -1, якщо другий рядок не є підрядком першого рядка.
def find_substring(str1, str2):
    """First entry of the second line into the first line.

    Args:
        str1 (string): First string
        str2 (string): Second string

    Returns:
        int: Index of the first entry
    """
    return str1.find(str2)


string1 = 'Hello, world!'
string2 = 'world'
print(find_substring(string1, string2))  # поверне 7

string1 = 'The quick brown fox jumps over the lazy dog'
string2 = 'cat'
print(find_substring(string1, string2))  # поверне -1


# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# task 7
# Calculate unique symbols in the string.
def unique_symbols_quantity(text):
    """Calculate unique symbols in text.

    Args:
        text (string): Some text

    Returns:
        int: Quantity of unique symbols
    """
    return len(set(text.lower().replace(' ', '')))


entered_text = 'The quick brown fox jumps over the lazy dog'
unique_symbols = unique_symbols_quantity(entered_text)


# task 8
# Calculate sum of all Even number in list 'entered_numbers.
def even_number(numbers_list):
    """Calculate sum of all even numbers.

    Args:
        numbers_list (list): List of numbers.

    Returns:
        int: Sum of even numbers.
    """
    return sum(number for number in numbers_list if number % 2 == 0)


numbers2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
even_sum = even_number(numbers2)


# task 9
# Date formatted string.
# Create function which get date as: Day, Month, Year and by default '.'
# Function should return string in format 'day.month.year'
# If user's separator differs from default
# it should return string '15/03/2023'
def date_format(*args, sep='.'):
    """Date formatted string.

    Args:
        args (tuple): Tuple with three inputs: Day, Month, Year
        sep (str, optional): _description_. Defaults to ".".

    Returns:
        string: date in formatted string
    """
    return sep.join(str(arg) for arg in args)


date_string1 = date_format(22, 11, 2003)
date_string2 = date_format(11, 'April', 2003, sep='/')

# task 10
# Create function which compare two dictionaries with students courses grades.
# Function should compare grades for each course
# and return dictionary with grades difference for each student.
# Student should n't be displayed, if student isn't in both dictionaries.
grades_1 = {'John Smith': 90, 'Will Smith': 85, 'Katy Perry': 78,
            'Jeniffer Aniston': 99}
grades_2 = {'John Smith': 92, 'Will Smith': 87, 'Katy Perry': 80}


def compare_grades(grades1, grades2):
    """Compare students grades.

    Args:
        grades1 (int): Student grade from first dictionary.
        grades2 (_type_): Student grade from second dictionary.

    Returns:
        dict: Dictionary {'student': grade difference}
    """
    key_set = set(grades1.keys()) and set(grades2.keys())
    diff = {}
    for key in key_set:
        diff[key] = grades1[key] - grades2[key]
    return diff


grades_result = compare_grades(grades_1, grades_2)


# Create function which checks if number is prime.
def is_prime_number(number):
    """Check if number is PRIME.

    Args:
        number (integer): any number

    Returns:
        boolean: True or False
    """
    return (number > 1 and not any(number % i == 0
                                   for i in range(2, int(number ** 0.5) + 1)))


is_prime_result = is_prime_number(7)
print(is_prime_result)
