from stations_challenge import *

station2 = BusStation(station_name = 'Another Station', location = '123 Another Street', routes = ['1st street', '2nd street', '3rd street'])
station2.show_info()

station3 = SubwayStation(station_name = 'Another Subway', location = 'ABC Another line', lines = ['33', '66', '99'])
station3.show_info()

station4 = BusStation(station_name = 'Yet another station', location = '456 Another street', routes = ['4th', '5th', '6th'])
station4.show_info()