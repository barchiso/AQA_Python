# Dockerfile
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies directly 
RUN pip install --no-cache-dir pytest allure-pytest

# Command to run the tests
CMD ["pytest", "--alluredir=allure_results"]
