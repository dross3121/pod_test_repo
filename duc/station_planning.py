# # Q1.)
# class Station():
#     def __init__(self, station_name, location):
#         self.station_name = station_name
#         self.location = location
    
#     def show_info(self):
#         print(f'{self.station_name} station is located at {self.location}')

# class SubwayStation(Station):
#     def __init__(self, station_name, location, lines):
#         super().__init__(station_name, location)
#         self.lines = lines
#     def show_info(self):
#         print(f'{self.station_name}, station is located at {self.location} and lines{self.lines}stop here.')
# # Q2.)
# class BusStation(Station):
#     def __init__(self, station_name, location, routes):
#         super().__init__(station_name, location)
#         #  ['DC', 'Philly', 'Pittsburgh']
#         self.routes = routes
#         self.open = True

#     def show_info(self):
#         print(f'{self.station_name}, station is located at {self.location}.\n This bus station has the following {self.routes}.')
#         if self.open == True:
#             print("This station is open")
#         else:
#             print("This station is closed")
        
#     def open_station(self):
#         self.open = True
#         print(f'This station is open')
        
#     def close_station(self):
#         self.close = True
#         print(f'This station is closed')  


class UnionStation():
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location

    def show_info(self):
        print(f'{self.station_name} is located in {self.location}')


class Metro(UnionStation):
    def __init__(self, station_name, location, metro_lines):
        super().__init__(station_name, location)
        self.metro_lines = metro_lines

    def show_info(self):
        print(f'{self.station_name} is located in {self.location} and the {self.metro_lines} use this location as a hub for all of Los Angeles.')

class MTA():
    def __init__(self, station_name, locations, bus_lines):
        self.bus_lines = bus_lines
        self.locations = locations
        self.station_name = station_name

    def show_info(self):
        print(f'{self.station_name}, is located at {self.locations}.\n This bus station has the following {self.bus_lines}.')


