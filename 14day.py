"""
ERRORS & DEBUGGING IN PYTHON 
-----------------------------------------------------------
"""

# =============================================================
# 1) SyntaxError
# =============================================================
# WHAT:
# Happens when Python cannot understand the structure of your code.
# Python checks SYNTAX before running the program.
#
# WHY:
# Missing brackets, quotes, colons, wrong indentation, etc.

# ❌ Wrong (Python 3 does not allow this syntax)
# print 'hello world'

# ✔ Correct
print('hello world')


# =============================================================
# 2) NameError
# =============================================================
# WHAT:
# Raised when you try to use a variable or function that does not exist.
#
# WHY:
# - Variable not defined
# - Typo in variable name
# - Used before assignment

# ❌ Wrong
# print(age)

# ✔ Fix
age = 25
print(age)


# =============================================================
# 3) IndexError
# =============================================================
# WHAT:
# Raised when you access an index outside the valid range.
#
# WHY:
# Lists are zero-indexed: 0 to len(list)-1

numbers = [1, 2, 3, 4, 5]

# ❌ Wrong
# numbers[5]

# ✔ Correct
print(numbers[4])


# =============================================================
# 4) ModuleNotFoundError
# =============================================================
# WHAT:
# Python cannot find the module you are trying to import.
#
# WHY:
# - Typo in module name
# - Module not installed

# ❌ Wrong
# import maths

# ✔ Correct
import math


# =============================================================
# 5) AttributeError
# =============================================================
# WHAT:
# Raised when an object does not have the requested attribute or method.
#
# WHY:
# - Typo in attribute name
# - Attribute does not exist

# ❌ Wrong
# math.PI

# ✔ Correct
print(math.pi)


# =============================================================
# 6) KeyError
# =============================================================
# WHAT:
# Raised when a dictionary key does not exist.
#
# WHY:
# - Typo in key name
# - Key was never defined

user = {'name': 'SV', 'age': 250, 'country': 'IND'}

# ❌ Wrong
# user['county']

# ✔ Correct
print(user['country'])


# =============================================================
# 7) TypeError
# =============================================================
# WHAT:
# Raised when an operation is applied to incompatible data types.

# WHY:
# Python does not automatically convert between unrelated types.

# ❌ Wrong
# 4 + '3'

# ✔ Fix by converting types
print(4 + int('3'))   # 7
print(4 + float('3')) # 7.0
print(str(4) + '3')   # '43'


# =============================================================
# 8) ImportError
# =============================================================
# WHAT:
# Raised when you try to import something that does not exist
# inside a valid module.
#
# WHY:
# Function or variable name is wrong.

# ❌ Wrong
# from math import power

# ✔ Correct
from math import pow
print(pow(2, 3))


# =============================================================
# 9) ValueError
# =============================================================
# WHAT:
# Raised when a function gets the correct TYPE but an invalid VALUE.
#
# WHY:
# Conversion failed, invalid input format, etc.

# ❌ Wrong
# int('12a')

# ✔ Correct
print(int('12'))


# =============================================================
# 10) ZeroDivisionError
# =============================================================
# WHAT:
# Raised when dividing by zero.
#
# WHY:
# Division by zero is mathematically undefined.

# ❌ Wrong
# 1 / 0

# ✔ Safe check
x = 10
y = 2
if y != 0:
    print(x / y)


