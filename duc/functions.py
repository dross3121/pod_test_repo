# ===========================================FUNCTIONS LECTURE WITH DESHAWN=============================================================
# FUNCTION - A BLOCK OF CODE THAT RUNS TO COMPLETE A SPECIFIC SET OF TASK OR PROCEDURES

# ==================================================CREATING / USING FUNCTIONS==========================================================

# def say_hello():
#    #block of code
#    print('Hello World')

# say_hello()
# say_hello()

# if 1 < 2 :
#     say_hello()
# else: 
#     print('not true')
# WHAT DO YOU MEAN BY YOU WANT THE CODE TO DRAW IN FUNCTION?
# WHY DID THE FUNCTION PRINT OUT 3 HELLO WORLDS INSTEAD OF JUST 2?
# ======================================================================================================================================
# Hello Ash
# Good Morning
# And Good Night
# Hello Paul
# Good Morning
# And Good Night

# def say_hello_ash():                #LONGER WAY TO PRINT
#     print('Hello Ash')
#     print('Good Morning')
#     print('And Good Night')

# def say_hello_paul():
#     print('Hello Paul')
#     print('Good Morning')
#     print('And Good Night')

# def say_morning_night():            #SIMPLER AND FASTER WAY TO PRINT
#     print('Good Morning')
#     print('And Good Night')

# def say_hello_ash():               
#     print('Hello Ash')
#     say_morning_night()

# def say_hello_paul():
#     print('Hello Paul')
#     say_morning_night()

# say_hello_ash()
# say_hello_paul()

# ==========================================================PARAMETERS==================================================================
# PARAMETERS - IS A VARIABLE OR PLACEHOLDER ( YOU CAN NAME IT WHATEVER YOU WANT) / TO HOLD A VALUE OR REFERENCE TO A VALUE THAT WE ADD TO IT

# def say_hello(name):                #EVEN FASTER WAY TO PRINT
#     print(f'Hello {name}')
#     print('Good Morning')
#     print('And Good Night')

# say_hello('Ash')
# say_hello('Paul')

# ===========================================PARAMETERS / FUNCTION TO INTEGERS==========================================================

def times_two(num):
    print(num*2)

# times_two(3)
# times_two(599)

# ==============================================PARAMETERS / LIST TO FUNCTION==========================================================
number = [0, 1, 99, 13, 24]

def first_num(nums):
    print(nums[0])

first_num(number)


