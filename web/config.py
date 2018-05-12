from os import getenv


ENVIRONMENT = getenv('ENVIRONMENT', 'development')

DEBUG = getenv('DEBUG', '')

REDIS_URL = getenv('REDIS_URL', '')

YOUTUBE_API_KEY = getenv('YOUTUBE_API_KEY', '')