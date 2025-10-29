# Multi-stage build for optimized production image

# Stage 1: Base image with dependencies
FROM python:3.11-slim as base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Development image
FROM base as development

# Install development dependencies
RUN pip install --no-cache-dir \
    pytest \
    pytest-asyncio \
    pytest-cov \
    black \
    flake8 \
    mypy

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run with reload for development
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Stage 3: Production image
FROM base as production

# Copy only application code
COPY ./app /app/app
COPY ./alembic /app/alembic
COPY alembic.ini /app/

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
