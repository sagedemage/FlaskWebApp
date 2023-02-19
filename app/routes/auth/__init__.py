""" Authentication Routes """

import json
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from app.auth.token import decode_token
from app.auth import user_login, user_registration


load_dotenv()

auth_routes = Blueprint('auth_routes', __name__)


@auth_routes.route("/api/register", methods=["POST"])
def register():
    """ Register API Route """
    data = json.loads(request.data)

    email = data["email"]
    username = data["username"]
    password = data["password"]

    msg = user_registration(email, username, password)

    return jsonify(msg)


@auth_routes.route("/api/login", methods=["POST"])
def login():
    """ Login API Route """
    data = json.loads(request.data)

    username = data["username"]
    password = data["password"]

    msg = user_login(username, password)

    return jsonify(msg)


@auth_routes.route("/api/get-decoded-token", methods=["POST"])
def get_decoded_token():
    """ Get Decoded Token API Route """
    data = json.loads(request.data)

    token = data["token"]

    msg = {"data": decode_token(token)}

    return jsonify(msg)



