from os import getenv

from flask import jsonify, url_for


def create_views(blueprint):
    ''' Create views.'''
    @blueprint.route('/')
    def index():
        stream = url_for('sse.stream')
        return "<script> const source = new EventSource('{}');</script>".format(stream)
        api_version = getenv('API_VERSION')
        dct = {
            'app_name': 'Offline Tube', 
            'app_version': f'{api_version}'
        }
        return jsonify(dct)
