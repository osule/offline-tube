import os


def getenv(key, default=''):
    return os.getenv(key, default)


def configure_defaults():
    env = getenv('ENVIRONMENT', 'development')
    config = {
        'DEBUG': getenv('DEBUG', True),
        'REDIS_URL': getenv('REDIS_URL'),
        'YOUTUBE_API_KEY': getenv('YOUTUBE_API_KEY'),
    }
    if env != 'PRODUCTION':
        config['PYFILE'] = os.path.join('..', '.env')
    return config

