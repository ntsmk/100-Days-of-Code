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

    def sendText(self, city1, price_sheet, price_api):
        city = city1
        price1 = price_sheet
        price2 = price_api

        for i in range(len(city)):
            if price2[i] != "N/A" and float(price2[i]) < float(price1[i]):
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    from_=from_number,
                    body=f"Low price alert! Only ${price2[i]} to fly from Whitehorse to {city[i]}",
                    to=to_number
                )
        print("text sent")
