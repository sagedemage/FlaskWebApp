from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import g
from app.config import sqlite_path

db = SQLAlchemy()


def create_db():
    database = getattr(g, '_database', None)
    if database is None:
        g._database = sqlite3.connect(sqlite_path())
