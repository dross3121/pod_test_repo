#===============================================DICTIONARY LECTURE NOTES with ASH ======================================================
# blank_dict = {}
# print(blank_dict)
# print(type(blank_dict))

#==============================================CREATED A DICTIONARY, ADDED KEY-VALUE PAIRS==============================================
# user_account = {'username': 'hungryroamer', 'balance': 270.56}
#                 # KEY           VALUE         VALUE
# print(user_account)
#=========================================================ACCESS VALUE BY USING KEY=====================================================
# print(user_account['username'])
# print(user_account['balance'])

# username = user_account['username']
# print(username)

# user_account = {
#     'username': 'pbloom',
#     'balance': 270.56,
#     'deposits': [100, 20, 45.8],
#     'withdrawals': [-43.7, -10, -23],
#     'email_notifications': True
# }

#========================================================ADDING KEY / VALUE PAIRS=======================================================
# user_account['last_transaction_date'] = '9/25/21'
# # DICTIONARY        KEY                   VALUE   
# print(user_account)

#========================================================UPDATE KEY / VALUE PAIRS=======================================================
# user_account['balance'] = 240.54
# print(user_account)
# print(user_account['deposits'][0])
# #           OR THIS WAY
# deposits = user_account['deposits']
# print(deposits[0])
# # APPEND = TO ADD
# user_account['deposits'].append(30)
# print(user_account)

#==========================================================REMOVING KEY / VALUE PAIRS===================================================
# user_account.pop('email_notifications')
# print(user_account)

#=======================================================================================================================================

a = [] # EMPTY LIST
b = {} # EMPTY DICTIONARY
#============================================================ADDING ITEMS TO LIST=======================================================
a.append('apples')
a.append('bananas')
a.append('mangoes')

print(a)
print(a[2]) #ACCESSING MANGOES

#====================================================ADDING KEY / VALUE PAIRS TO DICTIONARY=============================================
b['lastname'] = 'ta'
b['firstname'] = 'duc'
b['middlename'] = 'hong'

print(b)
print(b['lastname']) #ACCESSING LASTNAME