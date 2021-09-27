print("Challenge: Favourite Restaurants")

print()

print("Question 1")

# '''
# Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

# Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
# 1. The latitude and longitude of Four Barrel Coffee 
# 2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
# 3. The website of Four Barrel Coffee
# '''


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

print(restaurant['latitude'])
print(restaurant['longitude'])
print(f"""The complete address of the Four Barrel Coffee Shop is"{restaurant['address1'], restaurant['city'], restaurant['state'], restaurant['country'], restaurant['zip_code']}""")

print(f"""We can also be found at"{restaurant['url']}""")


# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.


print("Question 2: Favorite Restaurants")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)


My_favorite_restaurant1 = {"name": "Peter Luger Steak House",
                           "address": "178 Broadway, Brooklyn, New York",
                           "Favorite_dish": "Prime Rib"
                           }

My_favorite_restaurant2 = {"name": "OLLIES", 
                           "address": "411 W 42nd Street, NYC, NY", 
                           "Favorite_dish": "Anything on the menu"
                           }

My_favorite_restaurant3 = {"name": "Juniors", 
                           "address": "386 Flatbush Ave. Extension, Brooklyn, NY",
                           "Favorite_dish": "Fried Butterfly Shrimp, Strawberry Cheesecake"
                           }


print(f"""My favorite restaurants are"{My_favorite_restaurant3['name'], My_favorite_restaurant3['address'], My_favorite_restaurant3['Favorite_dish']}""") 

 

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this


restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }

My_favorite_restaurant1 = {"name": "Peter Luger Steak House",
                           "address": "178 Broadway, Brooklyn, New York",
                           "Favorite_dish": "Prime Rib"}

My_favorite_restaurant2 = {"name": "OLLIES", 
                           "address": "411 W 42nd Street, NYC, NY", 
                           "Favorite_dish": "Anything on the menu"}                          

My_favorite_restaurant3 = {"name": "Juniors", 
                           "address": "386 Flatbush Ave. Extension, Brooklyn, NY",
                           "Favorite_dish": "Fried Butterfly Shrimp, Strawberry Cheesecake"}

print(My_favorite_restaurant1)
print(My_favorite_restaurant2)
print(My_favorite_restaurant3)

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print(My_favorite_restaurant3)
My_favorite_restaurant3.pop('Favorite_dish')
print(My_favorite_restaurant3)
#Removed 'Favorite dish from dictionary.

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

print(My_favorite_restaurant1)
My_favorite_restaurant1["address"] = '100 Broadway, Brooklyn, New York City'
print(My_favorite_restaurant1)

