#STRING OPERATIONS

# ----------------------------------------------------------
#Creating a String
# ----------------------------------------------------------


greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# ----------------------------------------------------------
#String Concatenation
# ----------------------------------------------------------

first_name = 'Sri' 
last_name = 'Vishnu'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Sri Vishnu

# ----------------------------------------------------------
# Checking the length of a string using len() built-in function
# ----------------------------------------------------------

print(len(first_name))  # 3
print(len(last_name))   # 4
print(len(first_name) > len(last_name)) #  False
print(len(full_name)) # 8

# ----------------------------------------------------------
#Escape Sequences in Strings
# ----------------------------------------------------------
'''
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''

print('I hope everyone is enjoying the Python Challenge.') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

'''
I hope every one is enjoying the Python Challenge.

Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)

'''
# ----------------------------------------------------------
#String formatting
# ----------------------------------------------------------

# Strings only
first_name = 'Sri'
last_name = 'Vishnu'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

# ----------------------------------------------------------
#New Style String Formatting (str.format) from Python version 3
# ----------------------------------------------------------

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
'''
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

'''
# ----------------------------------------------------------
# Strings  and numbers
# ----------------------------------------------------------

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# ----------------------------------------------------------
#Python Strings as Sequences of Characters
# ----------------------------------------------------------

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# ----------------------------------------------------------
# Accessing Characters in Strings by Index
# ----------------------------------------------------------

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

#If we want to start from right end we can use negative indexing. -1 is the last index.

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# ----------------------------------------------------------
#Slicing Python Strings
# ----------------------------------------------------------

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon

# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# ----------------------------------------------------------
#Reversing Strings
# ----------------------------------------------------------

s = "Hello World"
reversed_s = s[::-1]
print(reversed_s) 

# Output: dlroW olleH

#Another way to do
s = "Python"
reversed_s = "".join(reversed(s))
print(reversed_s)

# Output: nohtyP

# ----------------------------------------------------------
#Skipping Characters While Slicing
# ----------------------------------------------------------

language = 'Python'
pto = language[0:2:6] #
print(pto) # Ptn


# STRING METHODS PROGRAM

challenge="thirty days of python"
print(challenge.index('da', 9)) # ValueError

# rindex()
print(challenge.rindex('da')) # 7

# print(challenge.rindex('da', 9)) # ValueError
print(challenge.rindex('on', 8)) # 19

# isalnum()
print('ThirtyDaysPython'.isalnum()) # True
print('30DaysPython'.isalnum()) # True
print('thirty days of python'.isalnum()) # False

# isalpha()
print('thirty days of python'.isalpha()) # False
print('ThirtyDaysPython'.isalpha()) # True
print('123'.isalpha()) # False

# isdecimal()
print('thirty days'.isdecimal()) # False
print('123'.isdecimal()) # True
print('²'.isdecimal()) # False
print('12 3'.isdecimal()) # False


# isdigit()
print('Thirty'.isdigit()) # False
print('30'.isdigit()) # True
print('²'.isdigit()) # True


# isnumeric()
print('10'.isnumeric()) # True
print('½'.isnumeric()) # True
print('10.5'.isnumeric()) # False


# isidentifier()
print('30DaysOfPython'.isidentifier()) # False
print('thirty_days_of_python'.isidentifier()) # True

##The isidentifier() method in Python is used to check whether a given string is a valid identifier according to Python's language rules.
# A valid identifier must start with a letter (a-z, A-Z) or an underscore (_), followed by any number of letters, digits (0-9), or underscores, and must not be a Python keyword

# islower() and isupper()
print('thirty days of python'.islower()) # True
print('THIRTY DAYS OF PYTHON'.isupper()) # True


# join()
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(' '.join(web_tech)) # HTML CSS JavaScript React
print('# '.join(web_tech)) # HTML# CSS# JavaScript# React


# strip()
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # irty days of py


# replace()
print('thirty days of python'.replace('python', 'coding'))


# split()
print('thirty days of python'.split())
print('thirty, days, of, python'.split(', '))


# title()
print('thirty days of python'.title())


# swapcase()
print('thirty days of python'.swapcase())
print('Thirty Days Of Python'.swapcase())


# startswith()
print('thirty days of python'.startswith('thirty')) # True
print('30 days of python'.startswith('thirty')) # False

