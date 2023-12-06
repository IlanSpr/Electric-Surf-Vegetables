import os
from flask import Flask
from dotenv import load_dotenv
from .kafka import setup_kafka

from . import app_db
from .models import db
from .app_logging import setup_logging
from .routes import init_app_routes

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app_db.init_db(app)

    setup_logging(app)
    init_app_routes(app)
    setup_kafka(app)

    return app
