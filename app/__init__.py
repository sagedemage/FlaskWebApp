from flask import Flask
from app.config import mysql_db_url
from app.routes.auth import auth_routes
from app.routes.note import note_routes
from app.db import db
from flask_migrate import Migrate
from app.db.models import *

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_db_url()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.register_blueprint(auth_routes)
    app.register_blueprint(note_routes)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app







