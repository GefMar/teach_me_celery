from celery import Celery
from .config import CELERY_BROKER, CELERY_BACKEND

app = Celery(
    "teach_me",
    broker=CELERY_BROKER,
    include=["celery_app.tasks", ],
)
