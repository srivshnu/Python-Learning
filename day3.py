# PYTHON OPERATERS WITH EXAMPLES


#ASSIGNMENT OPERATORS
# ----------------------------------------------------------
# 1. =   (Assignment)
# ----------------------------------------------------------
x = 5    # assigns value 5 to x
print("=  ->", x)   # 5


# ----------------------------------------------------------
# 2. +=   (Add and assign)
# x += 3  means  x = x + 3
# ----------------------------------------------------------
x = 5
x += 3   # x = 5 + 3
print("+= ->", x)   # 8


# ----------------------------------------------------------
# 3. -=   (Subtract and assign)
# x -= 3  means  x = x - 3
# ----------------------------------------------------------
x = 5
x -= 3
print("-= ->", x)   # 2


# ----------------------------------------------------------
# 4. *=   (Multiply and assign)
# x *= 3  means  x = x * 3
# ----------------------------------------------------------
x = 5
x *= 3
print("*= ->", x)   # 15


# ----------------------------------------------------------
# 5. /=   (Divide and assign → float)
# x /= 3  means  x = x / 3
# ----------------------------------------------------------
x = 15
x /= 3
print("/= ->", x)   # 5.0


# ----------------------------------------------------------
# 6. %=   (Modulus and assign)
# x %= 3  means  x = x % 3
# ----------------------------------------------------------
x = 10
x %= 3
print("%= ->", x)   # 1


# ----------------------------------------------------------
# 7. //=   (Floor divide and assign)
# x //= 3  means  x = x // 3
# ----------------------------------------------------------
x = 10
x //= 3
print("//= ->", x)  # 3


# ----------------------------------------------------------
# 8. **=   (Power and assign)
# x **= 3  means  x = x ** 3
# ----------------------------------------------------------
x = 2
x **= 3
print("**= ->", x)  # 8


# ----------------------------------------------------------
# 9. &=   (Bitwise AND and assign)
# x &= 3  means  x = x & 3
# ----------------------------------------------------------
x = 6      # binary: 110
x &= 3     # binary: 011
print("&= ->", x)   # 2  (binary 010)


# ----------------------------------------------------------
# 10. |=   (Bitwise OR and assign)
# x |= 3  means  x = x | 3
# ----------------------------------------------------------
x = 4      # binary: 100
x |= 3     # binary: 011
print("|= ->", x)   # 7  (binary 111)


# ----------------------------------------------------------
# 11. ^=   (Bitwise XOR and assign)
# x ^= 3  means  x = x ^ 3
# ----------------------------------------------------------
x = 6      # binary: 110
x ^= 3     # binary: 011
print("^= ->", x)   # 5  (binary 101)


# ----------------------------------------------------------
# 12. >>=   (Right-shift and assign)
# x >>= 3  means  x = x >> 3
# ----------------------------------------------------------
x = 32     # binary: 100000
x >>= 3    # shift right by 3 → 100 (binary)
print(">>= ->", x)  # 4


# ----------------------------------------------------------
# 13. <<=   (Left-shift and assign)
# x <<= 3  means  x = x << 3
# ----------------------------------------------------------
x = 4      # binary: 100
x <<= 3    # shift left by 3 → 100000 (binary)
print("<<= ->", x)  # 32


# ARITHMETIC OPERATORS WITH DIFFERENT DATA TYPES
# Only using print() — results and implicit conversions shown
# ----------------------------------------------------------
i = 5                       # int
f = 2.5                     # float
b = True                    # bool (True = 1, False = 0)
c = 3 + 2j                  # complex
s = "Hi"                    # string
L = [1, 2]                  # list
T = (1, 2)                  # tuple


# ==========================================================
# 1. ADDITION (+)
# ==========================================================
print("\n---- ADDITION (+) ----")
print(i + i)       # 10        | result type: int         | implicit conversion: no conversion (int + int => int)
print(i + f)       # 7.5       | result type: float       | implicit conversion: int -> float
print(i + b)       # 6         | result type: int         | implicit conversion: bool -> int (True == 1)
print(i + c)       # (8+2j)    | result type: complex     | implicit conversion: int -> complex
print(s + s)       # HiHi      | result type: str         | string concatenation (no numeric conversion)
print(L + L)       # [1, 2, 1, 2] | result type: list     | list concatenation
print(T + T)       # (1, 2, 1, 2) | result type: tuple    | tuple concatenation


