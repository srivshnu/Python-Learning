# FUNCTIONS 
# --------------------------------------------------

# 1) Basic Function (no input)
# A function without parameters always does the same thing.
# Useful when you just want to run fixed steps.
# --------------------------------------------------
# ------------------
# syntax:
# def function_name():
#     statements

def greet():
    print("Hello!")


# 2) Function With Parameter

# Parameters allow the function to receive input.
# Whatever you pass inside () becomes available inside the function.

# --------------------------
# def function_name(param):
#     statements

def greet_person(name):
    print("Hello", name)


# 3) Function Returning a Value
# A function can *return* a result instead of printing it.
# Returning is important because other parts of your program can
# store the value, modify it, or pass it to other functions.
# --------------------------------------------------

# def function_name():
#     return value

def add(a, b):
    return a + b


# 4) Function With Default Parameter

# Default parameters allow you to provide an optional value.
# If the caller does not supply that argument, Python uses the default.
# --------------------------------------------------

# def func(a, b=default):
#     ...

def power(base, exp=2):
    return base ** exp


# 5) *args (variable number of positional arguments)
# Lets your function accept ANY number of values.
# Inside the function, args behaves like a tuple.
# Useful when you don’t know how many inputs you will receive.
# -------------------------------------------------- (any number of positional arguments)

# def func(*args):
#     ...

def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total


# 6) **kwargs (variable keyword arguments)

# Allows your function to accept any number of named arguments.
# Inside, kwargs is a dictionary.
# Useful for flexible configuration or optional parameters.
# -------------------------------------------------- (any number of keyword arguments)
# ---------------------------------------------
# def func(**kwargs):
#     ...

def describe(**info):
    return info


# 7) Passing a Function as Argument

# In Python, functions are "first-class objects" — you can store them,
# pass them to other functions, or return them.
# This is the foundation for callbacks, decorators, and functional programming.
# --------------------------------------------------
# ---------------------------------
# def func(f, x): return f(x)

def square(n):
    return n * n

def apply(func, value):
    return func(value)


# 8) Returning Multiple Values
# Python lets you return several values at once, packaged as a tuple.
# The caller can unpack them easily. This keeps function APIs clean.
# --------------------------------------------------
# ----------------------------
# return a, b

def min_max(numbers):
    return min(numbers), max(numbers)


# 9) Lambda (anonymous function)
# A lambda is a tiny function written in one line.
# Useful when you need a quick function without defining a full def block.
# Often used with map(), filter(), sort(), etc.
# -------------------------------------------------- (short anonymous function)
# lambda arguments: expression

time2 = lambda x: x * 2


# 10) Simple Generator (yield)
# Generators produce values one at a time using `yield`.
# They are memory-efficient because they don’t store the whole result.
# Ideal for large data streams or long sequences.
# -------------------------------------------------- (yield)
# def func():
#     yield value

def first_n(n):
    for i in range(n):
        yield i


# 11) Decorator (wrap another function)
# A decorator is a function that modifies the behavior of another function.
# Used for logging, validation, authentication, caching, etc.
# They rely on Python’s ability to treat functions as objects.
# -------------------------------------------------- (Simplest Form)
# -----------------------------
def debug(fn):
    def wrapper():
        print("Running", fn.__name__)
        return fn()
    return wrapper

@debug
def hello():
    return "hi"


# END OF BASIC SUMMARY
