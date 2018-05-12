from flask import Flask
from flask_sse import sse


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    return app, sse
