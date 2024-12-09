#!/usr/bin/env sh

set -eux

./manage.py collectstatic --noinput
./manage.py migrate

exec gunicorn -c config/gunicorn.conf.py config.wsgi:application --access-logfile '-'
