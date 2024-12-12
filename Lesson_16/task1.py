"""Class diamond inheritance."""

# Task 1
# Create an Employee class that has the attributes name and salary.
# Next, create two classes, Manager and Developer, that inherit from Employee.
# The Manager class should have an additional attribute department, and
# the Developer class should have an additional attribute programming_language.

# Now create a TeamLead class that inherits from both Manager and Developer.
# This class represents a manager on a development team.
# he TeamLead class should have all the attributes of
# Manager(name, salary, department), as well as a team_size attribute
# that indicates the number of developers on the team that the manager manages.

# Write a test that checks for the presence of the attributes
# from Manager and Developer in the TeamLead class


# Too few public methods (0/2)PylintR0903:too-few-public-methods
class Employee:
    """Class to represent an employee with a name and a salary."""

    def __init__(self, name, salary, **kwargs):
        """Initialize an Employee instance.

        Args:
            name (str): The name of the employee.
            salary (float): The salary of the employee.
            kwargs: Additional arguments to be passed to the parent class.
        """
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


# Too few public methods (0/2)PylintR0903:too-few-public-methods
class Manager(Employee):
    """Class to represent manager, inherited from Employee, with a department.

    Args:
        Employee (class): The base class representing an employee.
    """

    def __init__(self, name, salary, department, **kwargs):
        """Initialize a Manager instance.

        Args:
            name (str): The name of the manager.
            salary (float): The salary of the manager.
            department (str): The department the manager oversees.
            kwargs: Additional arguments to be passed to the parent class.
        """
        super().__init__(name, salary, **kwargs)
        self.department = department


# Too few public methods (0/2)PylintR0903:too-few-public-methods
class Developer(Employee):
    """Class a developer, inherited from Employee, with a programming language.

    Args:
        Employee (class): The base class representing an employee.
    """

    def __init__(self, name, salary, programming_language=None, **kwargs):
        """Initialize a Developer instance.

        Args:
            name (str): The name of the developer.
            salary (float): The salary of the developer.
            programming_language (str): The primary programming language.
            kwargs: Additional arguments to be passed to the parent class.
        """
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language


# Too few public methods (0/2)PylintR0903:too-few-public-methods
class TeamLead(Manager, Developer):
    """Class to represent team lead, who is both a manager and a developer.

    Args:
        Manager (class): The base class representing a manager.
        Developer (class): The base class representing a developer.
    """

    # Too many arguments (6/5)PylintR0913:too-many-arguments
    def __init__(self, name, salary, department, team_size=0,
                 programming_language=None):
        """Initialize a Team Lead instance.

        Args:
            name (str): The name of the team lead.
            salary (float): The salary of the team lead.
            department (str): The department the team lead oversees.
            team_size (int): The size of the team the team lead manages.
            programming_language (str): The primary programming language.
        """
        super().__init__(name, salary, department,
                         programming_language=programming_language)
        self.team_size = team_size


if __name__ == '__main__':
    employee = Employee('John Doe', 50000)
    manager = Manager('Alice Smith', 70000, 'HR')
    developer = Developer('Bob Brown', 60000, 'Python')
    team_lead = TeamLead('Charlie Green', 90000,
                         'Engineering', 5, 'JavaScript')
    team_lead1 = TeamLead('Sasha Grey', 80000, 'HR', 10)
    team_lead2 = TeamLead('Benny Hill', 70000, 'Sales')

    print(employee.__dict__)
    print(manager.__dict__)
    print(developer.__dict__)

    print(team_lead.__dict__)
    print(hasattr(team_lead, 'name'))  # Inherited from Employee
    print(team_lead.name)  # Inherited from Employee
    print(hasattr(team_lead, 'salary'))  # Inherited from Employee
    print(team_lead.salary)  # Inherited from Employee
    print(hasattr(team_lead, 'department'))  # Inherited from Manager
    print(team_lead.department)  # Inherited from Manager
    # Inherited from Developer
    print(hasattr(team_lead, 'programming_language'))
    print(team_lead.programming_language)  # Inherited from Developer
    print(hasattr(team_lead, 'team_size'))
    print(team_lead.team_size)

    print(team_lead1.__dict__)
    print(hasattr(team_lead1, 'name'))  # Inherited from Employee
    print(team_lead1.name)  # Inherited from Employee
    print(hasattr(team_lead1, 'salary'))  # Inherited from Employee
    print(team_lead1.salary)  # Inherited from Employee
    print(hasattr(team_lead1, 'department'))  # Inherited from Manager
    print(team_lead1.department)  # Inherited from Manager
    # Inherited from Developer
    print(hasattr(team_lead1, 'programming_language'))
    print(team_lead1.programming_language)  # Inherited from Developer
    print(hasattr(team_lead1, 'team_size'))
    print(team_lead1.team_size)

    print(team_lead2.__dict__)
    print(hasattr(team_lead2, 'name'))  # Inherited from Employee
    print(team_lead2.name)  # Inherited from Employee
    print(hasattr(team_lead2, 'salary'))  # Inherited from Employee
    print(team_lead2.salary)  # Inherited from Employee
    print(hasattr(team_lead2, 'department'))  # Inherited from Manager
    print(team_lead2.department)  # Inherited from Manager
    # Inherited from Developer
    print(hasattr(team_lead2, 'programming_language'))
    print(team_lead2.programming_language)  # Inherited from Developer
    print(hasattr(team_lead2, 'team_size'))
    print(team_lead2.team_size)
