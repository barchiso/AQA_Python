# Dockerfile
FROM python:3.9-slim

# Install PostgreSQL development files and dependencies for building psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install dependencies
RUN pip install --upgrade pip
RUN pip install sqlalchemy psycopg2-binary

# Set up working directory and copy the code
WORKDIR /app
COPY . /app

# Set the command to run the Python app
CMD ["python", "db_operations.py"]
