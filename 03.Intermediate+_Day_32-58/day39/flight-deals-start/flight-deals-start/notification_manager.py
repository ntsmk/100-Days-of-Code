import os
from twilio.rest import Client

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_number = os.getenv("from_number")
to_number = os.getenv("to_number")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body="test",
        to=to_number
    )