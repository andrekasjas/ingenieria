#!/usr/bin/env bash
# exit on error
# ejecutar con ./build.sh
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate