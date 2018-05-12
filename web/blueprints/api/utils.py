from .mappers import video_mapper

from celery.result import AsyncResult
from tasks import extract_info

def pass_query(fn):
    def wraps(*args):
        request, *rest = args
        return fn(request.query, *rest)
    return wraps

@pass_query
def search_video(query, api_key):
    params = {
        'part': 'snippet',
        'maxResults': 25,
        'q': query,
        'key': api_key,
        'type': 'video',
    }
    response = requests.get(SEARCH_ENDPOINT, params=params)
    json = response.json()

    results = list(
        map(video_mapper, json['items'])
    )
    return results

@pass_query
def get_media_types(query):
    async_result = extract_info.delay(query)
    return {
        'task_id': async_result.task_id
    }

@pass_query
def get_task_status(query):
    async_result = AsyncResult(query)
    return {
        'state': async_result.state,
        'result': async_result.result,
    }
