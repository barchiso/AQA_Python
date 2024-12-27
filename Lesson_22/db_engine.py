"""Database init."""

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

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Define the database connection string.
DB_STRING = 'sqlite:///student_management.db'

# Define the base class for SQLAlchemy models.
Base = declarative_base()


class DatabaseEngine:
    """Class to manage the creation of the database engine and session."""

    def __init__(self):
        """Initialize the Db class.

        - Creates a database engine based on the DB_STRING.
        - Sets up a scoped session to manage database transactions.
        - Initializes the database schema using the `_init_db` method.
        """
        # Create a database engine to handle the connection to the database.
        # The engine is the starting point for all SQLAlchemy operations.
        self.engine = create_engine(DB_STRING)

        # Set up a scoped session. This session ensures thread-safe handling of
        # database interactions and simplifies transaction management.
        self.session = scoped_session(
            sessionmaker(
                # Transactions are explicitly committed.
                autocommit=False,
                # Prevent automatic flushing of changes to the database.
                autoflush=False,
                bind=self.engine,  # Bind the session to the created engine.
            ),
        )

        # Initialize the database schema
        # and associate the session with the base query property.
        self._init_db()

    def _init_db(self):
        """Initialize database ORM metadata."""
        # Associate the session with the query property of the Base class.
        # This allows ORM models to use the `query` property
        # for database operations.
        Base.query = self.session.query_property()

        # Create all tables defined in the ORM models.
        # If the tables already exist in the database,
        # this operation is a no-op.
        Base.metadata.create_all(bind=self.engine)
