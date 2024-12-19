import requests
import os

endpoint = "https://api.sheety.co/1105c27e55d43a710547b8fe3239700f/copyOfFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def getNames(self):
        response = requests.get(url=endpoint)
        names = []
        for i in range(len(response.json()["prices"])):
            names.append(response.json()["prices"][i]["city"])
        return names

    def getPrice(self):
        response = requests.get(url=endpoint)
        prices = []
        for i in range(len(response.json()["prices"])):
            prices.append(response.json()["prices"][i]["lowestPrice"])
        return prices
