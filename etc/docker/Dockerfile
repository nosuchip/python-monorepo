FROM python:3.11

RUN python3 -m pip install pdm==2.20.1
ENV WORKDIR="/application/apps/app"
RUN mkdir -p "${WORKDIR}"
WORKDIR "${WORKDIR}"

COPY ./packages /application/packages
ARG APPLICATION
COPY apps/${APPLICATION}/pyproject.toml apps/${APPLICATION}/pdm.lock ./
RUN pdm install --no-lock --check --no-editable
COPY apps/${APPLICATION}/src ./