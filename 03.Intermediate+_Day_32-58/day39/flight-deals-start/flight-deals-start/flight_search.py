import json
import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()
ORIGIN = "YXY"
TODAY = datetime.today().strftime("%Y-%m-%d")
TOMORROW = (datetime.today() + timedelta(1)).strftime("%Y-%m-%d")
SIX_MONTH = (datetime.today() + timedelta(180)).strftime("%Y-%m-%d")
RETURN_DATE = (datetime.today() + timedelta(15)).strftime("%Y-%m-%d")
CURRENCY = "CAD"
ADULTS = 1
MAX = 1

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # getting access token
        _api_key = os.getenv("API_KEY1")
        _api_secret = os.getenv("API_SECRET1")
        oauth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        client = {
            "grant_type": "client_credentials",
            "client_id": _api_key,
            "client_secret": _api_secret,
        }
        response_token = requests.post(url=oauth_endpoint, headers=headers, data=client)

        _token = response_token.json()["access_token"]
        self.auth_header = {
            "Authorization": f"Bearer {_token}"
        }

    # getting city IATA list
    def getIATA(self, city_list):
        city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        city_list = city_list
        IATA_list = []

        for i in range(len(city_list)):
            keyword = {
                "keyword": city_list[i]
            }
            response = requests.get(url=city_search_endpoint, headers=self.auth_header, params=keyword)
            IATA_list.append(response.json()["data"][0]["iataCode"])
        return IATA_list


    # searching flights
    def flightSearch(self):
        flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        parameters = {
                "originLocationCode": ORIGIN,
                "destinationLocationCode": "PAR",
                "departureDate": TOMORROW,
                "returnDate": RETURN_DATE,
                "adults": ADULTS,
                "currencyCode": CURRENCY,
                "nonStop": "true",
                "max": MAX
            }
        response = requests.get(url=flight_offer_endpoint, headers=self.auth_header, params=parameters)
        print(json.dumps(response.json()))
