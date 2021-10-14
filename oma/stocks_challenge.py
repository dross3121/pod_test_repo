print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200




print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
f_name = input("Please enter Full Name.  ")
print()
# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("Please enter savings ammount.  "))
print()
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.  ")
print()

current_price = 0

if stock == "amzn":
    print   (f"Thank you {f_name}, you have choosen to invest in Amazon.com Incorporation (amzn) with in ${savings} your savings.   ")
    purchase = savings / amazon
    current_price = amazon
    purchase = input ("How many shares you would like to purchase of Amazon.com Incorporation (amzn)?  ")
    print()
   
elif stock == "aapl":
    print   (f"Thank you {f_name} you have choosen to invest in Apple Incorporation (aapl) with in ${savings} savings.    ")
    purchase = savings / apple 
    current_price = apple
    purchase = input ("How many shares you would like to purchase of Apple Incorporation (aapl)?  ")
    print()

elif stock == "fb":
    print   (f"{f_name} you have choosen to invest in Facebook Incorporation (fb) with in ${savings} savings.   ")
    purchase = savings / fb
    current_price = fb
    purchase = input ("How many shares you would like to purchase of Facebook Incorporation (fb)?  ")
    print()

elif stock == "goog":
    print   (f"{f_name} you have choosen to invest in Google LCC (goog) with ${savings} in savings.  ")
    purchase = savings / google
    current_price = google 
    purchase = input ("How many shares you would like to purchase of Google LCC (goog)  ")
    print()

elif stock == "msft":
    print   (f"{f_name} you have choosen to invest in Microsoft Corporation (msft) with ${savings} in savings.  ")
    purchase = (f'{savings / msft}')
    current_price = msft
    purchase = input ("How many shares you would like to purchase of Microsoft Corporation (msft)?  ")
    print()

else:  
     print("You didn't enter a valid stock option.")

print("Challenge 3.2.2: Perform user-specific calculations\n\n")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
#Created a varible for amount to determine number of shares client can purchase based off savings.


print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"Hello {f_name}, you have ${savings} in savings and can buy {purchase} shares of {stock} at the current price of ${current_price} per share.")

