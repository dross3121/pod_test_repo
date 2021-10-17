 # The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?
# Convert a temperature of 100 degrees fahrenheit to celsius
# Save this to a variable called celsius_100, and use print() to print out the value
# Is the resulting temperature you get an integer or float? How do you know?
# Convert a temperature of 0 degrees fahrenheit to celsius
# Save this to a variable called celsius_0, and use print() to print out the value
# Convert a temperature of 34.2 degrees fahrenheit to celsius
# Do this one all in one print statement without saving any variables

# 1
celsius_100 = 100-32*.556
print(celsius_100)
print(type(celsius_100))
# 2
celsius_0 = 0-32*.556
# 3
print(34.2-32*.556)
# 4
print(5/.556+32)
# 5
print(30.2/.556+32)
print('30.2 degrees celsius is hotter than 85.1 degrees farenheit')

# Make changes