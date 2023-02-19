from flask import Flask
from app.config import mysql_db_url, sqlite_url
from app.routes.auth import auth_routes
from app.routes.note import note_routes
from app.db import db, create_db
from flask_migrate import Migrate
from app.db.models import *
import dotenv
import os

dotenv.load_dotenv()

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    if os.getenv("TESTING") == "false":
        app.config["TESTING"] = False
    elif os.getenv("TESTING") == "true":
        app.config["TESTING"] = True

    if app.config["TESTING"]:
        app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url()
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    elif not app.config["TESTING"]:
        app.config["SQLALCHEMY_DATABASE_URI"] = mysql_db_url()
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(auth_routes)
    app.register_blueprint(note_routes)

    db.init_app(app)
    migrate.init_app(app, db)

    if app.config["TESTING"]:
        with app.app_context():
            create_db()
            db.create_all()
    elif not app.config["TESTING"]:
        with app.app_context():
            db.create_all()

    return app







