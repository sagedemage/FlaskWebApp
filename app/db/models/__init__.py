from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))
    note = relationship("Note", backref="user")

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password, 'sha256', 16)

    def check_password(self, password):
        password_match = check_password_hash(self.password, password)
        return password_match


class Note(db.Model):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.id"))

