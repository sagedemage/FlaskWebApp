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

    user = User(email=email, username=username, password=password)

    db.session.add(user)
    db.session.commit()
    
    data = {
        "page name": "about page",
        "page route": "/about"
    }

    return jsonify(data)
