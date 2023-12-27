import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from . import app_db, rabbitmq
from .models import db
from .routes import init_app_routes


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app_db.init_db(app)
    init_app_routes(app)

    return app
