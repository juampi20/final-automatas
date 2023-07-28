import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Registro de la blueprint
    from .controllers import automata
    app.register_blueprint(automata, url_prefix='/')

    return app
