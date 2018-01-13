import os


NON_ENVFILE_ENVIRONMENTS = {'PRODUCTION', 'TEST'}

def getenv(key, default=''):
    return os.getenv(key, default)


def configure_defaults():
    env = getenv('ENVIRONMENT', 'DEVELOPMENT')
    config = {
        'DEBUG': getenv('DEBUG', True),
        'REDIS_URL': getenv('REDIS_URL'),
        'YOUTUBE_API_KEY': getenv('YOUTUBE_API_KEY'),
    }
    if env not in NON_ENVFILE_ENVIRONMENTS:
        config['PYFILE'] = os.path.join('..', '.env')
    return config
