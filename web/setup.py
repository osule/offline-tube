import web
import factory


app, sse = factory.create_app()

web.app = app
web.sse = sse