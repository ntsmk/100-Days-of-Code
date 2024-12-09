import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

API_ID = ""
API_KEY = ""

basic = HTTPBasicAuth('whereismycoffee', '')
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)

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

date = datetime.today().strftime("%d/%m/%Y")
time = datetime.now().strftime('%H:%M:%S')
exercise = response_nu.json()["exercises"][0]["user_input"].title()
duration = response_nu.json()["exercises"][0]["duration_min"]
calories = response_nu.json()["exercises"][0]["nf_calories"]

parameter = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories,

    }
}
response_sh = requests.post(url=sheety_endpoint, json=parameter, auth=basic)
print(response_sh.text)