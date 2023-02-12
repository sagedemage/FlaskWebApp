from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))
    note = relationship("Note", backref="user")


class Note(db.Model):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(100))
    user_id = Column(Integer, ForeignKey("user.id"))

