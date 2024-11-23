import requests

api_key = ""
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
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
# for i in condition_list:
#     if i < 700:
#         print("bring your umbrella")
if any(x < 700 for x in condition_list):
    print("bring your umbrella")
