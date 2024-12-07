import requests

API_ID = ""
API_KEY = ""

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

query = {
    'query': input("tell me which exercise you did: ")
}

response = requests.post(url=api_endpoint, headers=headers, data=query)
print(response.json())