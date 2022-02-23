import uuid
import requests
from .app import app
import settings


@app.task(name="download_page")
def download_page(url):
    response = requests.get(url)
    file_name = f"{uuid.uuid4()}.html"
    file_path = settings.html_path.joinpath(file_name)
    with open(file_path, "wb") as file:
        file.write(response.content)
    return str(file_path)


@app.task(name="parse_page")
def parse_page(path):
    pass


@app.task(name="download_file")
def download_file(url):
    pass