# ==========================================================
# 2. SUBTRACTION (-)
# ==========================================================
print("\n---- SUBTRACTION (-) ----")
print(i - i)       # 0         | result type: int        | no conversion
print(i - f)       # 2.5       | result type: float      | implicit conversion: int -> float
print(i - b)       # 4         | result type: int        | implicit conversion: bool -> int
print(i - c)       # (2-2j)    | result type: complex    | implicit conversion: int -> complex


# ==========================================================
# 3. MULTIPLICATION (*) 
# ==========================================================
print("\n---- MULTIPLICATION (*) ----")
print(i * i)       # 25        | result type: int         | no conversion
print(i * f)       # 12.5      | result type: float       | int -> float
print(i * b)       # 5         | result type: int         | bool -> int
print(i * c)       # (15+10j)  | result type: complex     | int -> complex
print(s * 3)       # HiHiHi    | result type: str         | string repetition (int multiplier)
print(L * 2)       # [1, 2, 1, 2] | result type: list     | list repetition
print(T * 2)       # (1, 2, 1, 2) | result type: tuple    | tuple repetition


# ==========================================================
# 4. DIVISION (/)
# ==========================================================
print("\n---- DIVISION (/) ----")
print(i / i)       # 1.0       | result type: float      | division produces float
print(i / f)       # 2.0       | result type: float      | int -> float
print(i / b)       # 5.0       | result type: float      | bool -> int -> float
print(i / c)       # (1.1538461538461537-0.7692307692307693j) | result type: complex | int -> complex


# ==========================================================
# 5. MODULUS (%) 
# ==========================================================
print("\n---- MODULUS (%) ----")
print(i % i)       # 0         | result type: int        | no conversion
print(i % f)       # 0.0       | result type: float      | int -> float (float modulus)
print(i % b)       # 0         | result type: int        | bool -> int


# ==========================================================
# 6. EXPONENTIATION (**)
# ==========================================================
print("\n---- EXPONENTIATION (**) ----")
print(i ** i)      # 3125                                     | result type: int        | no conversion
print(i ** f)      # 55.90169943749474                        | result type: float      | int -> float (float exponent)
print(i ** b)      # 5                                        | result type: int        | bool -> int (True == 1)
print(i ** c)      # (-124.62695298730259-9.651247079335019j) | result type: complex    | int -> complex

# note: 5 ** (3+2j) = 125 * e^{2j * ln(5)} = 125*(cos(2 ln5) + j sin(2 ln5))
# approx shown above (real and imaginary parts given)


