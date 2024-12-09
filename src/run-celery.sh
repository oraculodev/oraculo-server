#!/usr/bin/env sh

set -eux

exec celery -A jobs worker --beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
