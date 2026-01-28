"""
PYTHON ERROR HANDLING & DATA UTILITIES
--------------------------------------
Focus: Robustness and efficient data manipulation.
"""

# =============================================================
# 1) ERROR MANAGEMENT (try, except, else, finally)
# =============================================================
# Standard idiom for "graceful exits" from errors.

try:
    # Simulating user input for a calculation
    # Let's assume the user enters '1990'
    birth_year = '1990' 
    current_age = 2026 - int(birth_year)
    print(f'Calculated Age: {current_age}')
except ValueError:
    print('Error: Please provide a valid integer.')
except Exception as error_msg:
    print(f'Unexpected error: {error_msg}')
else:
    print('Processing finished successfully.')
finally:
    print('Closing session.')

# OUTPUT:
# Calculated Age: 36
# Processing finished successfully.
# Closing session.

# =============================================================
# 2) UNPACKING SEQUENCES (*)
# =============================================================
# Passing list elements as individual arguments.

def calc_total(v1, v2, v3, v4, v5):
    return v1 + v2 + v3 + v4 + v5

data_points = [10, 20, 30, 40, 50]
print("Total via unpacking:", calc_total(*data_points)) 
# OUTPUT: Total via unpacking: 150

# Destructuring with the rest operator
technologies = ['Python', 'JavaScript', 'Rust', 'Go', 'Swift']
primary, secondary, niche, *others = technologies
print(f"Top: {primary}, {secondary}. Remaining: {others}")
# OUTPUT: Top: Python, JavaScript. Remaining: ['Go', 'Swift']

# =============================================================
# 3) UNPACKING DICTIONARIES (**)
# =============================================================

def member_profile(user, role, dept):
    return f"Member: {user} | Role: {role} | Dept: {dept}"

staff_record = {'user': 'Jordan', 'role': 'Lead Dev', 'dept': 'Engineering'}
print(member_profile(**staff_record))
# OUTPUT: Member: Jordan | Role: Lead Dev | Dept: Engineering

# =============================================================
# 4) PACKING (*args and **kwargs)
# =============================================================
# Handling an arbitrary number of arguments.

def handle_args(*args, **kwargs):
    print("Positional (Tuple):", args)
    print("Keyword (Dict):", kwargs)

handle_args('Alpha', 'Beta', priority='High', version=2.0)
# OUTPUT:
# Positional (Tuple): ('Alpha', 'Beta')
# Keyword (Dict): {'priority': 'High', 'version': 2.0}

# =============================================================
# 5) LIST SPREADING
# =============================================================

group_x = ['A', 'B']
group_y = ['D', 'E']
merged_list = ['Start', *group_x, 'C', *group_y]
print("Merged:", merged_list)
# OUTPUT: Merged: ['Start', 'A', 'B', 'C', 'D', 'E']

# =============================================================
# 6) ENUMERATE & ZIP
# =============================================================

# Enumerate: Accessing index and value
projects = ['Web App', 'Database', 'API']
for idx, title in enumerate(projects):
    print(f"Project #{idx}: {title}")
# OUTPUT:
# Project #0: Web App
# Project #1: Database
# Project #2: API

# Zip: Combining parallel lists
employees = ['Alice', 'Bob', 'Charlie']
tasks = [12, 8, 15]

for name, count in zip(employees, tasks):
    print(f"{name} completed {count} tasks.")
# OUTPUT:
# Alice completed 12 tasks.
# Bob completed 8 tasks.
# Charlie completed 15 tasks.