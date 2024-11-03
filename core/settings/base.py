import os
from pathlib import Path

# Base directory for the Django project
BASE_DIR = Path(__file__).resolve().parent.parent

# Common applications and middleware
INSTALLED_APPS = ["django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "app.db.models"]

# Secret key, overridden by environment-specific settings
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "default-secret-key")

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
]

# Common configurations for Django
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
