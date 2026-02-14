# Introduction
# Day 1 - 30DaysOfPython Challenge

# Python is dynamically typed:
# Variable types can be changed at runtime
x = 10     # int
x = "ten"  # now string

# Valid variable names:
my_name = "Vishnu"
my_age = 18
pi_value = 3.14

# Invalid:
# 1name = "x"
# my-name = "x"
# class = 5

'''
| Operator | Name             | Example | Meaning            |
|----------|------------------|---------|--------------------|
| +        | Addition         | a + b   | Sum                |
| -        | Subtraction      | a - b   | Difference         |
| *        | Multiplication   | a * b   | Product            |
| /        | Division         | a / b   | Float division     |
| //       | Floor Division   | a // b  | Integer result     |
| %        | Modulus          | a % b   | Remainder          |
| **       | Power            | a ** b  | Exponential        |

'''
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                             # Int
print(type(3.14))                           # Float
print(type(1 + 3j))                         # Complex
print(type('Sri Vishnu'))                   # String
print(type([1, 2, 3]))                      # List
print(type({'name':'Sri Vishnu','age':18})) # Dictionary
print(type({9.8, 3.14, 2.7}))               # Set
print(type((9.8, 3.14, 2.7)))               # Tuple
print(type(3 == 3))                         # Bool
print(type(3 >= 3))                         # Bool

'''
| Type        | Ordered | Mutable | Duplicate | Example           |
|-------------|---------|---------|-----------|-------------------|
| List        | Yes     | Yes     | Yes       | [1,2,3]           |
| Tuple       | Yes     | No      | Yes       | (1,2,3)           |
| Set         | No      | Yes     | No        | {1,2,3}           |
| Dictionary  | Yes     | Yes     | Keys No   | {'a':1,'b':2}     |
| Boolean     | Yes     | No      | No        | True / False      |

'''
