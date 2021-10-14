print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
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

print(restaurant)
print()
# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print("The latitude of Four Barrel Coffee is",restaurant["latitude"],"and"," the longitude is",restaurant["longitude"])
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print("The address is",restaurant['address1'])
print("              ",restaurant['city']," ",restaurant['state']," ",restaurant['zip_code'])
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print("The website URL of Four Barrel Coffee is",restaurant["url"])


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich" }
'''
restaurant_1 = {
    "name1": "Kata Robata",
    "address1": "3600 Kirby Suite H, Houston TX 77098",
    "favorite_dish1": "Sushi"}
print(restaurant_1)
print()

restaurant_2 = {
    "name2": "Phat Eatery",
    "address2": "23119 Colonial Parkway Suite B2, Katy TX 77449",
    "favorite_dish2": "Malaysian Chicken Curry"}
print(restaurant_2)
print()
restaurant_3 = {
    "name3": "Brother's Pizzeria",
    "address3": "3820 N Shepherd Dr, Houston TX 77018",
    "favorite_dish": "pizza"}
print(restaurant_3)
print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there. 
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
restaurant_2.pop("favorite_dish2")
print(restaurant_2)
print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
restaurant_1["address1"] = "123 Elm St, Houston TX 77002"
print(restaurant_1["address1"])
print(restaurant_1)
print()
