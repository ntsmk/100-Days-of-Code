import os
from twilio.rest import Client
# import flight_search

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_number = os.getenv("from_number")
to_number = os.getenv("to_number")

# todo edit "body", now it is just "test", import the data from "flight_search"
# todo need to figure it out why this method is not working as it is supposed to be

# todo figure out if sentence in flight_search.py -> need to use main.py for circulation issue
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendText(price, origin, destination):
        price = price
        origin = origin
        destination = destination

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=from_number,
            body=f"Low price alert! Only ${price} to fly from {origin} to {destination}",
            to=to_number
        )

    sendText("2000", "YXY", "TYO")
    # price is origin
    # origin is destination
    # the last parameter is destination
    # if I delete "self" from the param, it solves it
