from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

db = SQLAlchemy()
migrate = Migrate()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) ## initialize SQLAlchemy with the Flask app

    migrate.init_app(app, db) ## initialize Flask-Migrate with the Flask app and SQLAlchemy instance

    return app