#!/bin/bash
set -e
pip install -r requirements-prod.txt
python manage.py collectstatic --noinput
