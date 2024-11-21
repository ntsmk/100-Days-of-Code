import requests

api_key = ""
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 60.721188
MY_LONG = -135.056839

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
