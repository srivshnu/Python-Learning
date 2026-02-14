# PYTHON BUILT-IN FUNCTIONS WITH EXAMPLES

# ----------------------------------------------------------
# 1. print()  -> Display output to the screen
# ----------------------------------------------------------
print("Hello, World!")
print("Sum =", 10 + 20)


# ----------------------------------------------------------
# 2. input()  -> Takes user input as STRING
# ----------------------------------------------------------
# name = input("Enter your name: ")
# print("Welcome", name)
# (Commented to avoid blocking execution)


# ----------------------------------------------------------
# 3. type()  -> Shows data type of a variable/value
# ----------------------------------------------------------
a = 10
b = 3.14
c = "Python"
print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
print(type(c))   # <class 'str'>


# ----------------------------------------------------------
# 4. len()  -> Returns length of an iterable
# ----------------------------------------------------------
print(len("python"))        # 6
print(len([1, 2, 3, 4]))    # 4


# ----------------------------------------------------------
# 5. int(), float(), str()  -> Type conversion
# ----------------------------------------------------------
print(int(5.99))      # 5
print(float(10))      # 10.0
print(str(123))       # "123"


# ----------------------------------------------------------
# 6. list(), tuple(), set(), dict()  -> Create data structures
# ----------------------------------------------------------
print(list("ABC"))                     # ['A','B','C']
print(tuple([1, 2, 3]))                # (1,2,3)
print(set([1, 2, 2, 3]))               # {1,2,3}
print(dict(name="Vishnu", age=18))     # {'name': 'Vishnu', 'age': 18}


# ----------------------------------------------------------
# 7. abs()  -> Absolute value
# ----------------------------------------------------------
print(abs(-10))   # 10


# ----------------------------------------------------------
# 8. min(), max(), sum()  -> Mathematical operations on iterables
# ----------------------------------------------------------
nums = [5, 2, 9, 1]
print(min(nums))   # 1
print(max(nums))   # 9
print(sum(nums))   # 17


# ----------------------------------------------------------
# 9. round()  -> Round numbers
# ----------------------------------------------------------
print(round(3.14159, 2))   # 3.14


# ----------------------------------------------------------
# 10. pow()  -> Same as ** (exponent)
# ----------------------------------------------------------
print(pow(2, 3))   # 8  (2 ** 3)


# ----------------------------------------------------------
# 11. range()  -> Generate a sequence of numbers
# ----------------------------------------------------------
for i in range(1, 5):
    print("range ->", i)    


# ----------------------------------------------------------
# 12. enumerate()  -> Gives index + value
# ----------------------------------------------------------
fruits = ["apple", "banana", "kiwi"]
for index, value in enumerate(fruits):
    print("Index:", index, "Fruit:", value)


# ----------------------------------------------------------
# 13. zip()  -> Combine multiple iterables
# ----------------------------------------------------------
names = ["Vishnu", "Rahul", "Sam"]
scores = [90, 85, 88]

for n, s in zip(names, scores):
    print(n, "->", s)


# ----------------------------------------------------------
# 14. sorted()  -> Return a new sorted list
# ----------------------------------------------------------
print(sorted([3, 1, 4, 2]))         # [1,2,3,4]
print(sorted("python"))             # ['h','n','o','p','t','y']


# ----------------------------------------------------------
# 15. reversed()  -> Reverse an iterable
# ----------------------------------------------------------
print(list(reversed([1, 2, 3])))   # [3,2,1]


# ----------------------------------------------------------
# 16. id()  -> Unique object identifier
# ----------------------------------------------------------
x = 100
print("ID of x:", id(x))


# ----------------------------------------------------------
# 17. dir()  -> Shows available methods for an object
# ----------------------------------------------------------
print(dir("hello"))  # List of string methods


# ----------------------------------------------------------
# 18. help()  -> Documentation for functions/modules
# ----------------------------------------------------------
# help(print)   # Uncomment to see detailed help in console


# ----------------------------------------------------------
# 19. isinstance()  -> Check variable type
# ----------------------------------------------------------
print(isinstance(10, int))        # True
print(isinstance("abc", float))   # False


# ----------------------------------------------------------
# 20. any() & all()  -> Logical checks on iterables
# ----------------------------------------------------------
vals = [True, False, True]
print(any(vals))   # True  (at least one True)
print(all(vals))   # False (not all are True)


# ----------------------------------------------------------
# 21. map()  -> Apply function to each element
# ----------------------------------------------------------
def square(n):
    return n * n

print(list(map(square, [1, 2, 3])))   # [1,4,9]


# ----------------------------------------------------------
# 22. filter()  -> Keep items where function returns True
# ----------------------------------------------------------
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))
# Output: [2, 4, 6]
# Only even numbers are kept since is_even() returns True for even values


# ----------------------------------------------------------
# 23. ord()  -> Get ASCII/Unicode value of a character
#     chr() -> Convert number back to character
# ----------------------------------------------------------
print(ord('A'))   # 65
print(chr(90))    # 'Z'


# ----------------------------------------------------------
# 24. bin(), oct(), hex()  -> Number base conversions
# ----------------------------------------------------------
print(bin(10))   # '0b1010'
print(oct(10))   # '0o12'
print(hex(10))   # '0xa'


# ----------------------------------------------------------
# 25. getattr(), setattr(), hasattr()  -> Work with attributes dynamically
# ----------------------------------------------------------
class Student:
    def __init__(self):
        self.name = "Vishnu"

stu = Student()

print(hasattr(stu, "name"))          # True
print(getattr(stu, "name"))          # 'Vishnu'

setattr(stu, "age", 18)              # Adds stu.age dynamically
print(stu.age)                       # 18


# ----------------------------------------------------------
# 26. bytes(), bytearray()  -> For binary data
# ----------------------------------------------------------
b = bytes("ABC", "utf-8")
ba = bytearray(b)

ba[0] = 90    # Change 'A' (65) to 'Z' (90)

print(b)      # b'ABC'
print(ba)     # bytearray(b'ZBC')


# ----------------------------------------------------------
# 27. repr()  -> Developer-friendly string representation
# ----------------------------------------------------------
print(repr("Hello\nWorld"))
# Output: 'Hello\nWorld'
# Shows escape sequences clearly


# ----------------------------------------------------------
# 28. open()  -> File Handling
# ----------------------------------------------------------
# Writing to a file
with open("sample.txt", "w") as f:
    f.write("This is a demo file.")

# Reading from a file
with open("sample.txt", "r") as f:
    print(f.read())
# Output: This is a demo file.


# ----------------------------------------------------------
# 29. eval()  -> Evaluate string as Python expression (⚠ Dangerous)
# ----------------------------------------------------------
expr = "5 + 10"
print(eval(expr))   # 15


# ----------------------------------------------------------
# 30. exec()  -> Execute Python code dynamically
# ----------------------------------------------------------
code = """
for i in range(3):
    print("Exec ->", i)
"""
exec(code)

