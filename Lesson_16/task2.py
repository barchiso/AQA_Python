"""Geometric exercise."""

# Task 2
# Create an abstract class "Figure" with abstract methods for obtaining area
# and perimeter.
# Inherit from it several ( > 2) other figures, and implement mathematically
# correct methods for area and perimeter for them.
# Properties of the type "side length" etc. should be private,
# and initialized through the constructor.
# Create several different objects of figures, and in a loop calculate
# and output to the console the area and perimeter of each.

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    """Abstract class to represent geometric figures.

    Args:
        ABC (class): Class for defining abstract classes.
    """

    @abstractmethod
    def obtaining_area(self):
        """Abstract method to be implemented by subclasses."""

    @abstractmethod
    def obtaining_perimeter(self):
        """Concrete method available to all subclasses."""


# Concrete subclass
class Square(Figure):
    """Class to represent a square.

    Args:
        Figure (class): Abstract class for figures.
    """

    def __init__(self, side):
        """Initialize a Square instance.

        Args:
            side (float): The length of one side of the square.
        """
        self.__side = side

    def obtaining_area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__side ** 2

    def obtaining_perimeter(self):
        """Calculate the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return self.__side * 4


# Concrete subclass
class Circle(Figure):
    """Class to represent a circle.

    Args:
        Figure (class): Abstract class for figures.
    """

    def __init__(self, radius):
        """Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = radius

    def obtaining_area(self):
        """Calculate the area of the circle.

        Returns:
            float: The perimeter (circumference) of the circle.
        """
        return pi * self.__radius ** 2

    def obtaining_perimeter(self):
        """Calculate the perimeter of the circle.

        Returns:
            float: The perimeter (circumference) of the circle.
        """
        return 2 * pi * self.__radius


# Concrete subclass
class Rhomb(Figure):
    """Class to represent a rhombus.

    Args:
        Figure (class): Abstract class for figures.
    """

    def __init__(self, side, diagonal1, diagonal2):
        """Initialize a Rhomb instance.

        Args:
            side (float): The length of one side of the rhombus.
            diagonal1 (float): The length of the first diagonal.
            diagonal2 (float): The length of the second diagonal.
        """
        self.__side = side
        self.__diagonal1 = diagonal1
        self.__diagonal2 = diagonal2

    def obtaining_area(self):
        """Calculate the area of the rhombus.

        Returns:
            float: The area of the rhombus.
        """
        return self.__diagonal1 * self.__diagonal2 / 2

    def obtaining_perimeter(self):
        """Calculate the perimeter of the rhombus.

        Returns:
            float: The perimeter of the rhombus.
        """
        return 4 * self.__side


if __name__ == '__main__':
    figures = [
        Square(5),
        Circle(3),
        Rhomb(6, 8, 5),
    ]

    for figure in figures:
        print(f'Figure: {figure.__class__.__name__}')
        print(f'  Area: {figure.obtaining_area():.2f}')
        print(f'  Perimeter: {figure.obtaining_perimeter():.2f}')
