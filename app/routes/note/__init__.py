from flask import Blueprint, jsonify, request
from app.note import add_user_note, delete_user_note, edit_user_note
import json

note_routes = Blueprint('note_routes', __name__)


@note_routes.route("/")
def index():
    data = {
        "page name": "index page",
        "page route": "/"
    }

    return jsonify(data)


@note_routes.route("/about")
def about():
    data = {
        "page name": "about page",
        "page route": "/about"
    }

    return jsonify(data)


@note_routes.route("/api/add-note", methods=["POST"])
def add_note():
    data = json.loads(request.data)

    title = data["title"]
    description = data["description"]

    msg = add_user_note(title, description)

    return jsonify(msg)


@note_routes.route("/api/delete-note", methods=["POST"])
def delete_note():
    data = json.loads(request.data)

    note_id = data["note_id"]

    msg = delete_user_note(note_id)

    return jsonify(msg)


@note_routes.route("/api/edit-note", methods=["POST"])
def edit_note():
    data = json.loads(request.data)

    note_id = data["note_id"]
    title = data["title"]
    description = data["description"]

    msg = edit_user_note(note_id, title, description)

    return jsonify(msg)



