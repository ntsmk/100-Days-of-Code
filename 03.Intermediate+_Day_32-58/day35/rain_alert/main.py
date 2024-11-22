import requests

api_key = "a2b44f595520910382407a3218b16b9b"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 49.695596
MY_LONG = -124.990431

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
print(data)
# todo access the weather ID and print it out -> done, add if statement and print out bring umbrella
print(data["list"][0]["weather"][0]["id"])
