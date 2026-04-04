# -------------------------------------------------------------
# 30 DAYS OF PYTHON: DAY 24 - STATISTICS & NUMPY
# -------------------------------------------------------------

# =============================================================
# 📘 Python for Statistical Analysis
# =============================================================

# --- Statistics ---
# Statistics is the discipline that studies the collection, organization, 
# displaying, analysing, interpretation and presentation of data. 
# Statistics is a branch of Mathematics that is recommended to be a prerequisite 
# for data science and machine learning. Statistics is a very broad field but we 
# will focus in this section only on the most relevant part.
# Having some statistical knowledge will help you to make decisions based on data.

# --- Data ---
# Data is any set of characters that is gathered and translated for some purpose, 
# usually analysis. It can be any character, including text and numbers, pictures, 
# sound, or video. If data is not put in a context, it doesn't make any sense to a 
# human or computer. The work flow of data analysis, data science or machine learning 
# starts from data. Data can be provided from some data source or it can be created. 
# There are structured and unstructured data.

# --- Statistics Module ---
# The Python `statistics` module provides functions for calculating mathematical 
# statistics of numerical data. It is aimed at the level of graphing and scientific 
# calculators, not as a competitor to NumPy, SciPy, etc.

# =============================================================
# 📘 NumPy
# =============================================================
# NumPy is the core library for scientific computing in Python. It provides a 
# high-performance multidimensional array object, and tools for working with arrays.
# Install it via terminal: pip install numpy

# 

# --- Importing NumPy ---
import numpy as np

# print('numpy:', np.__version__) # Check the version
# print(dir(np))                  # Check available methods


# -------------------------------------------------------------
# Creating NumPy Arrays
# -------------------------------------------------------------

# --- Creating int numpy arrays ---
python_list = [1, 2, 3, 4, 5]
print('Type:', type(python_list)) 
print(python_list) 

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# --- Creating float numpy arrays ---
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

# --- Creating boolean numpy arrays ---
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# --- Creating multidimensional array using numpy ---
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)


# -------------------------------------------------------------
# Converting & Shapes
# -------------------------------------------------------------

# --- Converting numpy array to list ---
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# --- Creating numpy array from tuple ---
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_tuple: ', python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)

# --- Shape of numpy array ---
# The shape method provides the shape of the array as a tuple (rows, columns).
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)

print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)


# -------------------------------------------------------------
# Data Types & Size
# -------------------------------------------------------------

# --- Data type of numpy array ---
# Types: str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# --- Size of a numpy array ---
# In numpy to know the number of items in a numpy array list we use size
print('The size:', numpy_array_from_list.size)
print('The size:', numpy_two_dimensional_list.size)


# -------------------------------------------------------------
# Mathematical Operation using numpy
# -------------------------------------------------------------
# numpy can allow to do any mathematical operation without looping.

print('original array: ', numpy_array_from_list)

# Addition
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)

# Subtraction
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)

# Multiplication
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

# Division
ten_div_original = numpy_array_from_list / 10
print(ten_div_original)

# Modulus; Finding the remainder
ten_mod_original = numpy_array_from_list % 3
print(ten_mod_original)

# Floor division: the division result without the remainder
ten_floor_original = numpy_array_from_list // 10
print(ten_floor_original)

# Exponential
ten_exp_original = numpy_array_from_list ** 2
print(ten_exp_original)


# -------------------------------------------------------------
# Checking & Converting data types
# -------------------------------------------------------------
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# 1. Int to Float
numpy_int_to_float = np.array([1, 2, 3, 4], dtype='float')
# 2. Float to Int
numpy_float_to_int = np.array([1., 2., 3., 4.], dtype='int')
# 3. Int to boolean
numpy_int_to_bool = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
# 4. Int to str
numpy_int_to_str = numpy_float_arr.astype('int').astype('str')


# -------------------------------------------------------------
# Multi-dimensional Arrays & Slicing
# -------------------------------------------------------------
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# --- Getting items from a numpy array ---
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)

# 

# --- Slicing Numpy array ---
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

# How to reverse the rows and the whole array?
print(two_dimension_array[::-1])

# Reverse the row and column positions
print(two_dimension_array[::-1, ::-1])

# --- How to represent missing values? (Assigning values) ---
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)


