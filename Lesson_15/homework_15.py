"""Create a class called "Rhomb".

Create a geometric shape class "Rhomb".
The class must have the following attributes:
- side_a(length of side a).
- angle_a(angle between sides a and b).
- angle_b(adjacent to angle angle_a).
The following requirements must be implemented:
- The value of side side_a must be greater than 0.
- The angles angle_a and angle_b must satisfy the condition:
angle_a + angle_b = 180
- The opposite angles of a rhombus are always equal, so when the value of
angle_a is given, the value of angle_b is calculated automatically.

Use the "__setattr__" method to set the values of the attributes,
"""
import logging


def configure_logging():
    """Logger configuration.

    Returns:
        logging.Logger: Logging Logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_formatter = logging.Formatter(
        ('%(asctime)s.%(msecs)03d : %(module)-12s: '
         '%(lineno)3d %(levelname)-5s - %(message)s'),
        '%Y-%m-%d %H:%M:%S',
    )

    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    return logger


_log = configure_logging()


class Rhomb:
    """Class to represent a rhombus data."""

    def __init__(self, side_a, angle_a):
        """Initialize the rhombus with side length and an internal angle.

        Args:
            side_a (float): Rhombus side length.
            angle_a (float): Rhombus angle between two adjacent sides.
        """
        self.angle_b = None
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name: str, value):
        """Validate and set attributes dynamically.

        Args:
            name (str): The name of the attribute being set.
            value (Any): The value of the attribute being set.

        Raises:
            ValueError: "side_a" or "angle_a" must be a positive number.
            ValueError: angle_a must be less than 180 degrees
            ValueError: This is Square not Rhomb.
        """
        if name in ('side_a', 'angle_a'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f'{name} must be a positive number.')
            if name == 'angle_a' and value >= 180:
                raise ValueError(f'{name} must be less than 180 degrees.')
            if name == 'angle_a' and value == 90:
                raise ValueError('This is Square not Rhomb.')
            # Automatically create and calculate the angle_b.
            super().__setattr__('angle_b', 180 - value)

        super().__setattr__(name, value)

    def __repr__(self) -> str:
        """Rhomb object string representation.

        Returns:
            str: String describing the Rhomb object.
        """
        return (f'{self.__class__.__name__} created: side: {self.side_a}, '
                f'angle a: {self.angle_a}, angle b: {self.angle_b}')


data = [
    (30, 45),  # {'angle_b': 135, 'side_a': 30, 'angle_a': 45}
    (20, 55.5),  # {'angle_b': 124.5, 'side_a': 20, 'angle_a': 55.5}
    (15.5, 0.5),  # {'angle_b': 179.5, 'side_a': 15.5, 'angle_a': 0.5}
    (181, 179),  # {'angle_b': 1, 'side_a': 181, 'angle_a': 179}
    (35, 90),  # ValueError: This is Square not Rhomb.
    (0, 179),  # ValueError: side_a must be a positive number.
    (20, 0),  # ValueError: angle_a must be a positive number.
    (20, 1800),  # ValueError: angle_a must be less than 180 degrees.
    (35, 85),  # {'angle_b': 95, 'side_a': 35, 'angle_a': 85}
]

for side, angle in data:
    try:
        rhomb = Rhomb(side, angle)
        _log.info(repr(rhomb))
        _log.info(rhomb.__dict__)
    except ValueError as error:
        _log.error(error)
