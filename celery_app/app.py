import datetime

from celery import Celery
from .config import CELERY_BROKER, CELERY_BACKEND
routes = {
    "teach_me.*": {"queue": "teach_me"}
}
app = Celery(
    "teach_me",
    broker=CELERY_BROKER,
    backend=CELERY_BACKEND,
    include=["celery_app.tasks", ],
)

# app.conf.task_routes = routes
app.conf.task_queue_max_priority = 10
app.conf.task_default_priority = 1
app.conf.result_expires = datetime.timedelta(hours=2)
