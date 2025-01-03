import requests
from datetime import datetime

MY_LAT = 60.719560486554776
MY_LNG = -135.05267151196642

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# position = (latitude,longitude)
#
# print(position)
# 60.719560486554776, -135.05267151196642
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)