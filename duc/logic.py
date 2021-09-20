# LOGICAL EXPRESSIONS - are statements that compute True or False
# 1 > 0 computes True
# 10 < 5 computes False

# a = 2 + 2
# b = 5 

# print(a == b)

# COMPARISION OPERTATOR :~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = 0
# b = 1
# c = 1
# # a is equal to b
# print(a == b)
# # a is not equal b
# print(a !=b)
# # a is greater than b
# print(a > b)
# # a is less than b
# print(a < b)
# # b is greater than or equal to c
# print(b >=c)
# # b is less than or equal to c
# print(b<=c)

# print(True == 1)
# print(False == 0)
# print(True == 1.0)
# print(False < 1)
# print(False > 0)


# a = 'cat'
# b = 'cat'
# c = 'CAT'
# print(a == b)
# print(a == c)
# print(a > c)

# LOGICAL OPERATORS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DEFINITION : helps build more complex logical expressions so we're not limited to single comparisons like "a is greater than b" and "b is greater than c" could essentially be all combined
# 7 LOGICAL OPERATORS

# 1. or - at least one of the comparisons MUST be True
# print(2 < 3 or 4 < 3) # the first comparison is True
# print(2 > 3 or 4 > 3) # the second comparison is True
# print(2 > 3 or 4 < 3) # neither are True
# print(2 < 3 or 4 > 3) # both are True

# # and - all the comparisons have to be True
# print(2 < 3 and 4 < 3)
# print(2 > 3 and 4 > 3)
# print(2 > 3 and 4 < 3) 
# print(2 < 3 and 4 > 3)

# print(True and False)
# print(False and True)
# print(False and False)
# print(True and True)

# not - reverse Boolen value by a logical expression
# print(not 2 < 3)
# print(not True)
# print(not 4 < 3)

# a = 1
# b = 10
# print( a < 10 and b > 10)

# CONDITIONAL STATEMENTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DEFINITION - Can make decisions in python code

# a = 2
# if a > 3:
#     print('Greater than 3!') # THIS EXAMPLE IS AN if STATEMENT
# else:
#     print('less than or equal to 3!')
# a = 4
# b = 2
# if b < 0:
#     print('a negative number')
#     print(b)
# elif b > 0:
#     if a  > 3:
#         print('greater than 3!')
#     print('a positive number')
# elif b == 0:
#     print('neither, its zero!')
# else:
#     print('well, nothing worked!')

# A PRACTICAL EXAMPLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# answer = input('Do you want to hear a joke? (press y/n)')
# # code responds accordingly
# if answer == "y":
#     print("I'm against picketing, but I don't know how to show it.")
#     # Mitch Hedberg (RIP)
# elif answer =="n":
#     print("Your Lost!")
# else:
#     print("I don't understand.")

# LOGIC LECTURE NOTES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a='cat'
# b='dog'
# print(a==b)
# COMPARISON OPERATORS:
# <=, >=, ==, !=, <, >

# or will always evaluate as a BOOLEAN
# a=3
# b=4
# c=9

# print(a<b and not b>c) 

# print(a<b or c>b) #in an or statment, if one side evaluates 

# and
# print (a==b and c>b)

# not
# print(not 1>2)

# my_wallet = 5
# friend_wallet = 100
# bagel_price = 7

# if my_wallet>=bagel_price:
#     print("Buying Bagel")
# if friend_wallet>=bagel_price:
#     print("Beg friend to buy bagel")
# elif friend_wallet+my_wallet>=bagel_price:
#     if(bagel_price>6):
#         print("Complain to friend")
# else:
#     print("Complain about New York Prices")

answer=input("Do you want to eat a bagel(press y/n)")
assert(answer=='y')

# if answer == 'y':
#     print("Here you go")
# elif answer == 'n':
#     print("No bueno for you")
# else:
#     print("not a valid character!")

