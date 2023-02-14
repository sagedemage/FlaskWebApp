from flask import Blueprint, jsonify, request
from app.db import db
from app.db.models import User
import json

rest_api_routes = Blueprint('rest_api_routes', __name__)


@rest_api_routes.route("/")
def index():
    data = {
        "page name": "index page",
        "page route": "/"
    }

    return jsonify(data)


@rest_api_routes.route("/about")
def about():
    data = {
        "page name": "about page",
        "page route": "/about"
    }

    return jsonify(data)


@rest_api_routes.route("/api/register", methods=["POST"])
def register():
    data = json.loads(request.data)

    email = data["email"]
    username = data["username"]
    password = data["password"]

    email_exists = User.query.filter_by(email=email).first()
    username_exists = User.query.filter_by(username=username).first()

    user = User(email=email, username=username, password=password)

    msg = {}

    if email_exists is not None:
        msg["err_msg"] = "email exists"
    elif username_exists is not None:
        msg["err_msg"] = "username exists"
    else:
        db.session.add(user)
        db.session.commit()
        msg["msg"] = "success"

    return jsonify(msg)


@rest_api_routes.route("/api/login", methods=["POST"])
def login():
    data = json.loads(request.data)

    username = data["username"]
    password = data["password"]

    email_exists = User.query.filter_by(email=username).first()
    username_exists = User.query.filter_by(username=username).first()

    msg = {}

    if email_exists is not None:
        if email_exists.check_password(password):
            msg["msg"] = "success"
        else:
            msg["err_msg"] = "wrong credentials"
    elif username_exists is not None:
        if username_exists.check_password(password):
            msg["msg"] = "success"
        else:
            msg["err_msg"] = "wrong credentials"
    elif email_exists is None:
        msg["err_msg"] = "wrong credentials"
    elif username_exists is None:
        msg["err_msg"] = "wrong credentials"

    return jsonify(msg)
