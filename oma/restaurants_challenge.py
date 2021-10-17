print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant:\t 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''

restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}
print("Go through the dictionary and print out the following 3 pieces of \
\ninformation about the restaurant:\
\n\n 1. The latitude and longitude of Four Barrel Coffee\n")

#1. The latitude and longitude of Four Barrel Coffee.
restaurant["latitude"], f'degrees latitude'
restaurant["longitude"], f'degrees longitude'
# Assigned variable for latitube & longitude to be placed in string.
lait = (restaurant["latitude"], f'degrees latitude')
longi = (restaurant["longitude"], f'degrees longitude')
#Printed statement for latitude and longitude of Four Barrel Coffee in string format
print (f'The latitude and longitude of Four Barrel Coffee is \
\n {lait} and {longi}\n\n')

print("2. The complete address of Four Barrel Coffee, formatted as a\
\n string it should include the address, city, state and the zip code.\n")
#Pull address, city, state and the zip code out dictionary 
restaurant["address1"]
restaurant["city"] 
restaurant["state"]
restaurant["zip_code"]
#Create variable for the complete address of Four Barrel 
# Coffee to be placed in string
complete_address = (restaurant["address1"], restaurant["city"], 
 restaurant["state"], restaurant["zip_code"])
#Printed statement for The complete address of Four Barrel Coffee
print(f'The complete address of Four Barrel Coffee is:{complete_address}\n\n')

print("3. The website of Four Barrel Coffee:\n")
#Pull url out dictionary 
restaurant["url"]
#Assigned varible for Four Barrel Coffee Website 
fbc_website = restaurant["url"]
#Printed Four Barrel Coffee URL
print(f'The URL for Four Barrel Coffee is, {fbc_website}.\n\n')


print("Question 2")
print("Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:\
\n 1. name : name of the resturant (string)\
\n 2. address: address of the restaurant (string)\
\n 3. favourite_dish: your favourite thing to order at the restaurant (string)\n")
print("TODO: Print each dictionary")
# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#        1. name : name of the resturant (string)
#        2. address: address of the restaurant (string)
#        3. favourite_dish: your favourite thing to order at the restaurant (string)
# TODO: Print each dictionary
# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''


restaurant_1  = {
    "name": "Ricardo",
    "address" : "2145 2nd Ave, New York 10029",
    "favourite_dish" : "Ricardos Plattter" 
}

restaurant_2  = {
    "name": "CUT by Wolfgang Puck",
    "address" : "3325 Las Vegas Blvd S, Las Vegas, NV 89109",
    "favourite_dish" : "Filet Mignon" 
}
    
restaurant_3  = {
    "name": "Triple Deuce Restaurant & Grill",
    "address" : "3601 Boston Road, Bronx, 10469",
    "favourite_dish" : "Salmon & Mash Potatoes" 
}

print(f'favourite restaurant 1\
    \n {restaurant_1}\n')

print(f'favourite restaurant 2\
    \n {restaurant_2}\n')

print(f'favourite restaurant 3\
    \n {restaurant_3}\n\n')

print("Question 3\
    \nImagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.\
     \nRemove the 'favourite_dish' key value pair from that restaurant's dictionary:\n")

'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
restaurant_3.pop("favourite_dish")

# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant​
print(f'favourite restaurant 3\
    \n {restaurant_3}\n\n')

print("Question 4\
\nImagine that another one of your most favourite restaurants modified its address. \
\nUpdate just this value in that restaurant's dictionary:\n")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
restaurant_1["address"] = "113 West 116th Street Harlem,New York 10026"

# TODO: Print the new address of the restaurant 
#       by accessing that field of the restaurant's dictionary

new_spot = restaurant_1["address"]

print(f'My favorite resturant #1 has moved to {new_spot} \n')

# TODO: Print the updated dictionary.
print(f'Favourite Restaurant 1\
    \n {restaurant_1}\n')

