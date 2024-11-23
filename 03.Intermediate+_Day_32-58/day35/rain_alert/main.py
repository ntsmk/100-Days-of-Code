import requests
from twilio.rest import Client


api_key = ""
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = ''
auth_token = ''

MY_LAT = 49.695596
MY_LONG = -124.990431
COUNT = 4

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": COUNT,
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
print(data)

condition_list = []
for i in range(COUNT):
    condition_list.append(data["list"][i]["weather"][0]["id"])

if any(x < 700 for x in condition_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='',
        body='Hello it is going to rain, bring your umbrella',
        to=''
    )

    print(message.status)
