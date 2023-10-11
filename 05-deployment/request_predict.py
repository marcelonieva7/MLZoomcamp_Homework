import requests

URL = 'http://192.168.1.17:9696/predict'
CLIENT = {"job": "unknown", "duration": 270, "poutcome": "failure"}


response = requests.post(URL, json=CLIENT).json()

print(f'Score = {round(response, 3)}')