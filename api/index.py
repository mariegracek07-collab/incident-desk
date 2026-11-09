# Vercel serverless entrypoint — imports the Django WSGI application.
# prepare_environment() (called inside config/wsgi.py) detects VERCEL=1
# and sets DJANGO_SETTINGS_MODULE=config.settings.production automatically.
from config.wsgi import application
