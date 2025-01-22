"""Database init."""

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Define the PostgreSQL database connection string.
DB_STRING = os.getenv(
    'DATABASE_URL', 'postgresql://user:password@postgres:5432/student_db')


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
