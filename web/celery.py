from celery import Celery

celery = Celery('offline_tube')

celery.config_from_object('web.celeryconfig')

if __name__ == '__main__':
    celery.start()
