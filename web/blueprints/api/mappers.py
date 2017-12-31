def video_mapper(item):
    snippet = item['snippet']
    return {
        'thumbnail_url': snippet['thumbnails']['default']['url'],
        'title': snippet['title'],
        'video_url': item['id']['videoId'],
    }