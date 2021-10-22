import numpy as np 

from stations_challenge import *

station1 = BusStation("Station 1", "Texas", False, ["location 1" , "location 2", "location 3"])
station2 = BusStation("Station 2", "Florida", False, ["location 1" , "location 2", "location 3"])
station3 = BusStation("Station 3", "California", False, ["location 1" , "location 2", "location 3"])
closed = "closed"
routes_joined = ", ".join(station1.routes)
if station1.open == False:
    print(f"{station1.station_names}, is at the {station1.locations} location, but is currently {closed}. Here are the routes: {routes_joined}.")





