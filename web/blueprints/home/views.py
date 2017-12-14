from flask import render_template


def create_views(blueprint):
    ''' Create views.'''
    @blueprint.route('/')
    def index():
        return render_template('index.html')
