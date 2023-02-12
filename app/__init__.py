import os

from flask import Flask, jsonify

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_USERNAME = "root"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "notebook2"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"

DB_URL = 'mysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME

# 'mysql://username:password@host:port/database_name'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL


@app.route("/")
def index():
    data = {
        "page name": "index page",
        "page route": "/"
    }

    return jsonify(data)


@app.route("/about")
def about():
    data = {
        "page name": "about page",
        "page route": "/about"
    }

    return jsonify(data)

