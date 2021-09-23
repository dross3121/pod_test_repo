#The formula for converting between fahrenheit and \n
#celsius is to first subtract 32, then multiply by 5/9.
print ('1. Convert a temperature of 100 degrees fahrenheit to celsius.')
# Formula F - 32 * 5/9
celsius_100 = float((100-32)*5/9)
print ( str(celsius_100 )+ ' ' + 'Degrees Celsius' ) 
print ('  \n')
print ('2.Convert a temperature of 0 degrees fahrenheit to celsius.') 
# Formula F - 32 * 5/9
celsius_0 = float((0-32)*5/9)
print (  str(celsius_0) + ' ' + 'Degrees Celsius')
print ('  \n')
print ('3. Convert a temperature of 34.2 degrees fahrenheit to celsius.') 
# Formula F - 32 * 5/9
celsius_34 = float((34.2-32)*5/9)
print (  str(celsius_34) + ' ' + 'Degrees Celsius')
print ('  ')
print ('Now, can you convert back?')
print ('  \n')
print ('4. Convert a temperature of 5 degrees celsius to fahrenheit?')
# Formula C * 5/9 + 32
fahrenheit_5 = float((5*9/5)+32)
print (str(fahrenheit_5) + '  ' + 'Degrees Fahrenheit')
print ('  \n')
print ('5. What is hotter, a temperature of 30.2 degrees celsius,\n   or a temperature of 85.1 degrees fahrenheit?\n')
#Convert 30.2 degrees celsius to fahrenheit.
celsius_30 = float((30.2*9/5)+32)
print ('30.2 degrees celsius is a hotter temperature @, ')
print (  str(celsius_30) + ' ' + 'Degrees Fahrenheit.\n\n')
