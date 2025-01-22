"""Database models."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db_engine import Base


class Student(Base):
    """Represent a student in the system.

    Args:
        Base (type): The base class for all SQLAlchemy models.
    """

    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    # Relationship with courses (Many-to-Many relationship)
    courses = relationship(
        'Course', secondary='enrollments', back_populates='students')


class Course(Base):
    """Represent a course in the system.

    Args:
        Base (type): The base class for all SQLAlchemy models.
    """

    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    # Relationship with students (Many-to-Many relationship)
    students = relationship(
        'Student', secondary='enrollments', back_populates='courses')


# Define the Enrollments table for many-to-many relationship
class Enrollment(Base):
    """Represent the enrollment of a student in a course.

        Establishing a many-to-many relationship.

    Args:
        Base (type): The base class for all SQLAlchemy models.
    """

    __tablename__ = 'enrollments'
    student_id = Column(Integer, ForeignKey(
        'students.id', ondelete='CASCADE'), primary_key=True)
    course_id = Column(Integer, ForeignKey(
        'courses.id', ondelete='CASCADE'), primary_key=True)
