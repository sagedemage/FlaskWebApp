""" Database """

import sqlite3
from flask import g
from flask_sqlalchemy import SQLAlchemy
from app.config import sqlite_path

db = SQLAlchemy()


def create_db():
    """ Create SQLite Database """
    database = getattr(g, '_database', None)
    if database is None:
        g._database = sqlite3.connect(sqlite_path())
