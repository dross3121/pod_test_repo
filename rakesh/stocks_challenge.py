print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
facebook = 250
google = 1400
microsoft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name? ")
print (f"Hi, {name}!")
print()

# TODO: Write code to ask the client his savings and save it to another variable.
# BONUS while loop utilized to make sure user enters a number, and not a letter, for savings.

while True:
    try:
        savings = float(input("What is your savings? "))
    except ValueError:
        print("Sorry, please enter a numerical value.")
        continue
    else:
        break
# BONUS Letting user know what shares they can afford. If user doesn't have a minimum of $100 for Apple, program ends.    
if savings <=100:
    print("You don't have enough money for these stocks.")
    quit()
elif savings >= 100 and savings <= 199:
    print("You can only afford Apple stocks.")
elif savings >= 200 and savings <= 249:
    print("You can only afford Apple and Microsoft stocks.")
elif savings >= 250 and savings <=1399:
    print("You can only afford Apple, Microsoft, and Facebook stocks.")
elif savings >=1400 and savings <=2999:
    print("You can only afford Apple, Microsoft, Facebook, and Google stocks.")
print()

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
# BONUS while loop used to ensure user inputs stock from specified choices of Amazon, Apple, Facebook, Google or Micorsoft.
while True:
    stock = input("Which stock are you interested in? (Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook,\n'goog' for Google and 'msft' for Microsoft.) ")
    if stock.lower() not in ('amzn','aapl', 'fb', 'goog', 'msft'):
        print(f"{stock} is not valid stock. Please re-enter a valid stock correctly.")
        continue
    else:
        break
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn':
    shares = round((savings/amazon))
    print(f"{name} has ${round(savings)} in savings and can buy {shares} shares of Amazon at the current price of ${amazon}/share.")
elif stock == 'aapl':
    shares = round((savings/apple))
    print(f"{name} has ${round(savings)} in savings and can buy {shares} shares of Apple at the current price of ${apple}/share.")
elif stock == 'fb':
    shares = round((savings/facebook))
    print(f"{name} has ${round(savings)} in savings and can buy {shares} shares of Facebook at the current price of ${facebook}/share.")
elif stock == 'goog':
    shares = round((savings/google))
    print(f"{name} has ${round(savings)} in savings and can buy {shares} shares of Google at the current price of ${google}/share.")
else:
    shares = round((savings/microsoft))
    print(f"{name} has ${round(savings)} in savings and can buy {shares} shares of Microsoft at the current price of ${microsoft}/share.")
print()


