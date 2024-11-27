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


class Rhomb:
    """Class to represent a rhombus data."""

    def __init__(self, side_a, angle_a):
        """Initialize the rhombus with side length and an internal angle.

        Args:
            side_a (float): Rhombus side length.
            angle_a (float): Rhombus angle between two adjacent sides.
        """
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


rhomb1 = Rhomb(30, 45)  # {'angle_b': 135, 'side_a': 30, 'angle_a': 45}
rhomb2 = Rhomb(20, 55.5)  # {'angle_b': 124.5, 'side_a': 20, 'angle_a': 55.5}
rhomb3 = Rhomb(15.5, 0.5)  # {'angle_b': 179.5, 'side_a': 15.5, 'angle_a': 0.5}
rhomb4 = Rhomb(181, 179)  # {'angle_b': 1, 'side_a': 181, 'angle_a': 179}
rhomb5 = Rhomb(35, 90)  # ValueError: This is Square not Rhomb.
rhomb6 = Rhomb(0, 179)  # ValueError: side_a must be a positive number.
rhomb7 = Rhomb(20, 0)  # ValueError: angle_a must be a positive number.
rhomb8 = Rhomb(20, 180)  # ValueError: angle_a must be less than 180 degrees.
rhomb9 = Rhomb(35, 85)  # {'angle_b': 95, 'side_a': 35, 'angle_a': 85}
