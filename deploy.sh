#!/bin/bash

cd ~/projects/django-oracle

git pull 

pipenv shell

pipenv install

python manage.py migrate
python manage.py collectstatic --noinput

sudo systemctl restart django