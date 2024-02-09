import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_DIR = os.path.join(BASE_DIR, "zip_folder/zipped")


file_path = os.path.join(BASE_DIR, "zip_folder/zipped/test.zip")
url = "http://127.0.0.1:8000/zip"

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)
print(response.json())
