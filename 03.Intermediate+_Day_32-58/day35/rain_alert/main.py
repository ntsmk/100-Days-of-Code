import requests

api_key = ""
MY_LAT = 60.721188
MY_LONG = -135.056839

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()
print(response.status_code)
print(data)
