# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Install UV package manager
RUN pip install uv

# Copy project files from monorepo root
COPY pyproject.toml uv.lock /app/
COPY apps/app1/pyproject.toml /app/
COPY apps/app1/src /app/src

# Copy local dependency pkg-database
COPY packages/pkg-database /app/packages/pkg-database

# Set working directory before installing dependencies
WORKDIR /app

# Install local dependency first
RUN uv pip install --system -e /app/packages/pkg-database

# Install all remaining dependencies
RUN uv pip install --system .

# Expose port
EXPOSE 8001

# Command to run the FastAPI app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
