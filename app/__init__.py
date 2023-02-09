from flask import Flask, jsonify

app = Flask(__name__)


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

