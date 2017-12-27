import os


def getenv(key):
    return os.getenv(key, '')


def configure_defaults():
    return {
        'PYFILE': os.path.join('..', '.env'),
    }
