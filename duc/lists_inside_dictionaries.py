#=========================================LISTS INSIDE DICTIONARIES LECTURE NOTES w/PAUL================================================
cart = {
    'fruit' : ['mangoes', 'pears', 'apples'],   #NESTED DATA
    'veggies' : ['spinach', 'peas'],    #NESTED DATA
    'total_price' : 23.21   #NON-NESTED DATA
}

print(cart)

print(type(cart))

print(type(cart['veggies']))

print(cart['veggies'])

# YOU CAN USE NUMERIC INDEXING TO RETREIVE SPECIFIC ITEMS FROM A LIST INSIDE A DICTIONARY
print(cart['veggies'][1])

#====================================REPLACING AN ELEMENT WITHIN A LIST NESTED INSIDE A DICTIONARY======================================

(cart['fruit'][0]) = 'papayas' #REPLACING MANGOES WITH PAPAYAS
print(cart)

# LIST : ORDERED ----INDEX
# DICTIONARY : NOT ORDERED ----KEY

#===========================================DICTIONARIES INSIDE DICTIONARIES============================================================

restaurants = {
    'El Basurero': {
        'address': '32-17 Steinway St, Queens, NY 11103',
        'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'
    },
    'SriPraPhai': {
        'address': '64-13 39th Ave, Woodside, NY 11377',
        'menu_url': 'https://sripraphai.com/menu.html'
    }
}

# print(restaurants)

print(restaurants['SriPraPhai'])

restaurants['CookingWithDuc'] = {'address': '2525 Robert Avenue, Los Angeles, Ca 90007',
                                'phone_number': '310-678-9808'}

print(restaurants)

#======================================UPDATING AND REMOVING NESTED KEY VALUE PAIRS====================================================

# restaurants['CookingWithDuc']['menu_url'] = 'http://www.CookingWithDuc.com' #ADDING URL LINK 

#print(restaurants)

# restaurants['CookingWithDuc'].pop('phone_number') #REMOVING THE PHONE NUMBER

#print(restaurants)

# ================================================DICTIONARIES NESTED INSIDE LIST=======================================================
# EXAMPLE:

# a = [{}, {}, {}]

# print(a)
# print(type(a))

# print(type(a[0]))

users = [
    {'username': 'alanna', 'password': 'javascript', 'last_login': '9/28/2020'},
    {'username': 'aryn', 'password': 'dictionaries'},
    {'username': 'yusuf', 'password': 'django', 'last_login': '9/26/2020'},
    {'username': 'paul', 'password': 'github'}
]

# print(users)

# print(users[2])
# print(users[2]['password'])


users.append({'username': 'serena', 'password': 'java'})

# print(users)
#============================================UPDATING DICTIONARIES NESTED INSIDE A LIST=================================================
users[-1]['verified_account'] = True

users[-1]['password'] = 'python216' #UPDATING PASSWORD WITH NEW ONE

users[0].pop('last_login') #REMOVING THE 'LAST_LOGIN' VALUE

print(users)