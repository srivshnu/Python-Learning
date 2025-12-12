# =============================================================
#List Comprehension
# -------------------------------------------------------------
# Example 1: Convert string to list of characters
# -------------------------------------------------------------

language = "Python"
chars = [c for c in language]

# -------------------------------------------------------------
# Example 2: Generate numbers 0 to 10
# -------------------------------------------------------------

numbers = [i for i in range(11)]

# Squares
squares = [i * i for i in range(11)]

# Tuples (number, square)
pairs = [(i, i * i) for i in range(11)]

# -------------------------------------------------------------
# Example 3: Filtering with conditions
# -------------------------------------------------------------

evens = [i for i in range(21) if i % 2 == 0]
odds = [i for i in range(21) if i % 2 != 0]

prime=[j for j in range(2,100) if all(j%d!=0 for d in range(2,int(j/2)+1))]
comp= [j for j in range(4,100) if (j not in prime)] 

nums = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
pos_even = [i for i in nums if i % 2 == 0 and i > 0]


# -------------------------------------------------------------
# Example 4: Flatten a 2D list
# -------------------------------------------------------------

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in list_of_lists for num in row]

# =============================================================
# 2) LAMBDA FUNCTIONS
# =============================================================
# A lambda is a tiny anonymous function.
# It has no name and contains only ONE expression.

# SYNTAX:
# lambda parameters: expression

# -------------------------------------------------------------
# Example 1: Convert a normal function to lambda
# -------------------------------------------------------------
def add_two(a, b):
    return a + b

add_two_lambda = lambda a, b: a + b

# -------------------------------------------------------------
# Example 2: Self-invoking lambda
# -------------------------------------------------------------
# (lambda a, b: a + b)(2, 3)

# -------------------------------------------------------------
# Example 3: Simple lambda expressions
# -------------------------------------------------------------
square = lambda x: x ** 2
cube = lambda x: x ** 3
mix = lambda a, b, c: a**2 - 3*b + 4*c

# -------------------------------------------------------------
# Example 4: Lambda inside another function (closure)
# -------------------------------------------------------------
def power(x):
    return lambda n: x ** n

# power(2)(3) → 8
# power(2)(5) → 32