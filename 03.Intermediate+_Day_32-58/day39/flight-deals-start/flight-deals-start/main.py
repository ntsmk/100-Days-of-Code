#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager2 import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
fd = FlightData()
nm = NotificationManager()

# sheet_data = dm.getEverything()
# print(sheet_data)

city_name = dm.getNames()
IATA_list = fs.getIATA(city_name)
# print(IATA_list)
# dm.updateIATA(IATA_list)

results = fs.flightSearch(IATA_list)
# print(results)
fd.find_cheapest_flight(city_name, results)
sheet_price = dm.getPrice()
# print(sheet_price)
nm.sendText(city_name, sheet_price, results)
