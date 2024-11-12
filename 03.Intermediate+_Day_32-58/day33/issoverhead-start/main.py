import requests
from datetime import datetime

MY_LAT = 60.721188 # Your latitude
MY_LONG = -135.056839 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "America/Whitehorse",
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position (condition 1)
#Your position is within +5 or -5 degrees of the ISS position.
print(iss_latitude)
print(iss_longitude)

# and it is currently dark (and condition 2)
# Then send me an email to tell me to look up. (action to take)
# BONUS: run the code every 60 seconds. (after think)

# there are 3 tasks, need to make it more clear

print(sunrise)
print(sunset)
# print(data)
print(time_now)
