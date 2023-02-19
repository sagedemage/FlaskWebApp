""" Note Routes """

import json
from flask import Blueprint, jsonify, request
from app.note import add_user_note, delete_user_note, edit_user_note, fetch_user_note

note_routes = Blueprint('note_routes', __name__)


@note_routes.route("/api/add-note", methods=["POST"])
def add_note():
    """ Add Note API Route """
    data = json.loads(request.data)

    title = data["title"]
    description = data["description"]

    msg = add_user_note(title, description)

    return jsonify(msg)


@note_routes.route("/api/delete-note", methods=["POST"])
def delete_note():
    """ Delete Note API Route """
    data = json.loads(request.data)

    note_id = data["note_id"]

    msg = delete_user_note(note_id)

    return jsonify(msg)


@note_routes.route("/api/edit-note", methods=["POST"])
def edit_note():
    """ Edit Note API Route """
    data = json.loads(request.data)

    note_id = data["note_id"]
    title = data["title"]
    description = data["description"]

    msg = edit_user_note(note_id, title, description)

    return jsonify(msg)


@note_routes.route("/api/fetch-note", methods=["POST"])
def fetch_note():
    """ Fetch Note API Route """
    data = json.loads(request.data)

    note_id = data["note_id"]

    msg = fetch_user_note(note_id)

    return jsonify(msg)



