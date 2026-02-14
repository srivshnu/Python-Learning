"""
HIGHER ORDER FUNCTIONS
------------------------------------------------
"""

# =============================================================
# 1) WHAT ARE HIGHER ORDER FUNCTIONS?
# =============================================================

# Any function that does at least ONE of the following is called
# a HIGHER ORDER FUNCTION:
# 1. Takes a function as an argument
# 2. Returns a function as a result

# =============================================================
# 2) FUNCTION AS A PARAMETER
# =============================================================
# Here, a function is passed INTO another function.
# This allows behavior to be decided dynamically.


def sum_numbers(nums):
    return sum(nums)


def higher_order_function(func, data): #function as parameter
    return func(data)

# Passing function WITHOUT calling it (no parentheses)
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# result = 15

# =============================================================
# 3) FUNCTION AS A RETURN VALUE
# =============================================================
# A function can RETURN another function.
# This is used when behavior must be chosen at runtime.

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return x if x >= 0 else -x

def function_factory(name):
    # Based on input, return a FUNCTION
    if name == "square":
        return square
    elif name == "cube":
        return cube
    elif name == "absolute":
        return absolute

# function_factory returns a function
f = function_factory("square")
# f now refers to square()
# f(3) → 9

# =============================================================
# 4) PYTHON CLOSURES
# =============================================================
# A closure happens when:
# - An inner function remembers variables from the outer function
# - Even after the outer function has finished execution

def add_ten():
    ten = 10  # local variable
    def add(num):
        # Inner function uses variable from outer scope
        return num + ten
    return add

# add_ten() returns the inner function          
closure = add_ten()

# closure remembers 'ten'
# closure(5) → 15
# closure(10) → 20

# =============================================================
# 5) PYTHON DECORATORS
# =============================================================
# A decorator is a function that MODIFIES another function WITHOUT changing its original code.
# Decorators are built using higher order functions.

# -----------------
# BASIC DECORATOR
# -----------------

def uppercase_decorator(function):
    # function is the original function being decorated
    def wrapper():
        # wrapper adds extra behavior
        result = function()
        return result.upper()
    return wrapper

@uppercase_decorator
# greeting is replaced by wrapper internally
def greeting():
    return "Welcome to Python"

# greeting() → 'WELCOME TO PYTHON'

# -----------------
# MULTIPLE DECORATORS
# -----------------
# Decorators execute from bottom to top

def split_string_decorator(function):
    def wrapper():
        return function().split()
    return wrapper

@split_string_decorator
@uppercase_decorator
# Execution order:
# greeting → uppercase → split
def greeting2():
    return "Welcome to Python"

# greeting2() → ['WELCOME', 'TO', 'PYTHON']

# -----------------
# DECORATOR WITH PARAMETERS
# -----------------
# Used when the original function accepts arguments


def decorator_with_parameters(function):
    def wrapper(first, last, country):
        function(first, last, country)
        print(f"I live in {country}")
    return wrapper

@decorator_with_parameters
def print_full_name(first, last, country):
    print(f"I am {first} {last}.")

# =============================================================
# 6) BUILT-IN HIGHER ORDER FUNCTIONS
# =============================================================
# Python provides built-in higher order functions
# that work with iterables.

# -----------------
# MAP FUNCTION
# -----------------
# map(function, iterable)
# Applies function to EVERY element

numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 2, numbers)
# list(squared) → [1, 4, 9, 16, 25]

# -----------------
# FILTER FUNCTION
# -----------------
# filter(function, iterable)
# Keeps elements where function returns True

evens = filter(lambda x: x % 2 == 0, numbers)
# list(evens) → [2, 4]

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
long_names = filter(lambda name: len(name) > 7, names)
# ['Asabeneh']

# -----------------
# REDUCE FUNCTION
# -----------------
# reduce(function, iterable)
# Combines all values into ONE result

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']

total = reduce(lambda x, y: int(x) + int(y), numbers_str)
# total → 15
