import requests
from datetime import datetime
import smtplib
import time

my_email = "whereismycoffee9@gmail.com"
password = ""

MY_LAT = 60.721188 # Whitehorse latitude
MY_LONG = -135.056839 # Whitehorse longitude

# API 1: getting ISS location
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# API 2 getting sunrise/sunset time
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

time_now_hour = datetime.now().hour

#If the ISS is close to my current position (condition 1)
#Your position is within +5 or -5 degrees of the ISS position.
# and it is currently dark (and condition 2)
# Then send me an email to tell me to look up. (action to take)
# print(iss_latitude)
# print(iss_longitude)
print(sunrise)
print(sunset)
print(time_now_hour)

# BONUS: run the code every 60 seconds.
while True:
    if iss_latitude -5 <= MY_LAT <= iss_latitude +5 and iss_longitude -5 <= MY_LONG <= iss_longitude +5 and time_now_hour > sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS is close by\n\nCheck the sky. Look up!")
        print("email sent")
    else:
        print("ISS is not close by")
    time.sleep(60)
