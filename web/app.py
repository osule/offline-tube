from flask import Flask

from blueprints import taskman, home, api
from config import configure_defaults

def register_blueprint(app, module, modifiers={}):
    ''' Register application blueprint. '''
    app.register_blueprint(module.blueprint, **modifiers)


app = Flask(__name__)
app.config.from_object(configure_defaults())
app.config.from_pyfile(app.config.get('PYFILE'))


register_blueprint(app, home)
register_blueprint(app, api, {'url_prefix': '/api'})
register_blueprint(app, taskman)

if __name__ == '__main__':
    app.run()
