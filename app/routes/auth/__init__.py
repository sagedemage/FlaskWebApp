import os

from flask import Blueprint, jsonify, request
from app.db import db
from app.db.models import User
from app.auth.token import decode_token
from app.auth import user_login
import json

import dotenv

dotenv.load_dotenv()

auth_routes = Blueprint('rest_api_routes', __name__)


@auth_routes.route("/")
def index():
    data = {
        "page name": "index page",
        "page route": "/"
    }

    return jsonify(data)


@auth_routes.route("/about")
def about():
    data = {
        "page name": "about page",
        "page route": "/about"
    }

    return jsonify(data)


@auth_routes.route("/api/register", methods=["POST"])
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


@auth_routes.route("/api/login", methods=["POST"])
def login():
    data = json.loads(request.data)

    username = data["username"]
    password = data["password"]

    msg = user_login(username, password)

    return jsonify(msg)


@auth_routes.route("/api/get-decoded-token", methods=["POST"])
def get_decoded_token():
    data = json.loads(request.data)

    token = data["token"]

    msg = {"data": decode_token(token)}

    return jsonify(msg)



