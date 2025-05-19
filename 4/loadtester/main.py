# Niveles/4/loadtester/main.py
import requests
import time
import random

URL = "http://api-service/predict"

while True:
    payload = {"data": [random.random() for _ in range(4)]}
    try:
        requests.post(URL, json=payload)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
