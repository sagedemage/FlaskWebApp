import os

from flask import Blueprint, jsonify, request
from app.db import db
from app.db.models import User
import json
import jwt
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

    email_exists = User.query.filter_by(email=username).first()
    username_exists = User.query.filter_by(username=username).first()

    msg = {}

    if email_exists is not None:
        if email_exists.check_password(password):
            user_id = email_exists.get_id()
            msg["msg"] = "success"
            msg["token"] = generate_token(user_id)
        else:
            msg["err_msg"] = "wrong credentials"
    elif username_exists is not None:
        if username_exists.check_password(password):
            user_id = username_exists.get_id()
            msg["msg"] = "success"
            msg["token"] = generate_token(user_id)
        else:
            msg["err_msg"] = "wrong credentials"
    elif email_exists is None:
        msg["err_msg"] = "wrong credentials"
    elif username_exists is None:
        msg["err_msg"] = "wrong credentials"

    return jsonify(msg)


@auth_routes.route("/api/get-decoded-token", methods=["POST"])
def get_decoded_token():
    data = json.loads(request.data)

    token = data["token"]

    msg = {"data": decode_token(token)}

    return jsonify(msg)


def generate_token(user_id):
    secret = os.getenv("JWT_SECRET")
    encoded_token = jwt.encode({"auth": True, "user_id": user_id}, secret, algorithm="HS256")
    return encoded_token


def decode_token(token):
    secret = os.getenv("JWT_SECRET")
    token_data = jwt.decode(token, secret, algorithms=["HS256"])
    return token_data
