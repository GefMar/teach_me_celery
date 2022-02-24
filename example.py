import datetime

from celery_app.tasks import download_page
from celery_app import worker_app

# from celery_app import worker_app
from celery import Celery
app = Celery('teach_me', broker='amqp://guest:guest@192.168.1.9:5672', backend='redis://192.168.1.9:6379')
app.conf.task_queue_max_priority = 10
app.conf.task_default_priority = 1
app.conf.result_expires = datetime.timedelta(hours=2)

url = "https://lenta.ru"

# a = download_page.delay(url)
# b = app.send_task(name="download_page", kwargs={"url": url}, priority=1)
a = download_page.apply_async(kwargs={"url": url}, priority=1)
print(1)
