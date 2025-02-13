#!/bin/sh

poetry run python manage.py migrate

exec "$@"
