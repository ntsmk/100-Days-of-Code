import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import os

endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/copyOfFlightDeals2/prices"
put_endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/copyOfFlightDeals2/prices/2"
load_dotenv()
auth = HTTPBasicAuth(os.getenv("UID1"), os.getenv("PASS1"))

class DataManager:

    def getEverything(self):
        response = requests.get(url=endpoint, auth=auth)
        return response.json()

    param = {
        'price': {
            'iataCode': "TESTING",
        }
    }

    # response = requests.put(url=put_endpoint, json=param, auth=auth)
    # print(response.text)