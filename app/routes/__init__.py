from flask import Blueprint, jsonify

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
