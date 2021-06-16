release: cd tilbage && python manage.py migrate
web: cd tilbage && daphne tilbage.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: cd tilbage && python manage.py runworker call
