import requests


def get_status():
    data = requests.get("http://127.0.0.1:8000/status")
    print(data.content)


get_status()
