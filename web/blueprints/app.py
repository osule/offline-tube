from flask import Flask
from blueprints import downloader, home


def register_blueprint(app, module):
    ''' Register application blueprint. '''
    app.register_blueprint(module.blueprint)


app = Flask(__name__)
register_blueprint(app, home)
register_blueprint(app, downloader)

if __name__ == '__main__':
    app.run(debug=True)