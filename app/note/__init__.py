from app.db.models import Note
from app.db import db


def add_user_note(title, description):
    note = Note(title=title, description=description)
    db.session.add(note)
    db.session.commit()
    msg = {"msg": "added_note"}

    return msg


def delete_user_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    db.session.delete(note)
    db.session.commit()
    msg = {"msg": "deleted_note"}

    return msg
