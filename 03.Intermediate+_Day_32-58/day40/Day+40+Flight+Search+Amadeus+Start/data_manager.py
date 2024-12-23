import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
auth = HTTPBasicAuth(os.getenv("SHEETY_USRERNAME"), os.getenv("SHEETY_PASSWORD"))

SHEETY_PRICES_ENDPOINT = os.getenv("PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("USERS_ENDPOINT")

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=auth)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=auth
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, auth=auth)
        data = response.json()['users']
        email_address = [email['whatIsYourEmailAddress'] for email in data]
        return email_address
