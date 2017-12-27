from flask import Flask

from .blueprints import taskman, home, api
from .config import configure_defaults

def register_blueprint(app, module, modifiers={}):
    ''' Register application blueprint. '''
    app.register_blueprint(module.blueprint, **modifiers)


def create_app(confs):
    app = Flask(__name__)
    app.config.from_object(confs)
    pyfile = confs.get('PYFILE', None)

    if pyfile:
        app.config.from_pyfile(pyfile)

    register_blueprint(app, home)
    register_blueprint(app, api, {'url_prefix': '/api'})
    register_blueprint(app, taskman)

    return app


if __name__ == '__main__':
    app = create_app(configure_defaults())
    app.run()
