import json
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

import step2

load_dotenv()
ORIGIN = "YXY"
TODAY = datetime.today().strftime("%Y-%m-%d")
TOMORROW = (datetime.today() + timedelta(1)).strftime("%Y-%m-%d")
RETURN_DATE = (datetime.today() + timedelta(15)).strftime("%Y-%m-%d")
CURRENCY = "CAD"
ADULTS = 1
MAX = 1

# getting access token
API_KEY = os.getenv("API_KEY1")
API_SECRET = os.getenv("API_SECRET1")
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

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN1")
auth_header = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    # getting city IATA list
    def getIATA(self, city_list):
        city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        city_list = city_list
        IATA_list = []

        for i in range(len(city_list)):
            keyword = {
                "keyword": city_list[i]
            }
            response = requests.get(url=city_search_endpoint, headers=auth_header, params=keyword)
            IATA_list.append(response.json()["data"][0]["iataCode"])
        return IATA_list


    # searching flights
    flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    # for iata in range(len(IATA_list)):
    #     parameters = {
    #         "originLocationCode": ORIGIN,
    #         "destinationLocationCode": IATA_list[iata],
    #         "departureDate": TOMORROW,
    #         "returnDate": RETURN_DATE,
    #         "adults": ADULTS,
    #         "currencyCode": CURRENCY,
    #         "max": MAX
    #     }
    #     result_list = []
    #     response = requests.get(url=flight_offer_endpoint, headers=auth_header, params=parameters)
    #     result_list.append(response.json())
    #
    # print(result_list)
    # print(result_list[3])
    # print(result_list[3]["data"][0]["price"]["total"])
