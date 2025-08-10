# 37 habit tracker

import os
from dotenv import load_dotenv
import requests
from datetime import datetime


load_dotenv()

PIXELA_API = os.getenv("PIXELA_API")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


# graph_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)


today = datetime(year=2025, month=8, day=8)

CREATE_PIXEL_CONFIG = {
    "date": today.strftime("%Y%m%d"),
    "quantity": 0,
}


UPDATE_PIXEL_CONFIG = {
    "quantity": input("How many km did you cycle today?: "),
}

DELETE_PIXEL_CONFIG = {
    
}


# create_pixel_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs/{GRAPH_CONFIG['id']}"
# response = requests.post(url=create_pixel_endpoint, json=CREATE_PIXEL_CONFIG, headers=HEADERS)
# print(response.text)

update_pixel_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs/{GRAPH_CONFIG['id']}/{today.strftime('%Y%m%d')}"
response = requests.put(url=update_pixel_endpoint, json=UPDATE_PIXEL_CONFIG, headers=HEADERS)
print(response.text)

# delete_pixel_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs/{GRAPH_CONFIG['id']}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
# print(response.text)