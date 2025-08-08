# 37 habit tracker

import os
from dotenv import load_dotenv
import requests


load_dotenv()

PIXELA_API = os.getenv("PIXELA_API")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
USER_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": "lukemorte",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
string = PIXELA_API + "/lukemorte"
print(string)
# response = requests.post(url=PIXELA_API, json=USER_PARAMS)
response = requests.delete(string)
response.raise_for_status()
print(response)