# -------------------------------------------------------------
# Zeros, Ones, Reshape, and Stacking
# -------------------------------------------------------------

# Numpy Zeroes
numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)

# Numpy Ones
numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)
twoes = numpy_ones * 2

# Reshape & Flatten
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)

# Horizontal Stack
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# Vertical Stack
print('Vertical Append:\n', np.vstack((np_list_one, np_list_two)))


# -------------------------------------------------------------
# Generating Random Numbers
# -------------------------------------------------------------
print(np.random.random())               # Generate a random float number
print(np.random.random(5))              # Generate 5 random float numbers
print(np.random.randint(0, 11))         # Random int between 0 and 10
print(np.random.randint(2, 10, size=4)) # Random ints creating a 1D array
print(np.random.randint(2, 10, size=(3, 3))) # Random ints creating a 3x3 array

# Normal distribution: np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)

# Numpy and Statistics (Plotting example with matplotlib/seaborn)
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)
# plt.show()


# -------------------------------------------------------------
# Matrices & Generating Sequences
# -------------------------------------------------------------

# --- Matrix in numpy ---
four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# --- Numpy arange() ---
# Similar to range: numpy.arange(start, stop, step)
lst = range(0, 11, 2)
whole_numbers = np.arange(0, 20, 1)
natural_numbers = np.arange(1, 20, 1)
odd_numbers = np.arange(1, 20, 2)
even_numbers = np.arange(2, 20, 2)

# --- linspace & logspace ---
print(np.linspace(1.0, 5.0, num=10))
print(np.linspace(1.0, 5.0, num=5, endpoint=False))
print(np.logspace(2, 4.0, num=4))

# To check the size of an array in bytes
x = np.array([1, 2, 3], dtype=np.complex128)
print(x.itemsize) # Returns 16


# -------------------------------------------------------------
# NumPy Statistical Functions
# -------------------------------------------------------------
# Functions: np.min(), np.max(), np.mean(), np.median(), np.std(), variance, percentile

np_normal_dis = np.random.normal(5, 0.5, 100)

print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
print('sd: ', two_dimension_array.std())

print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ===')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))


# --- Repeating Sequences ---
a = [1, 2, 3]
print('Tile:   ', np.tile(a, 2))   # [1 2 3 1 2 3]
print('Repeat: ', np.repeat(a, 2)) # [1 1 2 2 3 3]


# --- More Random Numbers ---
print(np.random.random(size=[2, 3]))
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print(np.random.rand(2, 2))
print(np.random.randn(2, 2))
print(np.random.randint(0, 10, size=[5, 3]))

# Using SciPy for Mode
# from scipy import stats
# np_normal_dis = np.random.normal(5, 0.5, 1000)
# print('mode: ', stats.mode(np_normal_dis))


# -------------------------------------------------------------
# Linear Algebra
# -------------------------------------------------------------
# 1. Dot Product
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print('Dot product:', np.dot(f, g))  # 23

# 2. Matrix Multiplication (matmul)
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print('Matmul:\n', np.matmul(h, i))

# 3. Determinant
print('Determinant:', np.linalg.det(i))

# Complex Array Generation Example
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)


# -------------------------------------------------------------
# Linear Equations Example (Temperature vs Pressure)
# -------------------------------------------------------------
new_list = [x + 2 for x in range(0, 11)]
np_arr = np.array(range(0, 11))
print(np_arr + 2)

temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print('Pressure:', pressure)

# Plotting code (Commented out for script format)
# plt.plot(temp,pressure)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()


# Gaussian normal distribution generation plot
# mu = 28
# sigma = 15
# samples = 100000
# x = np.random.normal(mu, sigma, samples)
# ax = sns.distplot(x);
# ax.set(xlabel="x", ylabel='y')
# plt.show()


# =============================================================
# 📘 Summary: NumPy Arrays vs Python Lists
# =============================================================
# 1. Arrays support vectorized operations, while lists don’t.
# 2. Once an array is created, you cannot change its size. You will have to create 
#    a new array or overwrite the existing one.
# 3. Every array has one and only one dtype. All items in it should be of that dtype.
# 4. An equivalent numpy array occupies much less space than a python list of lists.
# 5. numpy arrays support boolean indexing.

# 💻 Exercises: Day 24 - Repeat all the examples