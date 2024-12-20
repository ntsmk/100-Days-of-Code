class FlightData:
    #This class is responsible for structuring the flight data.
    def find_cheapest_flight(self, results1):
        results = results1
        for i in range(len(results)):
            print(results[3]["data"][0]["price"]["total"])