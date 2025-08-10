
import requests
import pprint

url = "https://httpbin.org/headers"
headers = {
    "Authorization": "Bearer XYZ123",
    "Custom-header": "Ahoj z Pythonu",
}

response = requests.get(url, headers=headers)


formatted_response = pprint.pformat(response.json())
print(formatted_response)
