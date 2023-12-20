#!/bin/sh

/wait-for-it.sh database:5432 -t 60

python manage.py migrate

exec "$@"