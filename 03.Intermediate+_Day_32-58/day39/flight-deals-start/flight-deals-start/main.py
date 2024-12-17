#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from step2 import DataManager

dm = DataManager()
sheet_data = dm.getEverything()
print(sheet_data)


