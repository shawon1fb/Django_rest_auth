import requests


def api_token_auth():
    url = r"http://127.0.0.1:8000/api-token-auth/"
    data = {
        "username": "shawon1fb",
        "password": "secret"
    }
    r = requests.post(url=url, data=data)
    json_data = r.json()
    token = json_data['token']

    print(token)


api_token_auth()
