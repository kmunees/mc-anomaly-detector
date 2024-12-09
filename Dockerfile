# Base image
FROM python:3.12-slim

# Set environment variables
ENV POETRY_VERSION=1.8.1 \
    POETRY_HOME=/opt/poetry \
    PATH="/opt/poetry/bin:$PATH"

# Install Poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy Poetry files first for dependency resolution
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Set the command to run the application
CMD ["python", "main.py"]
