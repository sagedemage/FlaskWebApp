from flask import Flask
from app.db import db, create_db
from app.config import mysql_db_url
from app.routes import rest_api_routes


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_db_url()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.register_blueprint(rest_api_routes)

    db.init_app(app)

    #with app.app_context():
    #db.create_all()

    return app







