# Create variable for name to be input using input() function, and receive users answers in the terminal
name = input('Type in your name then press enter. ')
# Create variable to greetaddress user by name 
greeting = input(f'Hello {name}. I will be happy to help you figure out the amount you have to spend on your meal. Press enter.')
#Create a variable to get input from user about the cost of their meal using float in case there is a cent value ex: $80.15.
foodcost = float(input('How much did your food cost? Only enter the number.'))
# Print information to let user view the amount they entered.
print(f'You entered ${foodcost}. ')
#Create a variable to get users input on the amount they wish to pay for a tip.
tip = int(input('How much percentage do you want to pay as a tip? Only enter the number. Dont be cheap :) . '))
# Print the tip amount entered by user.
print(f'Your tip will be {tip}%. ')
#Create a variable assigning it a value of .10 for the 10 percent tax to be paid for the bill.
tax = .10
# Create a variable to input information telling the user that they will be charged a 10 percent tax.
taxes = input('Please be aware that a 10% sales tax will be added to your bill. Press enter. ')
# Create a variable to find out how many people will be dividing the bill and give user a message.
people = float(input('How many people are splitting the bill? I will assume that you will be dividing the bill equally. '))
#Create a variable to calculate the tip based on the cost of the food and tip amount entered.
amount_tip = foodcost * tip/100
#Create a variable to calculate the amount of tax based on the cost of the food and the tax to be paid.
amount_tax = foodcost * tax
#Create a variable to calculate the total cost the user will pay.
exact_tax = foodcost/tax
total = foodcost + amount_tip + amount_tax
# Create a variable to calculate the amount each person will pay for the bill.
individual = total/people
# Use print function and f string to print out the cost of food and tip amount using variables.
print(f'Your food cost ${foodcost} and your tax was ${amount_tax}.')
# Use f string to print out tip amount.
print(f'Additionally, your tip was ${amount_tip}.')
# Use f string to print out the total with tax and tip.
print(f'Your total with tax and tip is ${total}.')
# Print out amount each person will pay.
print(f'Each person will pay ${individual}.')
# Print a message for user using f string and print function.
print(f'{name}, I hope that you enjoyed your meal and had a great time. Hoping the ${individual} was worth it! :)')

