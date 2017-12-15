from flask import jsonify, request, current_app
import requests


SEARCH_ENDPOINT = 'https://www.googleapis.com/youtube/v3/search/'

def search_video(query):
    api_key = current_app.config.get('YOUTUBE_API_KEY', '')
    params = {
        'part': 'snippet',
        'maxResults': 25,
        'q': query,
        'key': api_key,
        'type': 'video',
    }
    response = requests.get(SEARCH_ENDPOINT, params=params)
    json = response.json()

    def video_dct(item):
        snippet = item['snippet']
        return {
            'thumbnail_url': snippet['thumbnails']['default']['url'],
            'title': snippet['title'],
            'video_url': item['id']['videoId'],
        }

    results = list(
        map(video_dct, json['items'])
    )
    return results



def create_views(blueprint):

    @blueprint.route('/search')
    def search():
        query = request.args.get('q', '')
        results = search_video(query)
        return jsonify(results)
