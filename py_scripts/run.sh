#!/bin/sh

set -e

whoami

#python manage.py wait_for_db
#python manage.py collectstatic --noinput
python backend/manage.py makemigrations
python backend/manage.py makemigrations box
python backend/manage.py migrate
python backend/manage.py migrate box

pwd

uwsgi --chdir backend/ --socket :9000 --workers 4 --master --enable-threads --module backend.wsgi:application