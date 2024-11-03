"""
Main entry point for the FastAPI application with Django ORM integration.

This module configures the application environment and initializes Django ORM settings.
"""

import os

# Set the environment (default is "local")
ENV = os.getenv("ENV", "local")

# Load the appropriate .env file based on the environment
if ENV != "production":
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f"./envs/.env.{ENV}")

# Configure Django ORM settings BEFORE importing any Django models or configurations
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{ENV}")

import django  # noqa: E402

django.setup()  # Initialize Django to ensure models and settings are available

from fastapi import FastAPI  # noqa: E402

from app.api.v1.api_router import api_router  # noqa: E402

app = FastAPI()

# Include API routers
app.include_router(api_router, prefix="/api/v1")
