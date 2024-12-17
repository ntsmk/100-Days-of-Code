import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv
import os

endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/copyOfFlightDeals2/prices"

load_dotenv()
auth = HTTPBasicAuth(os.getenv("UID1"), os.getenv("PASS1"))

response = requests.get(url=endpoint, auth=auth)
# print(response.json())
pprint(response.json())