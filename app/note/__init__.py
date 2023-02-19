""" Note Actions """

from app.db.models import Note
from app.db import db


def add_user_note(title, description):
    """ Add a user note """
    note = Note(title=title, description=description)
    db.session.add(note)
    db.session.commit()
    msg = {"msg": "added_note"}

    return msg


def delete_user_note(note_id):
    """ Delete a user note """
    note = Note.query.filter_by(id=note_id).first()
    db.session.delete(note)
    db.session.commit()
    msg = {"msg": "deleted_note"}

    return msg


def edit_user_note(note_id, title, description):
    """ Edit a user note """
    note = Note.query.filter_by(id=note_id).first()
    note.edit_note(title, description)
    db.session.commit()
    msg = {"msg": "edited_note"}

    return msg


def fetch_user_note(note_id):
    """ Fetch a user note """
    note = Note.query.filter_by(id=note_id).first()
    title = note.get_title()
    description = note.get_description()
    msg = {"title": title, "description": description}

    return msg
