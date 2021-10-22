from stations_challenge import *

station3 = BusStation('Freeport Loop','59th Street and Columbus Circle', ['Brooklyn', 'Queens', 'Staten Island'])
station3.show_info()

station4 = BusStation('Jones Beach','161st Street and Amsterdam', ['Albany', 'South Jersey', 'Holland Tunnel'])
station4.show_info()

station5 = SubwayStation(station_name ='Fulton Street',location = 'Fulton Street and 1st Avenue', lines = ['A', 'C', 'E', '2'])
station5.show_info()