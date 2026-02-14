#----------------------------------------------------------
#Loops
#----------------------------------------------------------

  # syntax
#while condition:
    #code goes here

#----------------------------------------------------------
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

#----------------------------------------------------------
#Break 
#----------------------------------------------------------

# syntax
'''
while condition:
    code goes here
    if another_condition:
        break
        
'''

#----------------------------------------------------------
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break    #loop stops at count==3 and continues with the next steps in the program

#----------------------------------------------------------
#Continue
#----------------------------------------------------------

'''
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
'''

#----------------------------------------------------------
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1   #The above while loop only prints 0, 1, 2 and 4 (skips 3).

#----------------------------------------------------------
#For Loop
#----------------------------------------------------------

# syntax
#for iterator in list:
#    code goes here

'''
syntax
for iterator in string:
    code goes here

# syntax
for iterator in tpl:
    code goes here

# syntax
for iterator in dct:
    code goes here

# syntax
for iterator in st:
    code goes here
'''
#----------------------------------------------------------
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)      # the numbers will be printed line by line, from 0 to 5
    
language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
#----------------------------------------------------------
#Break and continue work the same in for loop too.
#----------------------------------------------------------

#----------------------------------------------------------
#The Range Function
#----------------------------------------------------------
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# syntax
for iterator in range(start, end, step):
    i=i+1

#----------------------------------------------------------
#Nested for loops
#----------------------------------------------------------

# syntax
for x in y:
    for t in x:
        print(t)

#----------------------------------------------------------
#Pass
#----------------------------------------------------------

#Used for skipping loop execution

#syntax
for number in range(6):
    pass

