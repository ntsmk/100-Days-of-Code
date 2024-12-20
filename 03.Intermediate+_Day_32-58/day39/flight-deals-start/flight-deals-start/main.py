#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from step2 import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

dm = DataManager()
fs = FlightSearch()
fd = FlightData()

# sheet_data = dm.getEverything()
# print(sheet_data)

city_name = dm.getNames()
IATA_list = fs.getIATA(city_name)
# print(IATA_list)
# dm.updateIATA(IATA_list)

# todo call the flight search method from flight search
results = fs.flightSearch(IATA_list)
# print(results)

fd.find_cheapest_flight(city_name, results)

