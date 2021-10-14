from stations_challenge import *

subway_station1 = SubwayStation('5th Ave/53rd St Station','5th Ave and 53rd St',['E', 'M'])
subway_station2 = SubwayStation('First Ave Station','First Avenue and East 14th Street',['L'])
bus_station1 = BusStation(['Boston', 'Albany', 'Philly','Atlantic City','Syracuse','Buffalo'], 'NYC Port Authority Greyhound Stop', '625 8th Ave.')

subway_station1.show_info()
print()
subway_station2.show_info()
print()
bus_station1.show_info()
