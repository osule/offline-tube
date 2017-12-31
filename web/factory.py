from flask import Flask
from flask_sse import sse

from .config import configure_defaults


def create_app():
    app = Flask(__name__)
    config = configure_defaults()

    app.config.from_object(config)
    pyfile = config.get('PYFILE', None)

    if pyfile:
        app.config.from_pyfile(pyfile)

    return app, sse
