import requests
from flask import jsonify, request, current_app

from .utils import search_video, get_media_types, get_task_status


SEARCH_ENDPOINT = 'https://www.googleapis.com/youtube/v3/search/'


class GetRequest():
    def __init__(self, req):
        self.query = req.args.get('q', '')


def create_views(blueprint):

    @blueprint.route('/search')
    def search():
        api_key = current_app.config.get('YOUTUBE_API_KEY', '')
        result = search_video(GetRequest(request), api_key)
        return jsonify(result)

    @blueprint.route('/media_types')
    def media_types():
        result = get_media_types(GetRequest(request))
        return jsonify(result)

    @blueprint.route('/task_status')
    def task_status():
        ''' Poll task status.
            TODO: deprecate to favor SSEs.
        '''
        result = get_task_status(GetRequest(request))
        return jsonify(result)
