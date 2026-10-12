import os

SECRET_KEY = os.environ.get("SECRET_KEY", "clave-local")
API_URL = os.environ.get("API_URL", "http://localhost:8000")
