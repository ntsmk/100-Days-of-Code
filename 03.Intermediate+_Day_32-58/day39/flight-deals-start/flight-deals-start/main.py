#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from step2 import DataManager
from flight_search import FlightSearch

dm = DataManager()
sheet_data = dm.getEverything()
print(sheet_data)

# city_name = dm.getNames()
# price = dm.getPrice()

fs = FlightSearch()
# IATA_list = fs.getIATA(city_name)
# print(IATA_list)

# dm.updateIATA(IATA_list)

