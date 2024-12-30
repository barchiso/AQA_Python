"""Database models."""

# Homework #22. My little SQLAlchemy.
# Creating a data model:
# Create a simple data model for the student management system.
# The model can contain tables for students, courses and their relationships.
# Each student can be enrolled in several courses.
# For example, create 5 courses, and distribute a randomly 20 students.
# Perform basic operations:
# Write a program that adds a new student to the database
# and adds it to a specific course.
# Make sure these changes are correctly displayed in the database.
# Database Requests:
# Write database queries that return information about students
# enrolled in a particular course or courses
# for which a particular student is registered.
# Update and delete data:
# Implement the ability to update student data or courses,
# as well as remove students from the database.
# You can use any ORM on your vibe

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
