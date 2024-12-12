"""Homework # 18 Each iterator and decorator generator."""

# Generators:
# Write a generator that returns a sequence of even numbers from 0 to N.
# Write a generator that generates a Fibonacci sequence to a specific N number.
# Iterators:
# Implement an iterator to reverse list items.
# Write an iterator that returns all even numbers in the range from 0 to N.
# Decorators:
# Write a decorator that logs the arguments and results of the called function.
# Write a decorator that intercepts and processes exceptions
# that occur during the performance of the function.
from functools import wraps

# Iterators:
# R0903: Too few public methods (1/2) (too-few-public-methods)


class ReversedList:
    """Iterate reverse list of items."""

    def __init__(self, data):
        """Initialize the ReversedList with a given list and reverses it.

        Args:
            data (list): The list to be reversed.
        """
        self.data = data
        self.data.reverse()  # Reverse the list

    def __iter__(self):
        """Iterate over the reversed list.

        Returns:
            iter: An iterator for the reversed list.
        """
        return iter(self.data)  # Return an iterator for the reversed list


# R0903: Too few public methods(1/2)(too-few-public-methods)
class EvenNumbers:
    """Iterate all even numbers in the range from 0 to N."""

    def __init__(self, max_num):
        """Initialize the EvenNumbers iterator with a maximum number.

        Args:
            max_num (int): The max_num up to which even numbers are returned.
        """
        self.max_num = max_num

    def __iter__(self):
        """Iterate from 0 to the max_num and yields even numbers.

        Yields:
            int: Even numbers in the range from 0 to the specified max_num.
        """
        for num in range(self.max_num + 1):
            if num % 2 == 0:
                yield num


# Generators:
def even_numbers_sequence(numbers):
    """Generate a sequence of even numbers from 0 to N.

    Args:
        numbers (int): The maximum number in the range (inclusive).

    Yields:
        int: The next even number in the sequence.
    """
    for num in range(numbers + 1):
        if num % 2 == 0:
            yield num


def fibonacci_sequence(nums):
    """Generate a Fibonacci sequence to a specific N number.

    Args:
        nums (int): The maximum value for the Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    start, end = 0, 1
    while start <= nums:
        yield start
        start, end = end, start + end


# Decorators:
def log_arguments_and_results(func):
    """Decorate output of the arguments and results of the called function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with exception handling.
    """
    @wraps(func)
    def wrapper(*args):
        print(f'Function {func.__name__} with arguments: {args}')
        result = func(*args)
        print(f'Function {func.__name__} result: {result}')
        return result
    return wrapper


def errors_handler(func):
    """Decorate intercepts and handle errors if occurs.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with exception handling.
    """
    @wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as error:
            return error
    return wrapper


@log_arguments_and_results
@errors_handler
def division(numerator, denominator):
    """Divides two numbers.

    Args:
        numerator (float): The numerator.
        denominator (float): The denominator.

    Returns:
        float: The result of the division.
    """
    return numerator // denominator


@log_arguments_and_results
@errors_handler
def greet(name, age=None):
    """Greets a person.

    Args:
        name (str): The name of the person to greet.
        age (int, optional): The age of the person. Defaults to None.

    Raises:
        ValueError: If `age` is provided but is not an integer.

    Returns:
        str: A greeting message containing the name and age of the person.
    """
    if age is not None and not isinstance(age, int):
        raise ValueError('Age must be an integer.')
    return f'Hello, {name}! Your age is {age}.'


if __name__ == '__main__':

    num_list = [1, 2, 3, 4, 5]
    names_list = ['Johnny', 'Lenny', 'Jimmy', 'Timmy']
    n_number = 20

    print('Testing iterators:')
    print(f'Reversed list iterator {num_list}.')
    reverse_numbers = ReversedList(num_list)
    for item in reverse_numbers:
        print(item)

    print(f'\nReversed list iterator {names_list}.')
    reverse_names = ReversedList(names_list)
    for item in reverse_names:
        print(item)

    print(f'\nEven Numbers iterator from 0 to {n_number}.')
    even_iter = EvenNumbers(n_number)
    for even_num in even_iter:
        print(even_num)

    print('\nTesting generators:')
    print(f'Even numbers generator from 0 to {n_number}.')
    for even in even_numbers_sequence(n_number):
        print(even)

    print(f'\nFibonacci sequence generator to {n_number}.')
    for fib in fibonacci_sequence(n_number):
        print(fib)

    print('\nTesting decorators:')
    division(20, 2)  # Should log arguments and result
    division(10, 0)  # Should log the exception
    greet('Alice', 20)   # Normal execution
    greet('Alice')   # Normal execution with default age
    greet('Alice', 'twenty')  # Triggers ValueError
