import requests

API_ID = ""
API_KEY = ""

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/myWorkouts/workouts"

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

query = {
    'query': input("tell me which exercise you did: ")
}

response = requests.post(url=api_endpoint, headers=headers, data=query)
print(response.json())

# todo step 4 write some code to use the Sheety API to generate a new row of data in your Google Sheet
# -> use POST
# -> read documentation first