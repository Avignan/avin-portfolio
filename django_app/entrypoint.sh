#!/bin/sh

echo "Waiting for services..."
sleep 10

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Django server..."
if [ "$DJANGO_ENV" = "production" ]; then
    gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000 --workers 3
else
    python manage.py runserver 0.0.0.0:8000
fi