import os

from fastapi import FastAPI

from app.routes import api_router

# Set Django environment for ORM and settings
ENV = os.getenv("ENV", "local")
if ENV != "production":
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f"./envs/.env.{ENV}")

# Django and ORM configuration

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{ENV}")

import django  # noqa E402

django.setup()

app = FastAPI()

app.include_router(api_router)
