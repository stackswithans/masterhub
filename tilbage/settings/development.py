from pathlib import Path
import os
from corsheaders.defaults import default_methods
from settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

# Databases
DATABASES["default"] = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
}

CHANNEL_LAYERS = {
    "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}
}


CORS_ALLOWED_ORIGINS = ["http://localhost:5000"]
CORS_ALLOWED_METHODS = list(default_methods)