# ==========================================================
# 7. FLOOR DIVISION (//)
# ==========================================================
print("\n---- FLOOR DIVISION (//) ----")
print(i // i)      # 1         | result type: int        | integer floor division
print(i // f)      # 2.0       | result type: float      | float floor division (5 // 2.5 => 2.0)
print(i // b)      # 5         | result type: int        | bool -> int


# ==========================================================
# INVALID OPERATIONS 
# ==========================================================


# ----------------------------------------------------------
# ADDITION INVALID CASES
# ----------------------------------------------------------
# 'Hi' + 5          -> TypeError  
#       Cannot add string and integer. Only string+string is allowed.
#
# [1,2] + 5         -> TypeError  
#       Lists can only be added to lists (concatenation).
#
# (1,2) + 5         -> TypeError  
#       Tuples can only be added to tuples.


# ----------------------------------------------------------
# SUBTRACTION INVALID CASES
# ----------------------------------------------------------
# 'Hi' - 'Hi'       -> TypeError  
#       Subtraction is defined only for numeric types.
#
# [1,2] - [1]       -> TypeError  
#       Lists do not support subtraction.
#
# (1,2) - (2,)      -> TypeError  
#       Tuples do not support subtraction.


# ----------------------------------------------------------
# MULTIPLICATION INVALID CASES
# ----------------------------------------------------------
# 'Hi' * 2.5        -> TypeError  
#       Strings can only be multiplied by integers (repetition).
#
# [1,2] * [1]       -> TypeError  
#       List cannot be multiplied by list.
#
# (1,2) * (2,)      -> TypeError  
#       Tuple cannot be multiplied by tuple.


# ----------------------------------------------------------
# DIVISION INVALID CASES
# ----------------------------------------------------------
# 'Hi' / 'Hi'       -> TypeError  
#       Division is a numeric-only operation.
#
# [1,2] / [1]       -> TypeError  
#       Lists cannot be divided.
#
# (1,2) / (2,)      -> TypeError  
#       Tuples cannot be divided.


# ----------------------------------------------------------
# MODULUS INVALID CASES
# ----------------------------------------------------------
# 5 % (3+2j)        -> TypeError  
#       Modulus (%) does not work with complex numbers.
#
# 'Hi' % 'Hi'       -> TypeError  
#       String % string tries old-style formatting, but invalid here.
#
# [1,2] % [1]       -> TypeError  
#       Lists do not support modulus.
#
# (1,2) % (2,)      -> TypeError  
#       Tuples do not support modulus.


# ----------------------------------------------------------
# EXPONENTIATION INVALID CASES
# ----------------------------------------------------------
# 'Hi' ** 2         -> TypeError  
#       Cannot exponentiate strings.
#
# [1,2] ** 2        -> TypeError  
#       Lists do not support exponentiation.
#
# (1,2) ** 2        -> TypeError  
#       Tuples do not support exponentiation.


# ----------------------------------------------------------
# FLOOR DIVISION INVALID CASES
# ----------------------------------------------------------
# 5 // (3+2j)       -> TypeError  
#       Floor division not defined for complex numbers.
#
# 'Hi' // 'Hi'      -> TypeError  
#       Strings have no numeric floor division.
#
# [1,2] // [1]      -> TypeError  
#       Lists cannot use floor division.
#
# (1,2) // (2,)     -> TypeError  
#       Tuples cannot use floor division.
# ==========================================================
# COMPARISON OPERATORS WITH DIFFERENT DATA TYPES
# Only using print() — results + implicit conversions
# ==========================================================

# ----------------------------------------------------------
# DATA TYPES
# ----------------------------------------------------------
i = 5                       # int
f = 2.5                     # float
b = True                    # bool  (True==1, False==0)
c = 3 + 2j                  # complex
s = "Hi"                    # string
L = [1, 2]                  # list
T = (1, 2)                  # tuple


# ==========================================================
# 1. EQUALS (==)
# ==========================================================
print("\n---- EQUALS (==) ----")
print(i == i)         # True     | int==int → no conversion
print(i == f)         # False    | int converted to float for comparison
print(i == b)         # False    | bool becomes int (True==1)
print(s == "Hi")      # True     | string equality
print(L == [1,2])     # True     | list element-wise equality
print(T == (1,2))     # True     | tuple element-wise equality
print(c == c)         # True     | complex equality

# Invalid: comparing complex with < or > (not here, == works always)


# ==========================================================
# 2. NOT EQUAL (!=)
# ==========================================================
print("\n---- NOT EQUAL (!=) ----")
print(i != f)         # True     | int→float
print(i != b)         # True     | bool→int
print(s != "Bye")     # True     | string compare
print(L != [2,1])     # True     | list compare
print(T != (1,2,3))   # True     | tuple compare


# ==========================================================
# 3. GREATER THAN (>)
# ==========================================================
print("\n---- GREATER THAN (>) ----")
print(i > f)          # True     | int→float
print(i > b)          # True     | bool→int

# Strings compare lexicographically (alphabet order)
print("'Hi' > 'Ha' =", "Hi" > "Ha")   # True  | lexicographic compare

# Invalid: complex > complex, list > list, tuple > tuple


# ==========================================================
# 4. LESS THAN (<)
# ==========================================================
print("\n---- LESS THAN (<) ----")
print(i < f)          # False    | int→float
print(i < b)          # False    | bool→int
print("'Hi' < 'Hz' =", "Hi" < "Hz")   # True  | lexicographic compare


# ==========================================================
# 5. GREATER THAN OR EQUAL (>=)
# ==========================================================
print("\n---- GREATER OR EQUAL (>=) ----")
print(i >= f)         # True     | int→float
print(i >= b)         # True     | bool→int
print("Hi" >= "Hi")   # True     | equal strings


# ==========================================================
# 6. LESS THAN OR EQUAL (<=)
# ==========================================================
print("\n---- LESS OR EQUAL (<=) ----")
print(i <= f)         # False    | int→float
print(i <= b)         # False    | bool→int
print("Hi" <= "Hi")   # True     | equal strings


# ==========================================================
# INVALID COMPARISONS (FULL EXPLANATION IN COMMENTS)
# ==========================================================


# ----------------------------------------------------------
# COMPLEX NUMBERS INVALID
# ----------------------------------------------------------
# complex > complex     -> INVALID
# complex < complex     -> INVALID
# complex >= complex    -> INVALID
# complex <= complex    -> INVALID
#
# Reason:
#   Complex numbers have no natural ordering in mathematics.


# ----------------------------------------------------------
# LIST INVALID COMPARES
# ----------------------------------------------------------
# [1,2] > [1,1]         -> INVALID (in Python 3)
# [1,2] < [1,1]         -> INVALID
#
# Reason:
#   Python 3 removed list/tuple ordering. Equality works, ordering does not.


# ----------------------------------------------------------
# TUPLE INVALID COMPARES
# ----------------------------------------------------------
# (1,2) > (1,1)         -> INVALID
# (1,2) < (1,1)         -> INVALID
#
# Reason:
#   Same as list: ordering not supported in Python 3.


# ----------------------------------------------------------
# STRING VS NUMBER INVALID
# ----------------------------------------------------------
# "Hi" > 5             -> INVALID
# "Hi" < 5             -> INVALID
#
# Reason:
#   Python cannot compare different unrelated types.


# ----------------------------------------------------------
# LIST/TUPLE VS NUMBER INVALID
# ----------------------------------------------------------
# [1,2] > 5            -> INVALID
# (1,2) < 3            -> INVALID
#
# Reason:
#   Containers cannot be compared with integers.
# ==========================================================
# LOGICAL OPERATORS (and, or, not)
# Only using print() — results + implicit conversions
# ==========================================================

# ----------------------------------------------------------
# DATA TYPES (for truthiness tests)
# ----------------------------------------------------------
i = 5         # truthy (non-zero)
f = 0.0       # falsy (zero float)
b = True      # truthy
c = 0 + 0j    # falsy (complex zero)
s = "Hi"      # truthy (non-empty)
e = ""        # falsy (empty string)
L = [1, 2]    # truthy (non-empty list)
E = []        # falsy (empty list)


# ==========================================================
# 1. AND OPERATOR
# ==========================================================
print("\n---- AND ----")

# Basic boolean examples
print(True and True)      # True   | both true
print(True and False)     # False  | second is false
print(False and True)     # False  | first false → short-circuits

# With numbers (converted to truthiness)
print(i and f)            # 0.0    | 5 (true) AND 0.0 (false) → returns second operand
print(f and i)            # 0.0    | 0.0 (false) → returns first operand

# With strings
print(s and e)            # ""     | "Hi" (true) AND "" (false)
print(e and s)            # ""     | "" (false) → short-circuit

# With lists
print(L and E)            # []     | [1,2] (true) AND [] (false)
print(E and L)            # []     | [] (false)


# ==========================================================
# 2. OR OPERATOR
# ==========================================================
print("\n---- OR ----")

# Basic boolean examples
print(True or False)      # True
print(False or True)      # True
print(False or False)     # False

# With numbers
print(i or f)             # 5      | first truthy → returned
print(f or i)             # 5      | f = 0.0 (false) → returns i

# With strings
print(s or e)             # "Hi"   | first truthy
print(e or s)             # "Hi"   | empty string false → returns "Hi"

# With lists
print(L or E)             # [1,2]
print(E or L)             # [1,2]


# ==========================================================
# 3. NOT OPERATOR
# ==========================================================
print("\n---- NOT ----")

print(not True)           # False
print(not False)          # True

print(not i)              # False   | non-zero → True, reversed to False
print(not f)              # True    | 0.0 is False → reversed to True

print(not s)              # False   | non-empty string True
print(not e)              # True    | empty string False

print(not L)              # False   | non-empty list True
print(not E)              # True    | empty list False


# ==========================================================
# INVALID OPERATIONS SUMMARY (EXPLAINED IN COMMENTS)
# ==========================================================

print("\n---- INVALID LOGICAL OPERATIONS SUMMARY ----")

# ----------------------------------------------------------
# Logical operators do NOT throw TypeError with any datatype.
# and/or/not work with ANY Python object because Python uses:
#   TRUTHINESS rules:
#     False, None, 0, 0.0, 0+0j, "", [], (), {}  => False
#     everything else                             => True
#
# There are NO invalid datatype combinations like arithmetic/comparison.
#
# BUT invalid *expressions* happen when operands inside conditions
# use >, <, %, // incorrectly.
# For example:
#   "Hi" and (5 % "Hello")   -> invalid because of '%' only
#   [] or (5 // (3+2j))      -> invalid because of '//' only
#
# The logical operator itself NEVER causes the error.
# ----------------------------------------------------------

#"Logical operators accept ALL data types."
#"Invalid expressions occur ONLY if the inside operation is invalid (like 'Hi' < 5 or 5 % 'Hi')"


# ==========================================================
# IDENTITY, MEMBERSHIP, AND BITWISE OPERATORS
# Only using print() — results + explanations
# ==========================================================

# ----------------------------------------------------------
# SAMPLE DATA
# ----------------------------------------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

x = 5
y = 5
z = 10

s = "Hello"
L = [10, 20, 30]
T = (1, 2, 3)

# For bitwise examples
p = 6    # 110 in binary
q = 3    # 011 in binary



# ==========================================================
# 5. IDENTITY OPERATORS
# ==========================================================
print("\n---- IDENTITY OPERATORS (is, is not) ----")

print(a is b)       # True   | both names refer to SAME list object
print(a is c)       # False  | same contents, but DIFFERENT objects
print(x is y)       # True   | small ints are cached → same memory
print(x is z)       # False  | different values → different objects

print(a is not b)   # False  | they are same object
print(a is not c)   # True   | different memory locations



# ==========================================================
# 6. MEMBERSHIP OPERATORS (in, not in)
# ==========================================================
print("\n---- MEMBERSHIP OPERATORS (in, not in) ----")

# Strings
print("H" in s)             # True  | substring exists
print("He" in s)            # True  | substring exists
print("Z" in s)             # False | not found

# Lists
print(20 in L)              # True  | element exists
print(40 in L)              # False | not found

# Tuples
print(2 in T)               # True
print(5 in T)               # False

# not in
print("H" not in s)         # False
print(50 not in L)          # True



# ==========================================================
# 7. BITWISE OPERATORS (&, |, ^, ~, <<, >>)
# ==========================================================
print("\n---- BITWISE OPERATORS ----")
print("p =", p, "binary:", bin(p))   # 110
print("q =", q, "binary:", bin(q))   # 011

print(p & q)              # 2   | AND  | 110 & 011 = 010
print(p | q)              # 7   | OR   | 110 | 011 = 111
print(p ^ q)              # 5   | XOR  | 110 ^ 011 = 101

print(~p)                 # -7  | NOT  | flips all bits
print(p << 1)             # 12  | left shift  | 1100
print(p >> 1)             # 3   | right shift | 011



# ==========================================================
# INVALID OPERATIONS (EXPLAINED IN COMMENTS)
# ==========================================================
#"\n---- INVALID OPERATIONS SUMMARY ----"

# IDENTITY INVALID?
# There are NO invalid cases.
# 'is' and 'is not' work with ANY data type.

#"Identity operators: no invalid cases (they accept all types)."

# MEMBERSHIP INVALID CASES
# These are invalid because membership only works with:
#   strings, lists, tuples, sets, dicts
#
# 5 in 10        -> INVALID (int is not iterable)
# 5 in 5.5       -> INVALID (float not iterable)
# 1 in 2+3j      -> INVALID (complex not iterable)

#"Membership invalid: 5 in 10, 5 in 5.5, 1 in (2+3j)  → TypeError"

# BITWISE INVALID CASES
# Bitwise operators ONLY work with integers.
#
# "Hi" & "Hello" -> INVALID
# 5.5 | 2        -> INVALID
# [1,2] ^ [3,4]  -> INVALID

#"Bitwise invalid: 'Hi' & 'Hello', 5.5 | 2, [1,2] ^ [3,4]  → TypeError"




