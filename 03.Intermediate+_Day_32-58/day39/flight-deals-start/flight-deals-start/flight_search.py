import requests
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # use Amadeus API
    API_KEY = os.environ["API_KEY"]
    API_SECRET = os.environ["API_SECRET"]

    amadeus_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    parameters = {
        "originLocationCode": "YXY",
        "destinationLocationCode": "TYO",
        "departureDate": "2024-05-01",
        "adults": 1
    }
    # response = requests.get(url=amadeus_endpoint, )
