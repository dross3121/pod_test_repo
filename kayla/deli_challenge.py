
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
meats2 = []
cheeses2 = []
for x in meats:
        capx = x.capitalize()
        meats2.append(capx)
for y in cheeses:
        capy = y.capitalize()
        cheeses2.append(capy)  

print(meats2)
print(cheeses2)





print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []
for x in meats2:
    for y in cheeses2:
        sandwiches.append(x+" and "+y)

print(sandwiches)       

print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
customer_order = input("What would you like?")
print(customer_order)
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
for x in sandwiches:
    if(customer_order == x):
        print("we have it")
    else:
        print("sorry, we don't have it")