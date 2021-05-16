from pathlib import Path
import os
import django_heroku
from settings.base import *
import psycopg2
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [".herokuapp.com"]

# Database config
DATABASE_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(DATABASE_URL, sslmode="require")

DATABASES["default"] = dj_database_url.config(
    conn_max_age=600, ssl_require=True
)

# Directory used by collect static
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Activate django_heroku
django_heroku.settings(locals())
