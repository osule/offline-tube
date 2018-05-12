from os import getenv

result_expires = 3600
broker_url = getenv('REDIS_URL', 'redis://')
result_backend = getenv('REDIS_URL', 'redis://')
result_serializer = 'json'
task_serializer = 'json'
accept_content = ['json']
include = ['tasks']
