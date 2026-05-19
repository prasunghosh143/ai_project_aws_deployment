web: python manage.py migrate --noinput && gunicorn ai_project.wsgi --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120 --access-logfile - --error-logfile -
