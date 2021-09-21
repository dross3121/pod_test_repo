print("Challenge 3.2: Playing with the stock market")



# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200


print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
name = input("What is your name? ")
print(name)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

user_input = int(input("how much savings do you have? "))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")


print(user_input)

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.


# Your code should look like this:




num_stocks = 0
if stock == "amzn":
    price = amazon
    num_stocks = int(user_input/price)
elif stock == "aapl":
    price = apple
    num_stocks = int(user_input/price)

elif stock == "fb":
    price = fb
    num_stocks = int(user_input/price)

elif stock == "goog":
    price = google
    num_stocks = int(user_input/price)

elif stock == "msft":
    price = msft
    num_stocks = int(user_input/price)

else: 
    price = "Can not calculate your total. Please try again later.."
print(f"you can spend: {price}")




print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{name} has ${user_input} in savings and is eligible to buy {num_stocks} {stock} shares at the price of ${price} each.")

