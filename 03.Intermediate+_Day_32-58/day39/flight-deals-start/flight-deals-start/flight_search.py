import json

import requests
import os
import data_manager

# getting access token
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
oauth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
client = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET,
}
# response = requests.post(url=oauth_endpoint, headers=headers, data=client)
# print(response.text)
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
auth_header = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# getting city IATA list
city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
d = data_manager.DataManager()
city_list = d.getNames()
IATA_list = []
for i in range(len(city_list)):
    keyword = {
        "keyword": city_list[i]
    }
    response = requests.get(url=city_search_endpoint, headers=auth_header, params=keyword)
    IATA_list.append(response.json()["data"][0]["iataCode"])
print(IATA_list)

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # use Amadeus API

    amadeus_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    parameters = {
        "originLocationCode": "YXY",
        "destinationLocationCode": "PAR",
        "departureDate": "2025-05-01",
        "adults": 1,
        "currencyCode": "CAD",
        "max": 10
    }
    # response = requests.get(url=amadeus_endpoint, headers=auth_header, params=parameters)
    # print(json.dumps(response.json()))
