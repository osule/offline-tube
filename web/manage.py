from web.setup import app, sse
from web.routes import register_blueprints

register_blueprints()

if __name__ == '__main__':
    app.run()
