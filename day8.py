# ----------------------------------------------------------
#Dictionaries
# ----------------------------------------------------------

#A dictionary is a collection of unordered, mutable paired (key: value) data type.It cannot be indexed. 


# ----------------------------------------------------------
#Creating a Dictionary
# ----------------------------------------------------------
empty_dict = {}

# Dictionary with data values

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person ={
    'first_name':'Sri',
    'last_name':'Vishnu',
    'age':250,
    'country':'Finland',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':
    {
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# ----------------------------------------------------------
#Dictionary Length
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

person = {
    'first_name':'Sri',
    'last_name':'Vishnu',
    'age':250,
    'country':'India',
    'is_married':False,

    'address':{
        'street':'SS street',
        'zipcode':'5502210'
    }
    }
print(len(person)) # 7

# ----------------------------------------------------------
#Accessing Dictionary Items
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

person = {
    'first_name':'Sri',
    'last_name':'Vishnu',
    'age':250,
    'country':'India',
    'is_married':False,
    'address':{
        'street':['SS street', 'TT street'],
        'zipcode':'5502210'
    }}
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['address']['street'][1]) # TT street
#print(person[''])       # Error

#Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

print(person.get('address'))
print(person.get('country'))    # Finland
print(person.get('city'))   # None

# ----------------------------------------------------------
#Adding Items to a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct)

person['city']='gn'
print(person)

# ----------------------------------------------------------
#Modifying Items in a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

person['age']=44
print(person)

# ----------------------------------------------------------
#Checking Keys in a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

print('SS street' in person['address']['street'])
'''
Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name

'''
# ----------------------------------------------------------
#Removing Key and Value Pairs from a Dictionary
# ----------------------------------------------------------
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
# ----------------------------------------------------------
person = {
    'first_name':'Sri',
    'last_name':'Vishnu',
    'age':20,
    'country':'India',
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Sam street',
        'zipcode':'6544511'
    }}
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# ----------------------------------------------------------
#Changing Dictionary to a List of Items
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# ----------------------------------------------------------
#Clearing a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# ----------------------------------------------------------
#Deleting a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# ----------------------------------------------------------
#Copy a Dictionary
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# ----------------------------------------------------------
#Getting Dictionary Keys as a List
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# ----------------------------------------------------------
#Getting Dictionary Values as a List
# ----------------------------------------------------------

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])