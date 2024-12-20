class FlightData:
    #This class is responsible for structuring the flight data.
    def find_cheapest_flight(self, city_names1, results1):
        results = results1
        city_names = city_names1
        for i in range(len(results)):
            price = results[i]
            name = city_names[i]
            print(f"{name}: {price} CAD")