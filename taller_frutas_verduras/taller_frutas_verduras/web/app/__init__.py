from flask import Flask
from config import SECRET_KEY
from .routes import rutas

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.register_blueprint(rutas)
    return app
