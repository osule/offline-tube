from web import app, sse
from blueprints import api, home


def register_blueprints():
    ''' Register application blueprint. '''
    app.register_blueprint(home)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(sse, url_prefix='/stream')
