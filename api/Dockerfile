FROM python:3.8.12-alpine3.14

# ===============
# Alpine packages
# ===============

RUN apk update \
    && apk add --no-cache gcc musl-dev g++ libffi-dev openssl-dev cargo \
    py3-pip tini bash openjdk8 openssl unzip wget git


ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.1.13 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.poetry/bin"

# System deps:
RUN pip install "poetry==$POETRY_VERSION"
#pip install --no-cache --upgrade wheel

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# create non-root user
RUN adduser -s /bin/sh -D -G root -u 1000 web

WORKDIR /api
# Setting up proper permissions:
RUN chown -R 1000:1000 /api

# Copy only requirements, to cache them in docker layer
COPY --chown=1000:1000 ./poetry.lock ./pyproject.toml /api/


# Project initialization:
RUN poetry install --no-dev --no-root --no-interaction --no-ansi \
  # Cleaning poetry installation's cache for production:
  && rm -rf "$POETRY_CACHE_DIR"

# Creating folders, and files for a project:
COPY --chown=1000:1000 . /api


ENV FLASK_APP=main.core:app \
    FLASK_ENV=development \
    GUNICORN_LOG_LEVEL=${GUNICORN_LOG_LEVEL:-debug}

EXPOSE 5000
LABEL name="Favorite Tree API" \
    maintainer="Mohammad Abudayyeh <mo@techtative.io>" \
    version="1.0.0" \
    release="a1" \
    description="A simple API that returns my faviorite tree"

# Running as non-root user:
USER 1000

# Set env with user being web created above
ENV HOME /home/web

# Create .cloud folder holding api values in order to be accessible by current user
RUN mkdir -p $HOME/.secrets


ENV SQLALCHEMY_DATABASE_URI_FILEPATH=${SQLALCHEMY_DATABASE_URI_FILEPATH}

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD "poetry" "run" "gunicorn" "main.core:app" "-b" ":5000" "--log-level" \
$GUNICORN_LOG_LEVEL "--workers" "1" "--threads" "8" "--timeout" "0" \
"--worker-tmp-dir" "/dev/shm" "--worker-class" "gthread" \
"--access-logfile" "-"  "--error-logfile" "-" "--preload" \
"--graceful-timeout" "30" "--keep-alive" "5" \
"--log-config" "gunicorn_logging.conf"
