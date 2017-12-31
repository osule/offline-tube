result_expires = 3600
broker_url = 'redis://'
result_backend = 'redis://'
result_serializer = 'json'
task_serializer = 'json'
accept_content = ['json']
include = ['web.tasks']
