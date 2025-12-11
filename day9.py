# ----------------------------------------------------------
#Conditionals
# ----------------------------------------------------------
# syntax
#if condition:
    #this part of code runs for truthy conditions
#-----------------------------------------------------------
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
#-----------------------------------------------------------
#If Else
#-----------------------------------------------------------
# syntax
#if condition:
#    this part of code runs for truthy conditions
#else:
#     this part of code runs for false conditions
#----------------------------------------------------------
#Example
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
#----------------------------------------------------------
#If Elif Else
#----------------------------------------------------------
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
#----------------------------------------------------------
#Nested Conditions
#----------------------------------------------------------
# syntax
'''
if condition:
    code
    if condition:
    code
'''
#----------------------------------------------------------
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
#----------------------------------------------------------
#The use of the conditionals same as other languages where you can use multiple logical operators in a single condition and proceed the code accordingly
#----------------------------------------------------------
