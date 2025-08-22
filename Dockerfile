FROM python:3.13-slim-bullseye AS python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base AS builder-base
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install -y --no-install-recommends curl=7.74.0-1.3+deb11u15 \
    && apt-get install -y --no-install-recommends "$buildDeps" \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.4.2
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} && \
    chmod a+x /opt/poetry/bin/poetry

WORKDIR $PYSETUP_PATH

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --only main


FROM python-base AS development
ENV FASTAPI_ENV=development

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /app
COPY . .

RUN useradd -u 10000 -m -r app_user && \
    chown app_user .
EXPOSE 8080

USER app_user

ENTRYPOINT ["/entrypoint.sh"]
