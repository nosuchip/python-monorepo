# === Stage 1: Install dependencies ===
FROM python:3.11-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Build argument for selecting the service
ARG APPLICATION

# Copy only the dependency files for the specific service
COPY apps/${APPLICATION}/pyproject.toml uv.lock ./


RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --package ${APPLICATION} --no-install-workspace

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable --package ${APPLICATION}

# === Stage 2: Final runtime container ===
FROM python:3.11-slim

WORKDIR /app

# Build argument for selecting the service
ARG APPLICATION

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/apps/${APPLICATION}/src /app
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

# Run FastAPI application
CMD ["uvicorn", "app1.main:app", "--host", "0.0.0.0", "--port", "8000"]
