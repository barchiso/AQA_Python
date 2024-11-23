"""Create a class called "Student".

Create a class called "Student" with attributes like
"first name", "last name", "age", and "average grade".
Create an object of this class to represent a student.
Then add a method to the "Student" class
that allows you to change the student's grade point average.
Print out information about the student and change their grade point average.
"""
from logger import configure_logging

_log = configure_logging()


class Student:
    """Class to represent a student's info."""

    def __init__(self, first_name, last_name, age, average_grade):
        """Initialize the student's attributes.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
            average_grade (float): Student's average grade.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_grade(self, new_grade):
        """Change student's average grade.

        Args:
            new_grade (float): New student's average grade.

        Returns:
            string: _description_
        """
        # B010 "Do not call setattr with a constant attribute value,
        # it is not any safer than normal property access.""
        # if we use setattr(self, 'average_grade', new_grade)
        self.average_grade = new_grade
        message = f'Average grade is changed to : {new_grade}'
        return message

    def display_info(self):
        """Display student's info.

        Returns:
            string: Student's info.
        """
        message = (f'Student: {self.first_name}, {self.last_name}, '
                   f'Age: {self.age}, Average grade: {self.average_grade}')
        return message


# B010 "Do not call setattr with a constant attribute value,
# it is not any safer than normal property access.""
# and have next code
# >>> class Student:
# >>> >>> first_name = None
# >>> >>> last_name = None
# >>> >>> age = None
# >>> >>> average_grade = None
# and try to use setattr()
# >>> >>> student = Student()
# >>> >>> setattr(student, 'first_name', 'Johnny')
# >>> >>> setattr(student, 'last_name', 'Bravo')
# >>> >>> setattr(student, 'age', 20)
# >>> >>> setattr(student, 'average_grade', 80.3)

student = Student('Johnny', 'Bravo', 20, 80.3)
student1 = Student('Phoebe', 'Buffay', 19, 85.5)
student2 = Student('Joey', 'Tribbiani', 20, 70)
student3 = Student('Monica', 'Geller', 18, 91.1)
student4 = Student('Chandler', 'Bing', 21, 76.7)
student5 = Student('Rachel', 'Green', 18, 75)
student6 = Student('Ross', 'Geller', 23, 76.9)

_log.info(student.display_info())
_log.info(student.change_grade(85))
_log.info(student.display_info())

_log.info(student1.display_info())
_log.info(student1.change_grade(88.8))
_log.info(student1.display_info())

_log.info(student2.display_info())
_log.info(student2.change_grade(77.7))
_log.info(student2.display_info())

_log.info(student3.display_info())
_log.info(student3.change_grade(95.5))
_log.info(student3.display_info())

_log.info(student4.display_info())
_log.info(student4.change_grade(79.9))
_log.info(student4.display_info())

_log.info(student5.display_info())
_log.info(student5.change_grade(80.1))
_log.info(student5.display_info())

_log.info(student6.display_info())
_log.info(student6.change_grade(83.3))
_log.info(student6.display_info())
