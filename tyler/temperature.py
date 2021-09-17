# The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

# Convert a temperature of 100 degrees fahrenheit to celsius
# Save this to a variable called celsius_100, and use print() to print out the value
# Is the resulting temperature you get an integer or float? How do you know?
# Convert a temperature of 0 degrees fahrenheit to celsius
# Save this to a variable called celsius_0, and use print() to print out the value
# Convert a temperature of 34.2 degrees fahrenheit to celsius
# Do this one all in one print statement without saving any variables

# 1. Converting 100 degrees farenheit to celsius, assigning to variable "celsius_100" then showing the type for the variable "celsius_100", printing result
celsius_100 = 100 - 32 * 0.556
print(celsius_100)
print(type(celsius_100))
# 2. Converting 0 degrees farenheit to celsius, assigning to variable "celsius_0", printing result
celsius_0 = 0 - 32 * 0.556
print(celsius_0)
# 3. Converting 34.2 degrees farenheit to celsius, printing result
print(34.2 - 32 * 0.556)
# 4. Converting 5 degrees celsius to farenheit, printing result
print(5 / 0.556 + 32)
# 5. Converting 30.2 degrees celsius to farenheit to see if its hotter than 85.1 degrees farenheit
print(30.2 / 0.556 + 32)
print('30.2 degrees celsius is hotter than 85.1 degrees farenheit')