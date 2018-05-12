from os import getenv

from youtube_dl import YoutubeDL
from celery import Task
from celery.result import AsyncResult

from celeree import celery
from manage import app
from manage import sse
from events import extract_info_success


class ExtractInfoTask(Task):
    name = 'extract_info'

    def run(self, url):
        youtubedl = YoutubeDL()
        return youtubedl.extract_info(
            url, download=False
        )

    def on_success(self, retval, uuid, *args, **kwargs):
        with app.app_context():
            extract_info_success(sse, retval)

celery.tasks.register(ExtractInfoTask())

extract_info = celery.tasks[ExtractInfoTask.name]
