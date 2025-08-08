# 37 habit tracker

import os
from dotenv import load_dotenv
import requests


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

CREATE_PIXEL_CONFIG = {
    "date": "20250809",
    "quantity": "70",
    
}

# graph_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=GRAPH_CONFIG, headers=HEADERS)
# print(response.text)


create_pixel_endpoint = f"{PIXELA_API}/{PIXELA_USERNAME}/graphs/{GRAPH_CONFIG['id']}"
response = requests.post(url=create_pixel_endpoint, json=CREATE_PIXEL_CONFIG, headers=HEADERS)
print(response.text)
