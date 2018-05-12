from os import getenv

from flask import jsonify


def create_views(blueprint):
    ''' Create views.'''
    @blueprint.route('/')
    def index():
        api_version = getenv('API_VERSION')
        dct = {
            'app_name': 'Offline Tube', 
            'app_version': f'{api_version}'
        }
        return jsonify(dct)
