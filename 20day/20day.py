import webbrowser
import requests

# =============================================================
# 1) WHAT IS PIP & INSTALLATION
# =============================================================
# PIP stands for Preferred installer program. It's used to install
# Python packages (modules we can use in our applications).

# To install pip (if not already installed) via terminal:
# $ pip install pip

# To check pip version:
# $ pip --version


# =============================================================
# 2) INSTALLING & UNINSTALLING PACKAGES
# =============================================================
# We can install packages from the Python community.

# Installing NumPy (fundamental package for scientific computing):
# $ pip install numpy

# Installing Pandas (data structures and analysis tools):
# $ pip install pandas

# Uninstalling a package:
# $ pip uninstall packagename


# =============================================================
# 3) PACKAGE MANAGEMENT COMMANDS
# =============================================================
# Listing installed packages:
# $ pip list

# Showing information about a specific package:
# $ pip show pandas
# $ pip show --verbose pandas

# Generating a list of installed packages with versions (useful for requirements.txt):
# $ pip freeze


# =============================================================
# 4) USING BUILT-IN MODULES (Example: webbrowser)
# =============================================================
# Some modules come pre-installed with Python, like 'webbrowser'.

print("\n--- WEBBROWSER EXAMPLE ---")
# list of urls
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# Uncomment below to open the urls in your browser
# for url in url_lists:
#     webbrowser.open_new_tab(url)
print("Webbrowser code executed")


# =============================================================
# 5) READING FROM URL & APIs (using 'requests' package)
# =============================================================
# We use the 'requests' package to open network connections and fetch data.
# Install it first: $ pip install requests

print("\n--- REQUESTS TEXT EXAMPLE ---")
# Reading a text file from a URL
url_text = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response_text = requests.get(url_text)

print(f"Response Object: {response_text}")
print(f"Status Code: {response_text.status_code}") # 200 means success
# print(response_text.headers) # View headers
# print(response_text.text)    # View the actual text content (commented out for brevity)
print("Successfully fetched text data.")


print("\n--- REQUESTS JSON (API) EXAMPLE ---")
# Reading JSON data from an API
# Using a dummy API for demonstration as the original one might be down
url_api = 'https://jsonplaceholder.typicode.com/users' 
response_api = requests.get(url_api)

print(f"Response Object: {response_api}")
print(f"Status Code: {response_api.status_code}")

if response_api.status_code == 200:
    users = response_api.json() # Extract JSON data
    print("First user data fetched:")
    print(users[:1]) # Slicing to show only the first item
else:
     print("Failed to fetch API data.")


# =============================================================
# 6) CREATING A CUSTOM PACKAGE
# =============================================================
# A package is a folder containing one or more module files and an __init__.py file.

# Folder Structure Example:
# mypackage/
#     __init__.py
#     arithmetics.py
#     greet.py


# Inside greet.py:
# def greet_person(firstname, lastname):
#     return f'{firstname} {lastname}, welcome!'

# To use it (assuming the folder exists):
from mypackage import arithmetics, greet
print(arithmetics.add_numbers(1, 2, 3))
print(greet.greet_person('John', 'Doe'))
