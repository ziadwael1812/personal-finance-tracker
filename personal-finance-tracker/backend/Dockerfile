# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies (if any, e.g., for psycopg2-binary if not using pure Python driver)
# RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Poetry (or your preferred package manager like PDM)
# This is an example using pip for simplicity with requirements.txt for now
# RUN pip install --upgrade pip
# COPY ./requirements.txt /app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# For Poetry or PDM, you'd copy pyproject.toml and poetry.lock/pdm.lock
# and run 'poetry install' or 'pdm install'
COPY ./pyproject.toml ./poetry.lock* /app/
# Ensure poetry is installed. If not, install it:
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY ./app /app/app
COPY ./main.py /app/main.py
COPY ./alembic.ini /app/alembic.ini
COPY ./alembic /app/alembic

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
# For development with uvicorn and auto-reload (not for production):
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# For production:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 