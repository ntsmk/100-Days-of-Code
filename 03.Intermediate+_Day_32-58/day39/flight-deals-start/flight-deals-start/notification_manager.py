import os
from twilio.rest import Client
# import flight_search

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_number = os.getenv("from_number")
to_number = os.getenv("to_number")

# todo edit "body", now it is just "test", import the data from "flight_search"
# todo figure out if sentence in flight_search.py
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendText(self, price, origin, destination):
        # later copy and paste here to give the access in flight_search
        origin = origin
        destination = destination
        price = price

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=from_number,
            body=f"Low price alert! Only ${price} to fly from {origin} to {destination}",
            to=to_number
        )

    sendText("xxx", "100","XYX", "YVR")