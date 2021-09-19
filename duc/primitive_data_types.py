# '''
# Strings - text/character data
# Integer - numeric, no decimal
# Float - numeric, with decimal
# Boolean - True / False

# PRIMITIVE DATA TYPES
# make up prettu much all data structures in python
# '''
# ''' LONG COMMENT '''


# # INTEGERS

# # EXAMPLE:
my_int = 4
print(my_int)

# # HOW TO IDENTIFY YOUR VARIABLE:
# # print(type(VARIABLE))

# FLOATS  
my_float = 4.0
print(my_float)
print(type(my_float))

# MATH WITH INTEGERS / FLOATS
print(my_int + my_float)
print(my_int - my_float)
print(my_int * 100)
print(my_int / 3.2987923874293874928374923749238749283749238472)

# EXPONENTS
my_num = 13**13
print(my_num)

'''
P - Parenthesis
E - Exponents
M - Multiply
D - Divide
A - Add
S - Subtract
'''

num1 = 2+2*10
num2 = (2+2)*10
print(num1, num2)

# TYPE CONVERSION FROM FLOAT TO INTEGER
# WHEN CONVERTING FROM FLOAT TO INTERGER, ANYTHING PASS THE DECIMAL WILL BE ELIMINATED. GONE. 4.999999999999999 WILL ALWAYS EQUAL 4

my_float2 = 4.68
my_int2 = int(my_float2)
print(my_int2)
print(round(my_float2))

print(float(9))

print(round(my_float2, 5))


# NOTES: STRINGS
"""
What's important about STRINGS?

QUOTES
"" or ''

Strings can have spaces in them




"""

my_string = 'hello world!'
print(my_string)
print(type(my_string))

my_space_case = '           '
print(my_space_case)

# WITH ESCAPE CHARACTERS
# \ - Break Long Sentence
# \n - New Line w/Sentence
# \t - Indent

paragraph = 'This big walnut board is already ideally designed for your best cutting and carving, \
\n\twith a big trough for catching all those runoff juices. \
\nSo why not make it even more your own with a monogram? \
\nThat’s right—you can customize this one with a big letter \
\n\t\t(in our favorite Gotham font!) representing your name or a giftee’s. \
\nIt’s a true hardwood statement.'

print(paragraph)

# f-strings (formatted settings) - a way to insert code (a VARIABLE) into a string

profit = 120

my_f_string = f"The profit today is ${profit*100}"
print(my_f_string)

# MATH WITH STRINGS??
# + WITH STRINGS CONCATENATES THEM: SMOOSHES THEM TOGETHER "APPLECHERRY"

string_plus = 'apples' + 'cherry'
print(string_plus)

print('apples'*1000)

print(str(267.99))
print(type(str(267.99)))

# CONVERTING STRINGS TO NUMERIC DATA?

print(int('5'))
print(float('5.0'))
print(float('8.1'))

# UPPER AND LOWER CASE

my_name = 't40 banh mi'
print(my_name.upper())

my_middle_name = 'HuGrYRoAmER'
print(my_middle_name.lower())

# BOOLEANS VARIABLES
# TRUE == 1
# FALSE == 0

my_bool = True
print(my_bool)
print(type(my_bool))

print(my_bool+10)
print(False+1)

print(int(my_bool))
print(float(my_bool))
print(float(False))

print(str(False))
print(type(str(False)))
