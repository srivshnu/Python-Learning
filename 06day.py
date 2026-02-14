#TUPLES

# A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, (). 

# ----------------------------------------------------------
# Creating a Tuple
# ----------------------------------------------------------

# Creating an empty tuple
empty_tuple = () # syntax
# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# ----------------------------------------------------------
# Tuple length
# ----------------------------------------------------------

# We use the len() method to get the length of a tuple.
tpl = ('item1', 'item2', 'item3')
print(len(tpl)) # 3 

# ----------------------------------------------------------
# Accessing Tuple Items
# ----------------------------------------------------------

# Positive Indexing
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing
# Negative indexing means beginning from the end, -1 refers to the last item.
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# ----------------------------------------------------------
# Slicing tuples
# ----------------------------------------------------------

# Range of Positive Indexes
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]          # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits = fruits[0:]     # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Range of Negative Indexes
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]           # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]      # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# ----------------------------------------------------------
# Changing Tuples to Lists
# ----------------------------------------------------------

# Tuple is immutable if we want to modify a tuple we should change it to a list.
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# ----------------------------------------------------------
# Checking an Item in a Tuple
# ----------------------------------------------------------

# We can check if an item exists or not in a tuple using in, it returns a boolean.
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl) # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# ----------------------------------------------------------
# Joining Tuples
# ----------------------------------------------------------

# We can join two or more tuples using + operator
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# ----------------------------------------------------------
# Deleting Tuples
# ----------------------------------------------------------

# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

