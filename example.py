# from celery_app.tasks import download_page
# from celery_app import worker_app
from celery import Celery
app = Celery('teach_me', broker='amqp://guest:guest@192.168.1.9:5672')
url = "https://lenta.ru"

# a = download_page.delay(url)
b = app.send_task(name="download_page", kwargs={"url": url}, priority=1)
# download_page.s(url).apply_async()
print(1)