import os


def getenv(key):
    return os.getenv(key, '')


class SharedConfiguration:
    PYFILE = os.path.join('..', '.env')

def configure_defaults():
    return SharedConfiguration()
