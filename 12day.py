# -------------------------------------------------------------
# 1) What is a Module?
# -------------------------------------------------------------
# A module is simply a .py file containing variables or functions.
# You can import modules to reuse code instead of rewriting again in your program file.


#print(help('modules'))  #prints all in-built modules
#print(help('math'))  #prints in-built functions of the module


# -------------------------------------------------------------
# 1) What is a Module?
# -------------------------------------------------------------
# A module is simply a .py file containing variables or functions.
# You import modules to reuse code instead of rewriting it.

# -------------------------------------------------------------
# 2) Creating a Module (mymodule.py)
# -------------------------------------------------------------
# def generate_full_name(firstname, lastname):
#     return firstname + " " + lastname
#Create a file with this functions

# -------------------------------------------------------------
# 3) Importing the module
# -------------------------------------------------------------
# import mymodule
# print(mymodule.generate_full_name("A", "B"))

#Example
import mymodule
mymodule.printMathFunctionsAndConstants()

# -------------------------------------------------------------
# 4) Importing only specific items
# -------------------------------------------------------------
# from mymodule import generate_full_name, sum_two_nums, person, gravity
# generate_full_name("A", "B")

#Example
from mymodule import x,y
print(sum(x,y))

# -------------------------------------------------------------
# 5) Renaming while importing
# -------------------------------------------------------------
# from mymodule import generate_full_name as fullname
# fullname("A", "B")

from mymodule import printMathFunctionsAndConstants as pmmfc, x as q, y as u
pmmfc()
print(q/u)

# -------------------------------------------------------------
# 6) Built‑in Modules
# -------------------------------------------------------------

# --- OS MODULE ---

import os

#Using python os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# --- SYS MODULE ---
#The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2

print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

# --- STATISTICS MODULE ---
# from statistics import mean, median, mode, stdev
# ages = [20,20,4,24,25,22,26,20,23,22,26]
# mean(ages)
# median(ages)
# mode(ages)
# stdev(ages)

# --- MATH MODULE ---
# import math
# math.pi
# math.sqrt(2)
# math.pow(2,3)
# math.floor(9.81)
# math.ceil(9.81)
# math.log10(100)

# Import specific functions:
# from math import pi, sqrt, pow
# pi
# sqrt(2)

# Import ALL functions from a particular module:
# from math import *

# Renaming imported functions:
# from math import pi as PI
# PI

# --- STRING MODULE ---
# import string
# string.ascii_letters
# string.digits
# string.punctuation

# --- RANDOM MODULE ---
# from random import random, randint
# random()      # float between 0 and 1
# randint(5,20) # random integer between 5 and 20 inclusive
