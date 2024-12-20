from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_number = os.getenv("from_number")
to_number = os.getenv("to_number")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def sendText(self):

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
