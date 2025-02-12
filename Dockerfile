# === Stage 1: Install dependencies ===
FROM python:3.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Build argument for selecting the service
ARG APPLICATION

# Copy only the dependency files for the specific service
COPY apps/${APPLICATION}/pyproject.toml uv.lock ./

RUN uv sync --locked --no-install-workspace

COPY packages /app/packages
RUN uv sync --locked --no-editable --package

# # Install uv
# RUN pip install --no-cache-dir uv

# # Generate a requirements file for the specific service
# RUN uv pip freeze --workspace apps/${APPLICATION} > requirements.txt \
#     && pip install --no-cache-dir --prefix=/install -r requirements.txt

# === Stage 2: Final runtime container ===
FROM python:3.11-slim

WORKDIR /app

# Build argument for selecting the service
ARG APPLICATION

# Copy installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy only the source code for the selected service
COPY apps/${APPLICATION}/src/${APPLICATION} /app/${APPLICATION}

# Run FastAPI application
CMD ["uvicorn", "app1.main:app", "--host", "0.0.0.0", "--port", "8000"]
