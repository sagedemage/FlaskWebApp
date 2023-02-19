""" Database Models """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import db


class User(db.Model):
    """ User model """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))
    note = relationship("Note", backref="user")

    def __init__(self, email, username, password):
        """ Initialize User """
        self.email = email
        self.username = username
        self.password = generate_password_hash(password, 'sha256', 16)

    def check_password(self, password):
        """ Check password is correct """
        password_match = check_password_hash(self.password, password)
        return password_match

    def get_id(self):
        """ get User's id """
        return self.id


class Note(db.Model):
    """ Note model """
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.id"))

    def edit_note(self, title, description):
        """ Edit Note's title and description """
        self.title = title
        self.description = description

    def get_title(self):
        """ Get Note's title """
        return self.title

    def get_description(self):
        """ Get Note's description """
        return self.description
