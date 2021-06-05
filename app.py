import os

from logtube import create_app, ext_celery
import logtube.tasks

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = create_app()
celery = ext_celery.celery


@app.route('/')
def home():
    return {"status": "Python REST Servicve is UP", "api": "/api/1.0/search"}


@app.route('/transcribe/<playlist_id>')
def transcribe(playlist_id):
    task = logtube.tasks.crawl_most_popular.delay()
    return {"task_id": task.task_id, "status": task.status}
