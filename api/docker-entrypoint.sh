#!/usr/bin/env sh
set -eu

echo "Run db migration upgrade and data seeder"
poetry run flask db upgrade
poetry run flask seed run --root=main/seeds
exec "$@"