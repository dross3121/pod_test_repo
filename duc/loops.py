# ==============================================LOOPS LECTURE NOTES w/ CLAIRE===========================================================
# LOOP = APPLY ALL / FASTER AND EASIER WAY TO PRINT COMPLEX CODES
# for x in y
# for (each) person in (the list of) people
#        x                  y
# y = list of people
# x = each person

# for (each stock) in the lsit of stocks
#           x                   y

# for (each random thing) in the list of random things
#             x                         y

numbers = [12, 8, 41]

# INSTEAD OF PRINTING EACH ONE LIKE THIS:
# print(12)
# print(8)
# print(41)
# # OR
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# USE A "FOR LOOP" FUNCTION LIKE THIS INSTEAD:
 
# for number in numbers:
# #      x         y
#     print(number)

# =======================================================FOR LOOP SYNTAX================================================================

# FOR LOOP - RUNS A SET NUMBER OF TIMES 
'''for DUCK in numbers: #YOU CAN USE ANYTHING IN DUCK FOR INTERATING THE LOOP JUST AS LONG AS IT IS THE SAME IN THE PRINT
    print(DUCK)

    print("Hello World") #WILL ALWAYS PRINT BECAUSE IT'S INDENTED AND STILL INSIDE LOOP

print("hi, computer")# PRINT ONCE SINCE IT IS NOT INDENTED BECAUSE IT'S OUTSIDE THE LOOP
'''

# lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']
# upper_list = []

# for i in lower_list:
#     upper_list.append(i.upper())        #USING SYNTAX TO CHANGE LOWER CASE TO UPPER CASE

# print(upper_list)
# ==========================================LOOPING THROUGH CHARACTERS IN A STRING======================================================
# my_string = 'ice cream'
# vowels = ['a', 'e', 'i', 'o', 'u']
# for letter in my_string:
#     if letter in vowels: 
#          print(f'{letter} is a vowel')
#     else:
#         print(f'{letter} is not a vowel')

# ========================================================A WHILE LOOP==================================================================
# A WHILE LOOP - KEEPS REPEATING UNTIL A CERTAIN LOGICAL CONDITION IS MET
count = 0
while (count < 5):
    print(count)
    count = count + 1
print ('done')

# BEWARE IF CREATING AN INCORRECT WHILE LOOP, IT CAN RUN FOREVER!!!!!!! while (count >= 0) NEVER RUN THIS CODE!

