import requests
from datetime import datetime

API_ID = ""
API_KEY = ""

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/copyOfMyWorkouts/workouts"

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

query = {
    'query': input("Tell me which exercise you did: ")
}

response_nu = requests.post(url=nutrition_endpoint, headers=headers, data=query)
# print(response_nu.json()["exercises"][0]["user_input"])

today = datetime.today().strftime("%d/%m/%Y")
exercise = response_nu.json()["exercises"][0]["user_input"].title()
duration = response_nu.json()["exercises"][0]["duration_min"]
calories = response_nu.json()["exercises"][0]["nf_calories"]

# todo step 4 write some code to use the Sheety API to generate a new row of data in your Google Sheet
# now I can add the raw by using dummy data so next step will be add the info from
parameter = {
    'workout': {
        'date': today,
        'time': "xx",
        'exercise': exercise,
        'duration': duration,
        'calories': calories,

    }
}
response_sh = requests.post(url=sheety_endpoint, json=parameter)
print(response_sh.text)