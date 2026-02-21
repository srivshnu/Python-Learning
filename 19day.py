"""
PYTHON FILE HANDLING & DATA FORMATS
-----------------------------------
Focus: Reading, writing, updating, and parsing different file types (.txt, .json, .csv, .xml).

"""

import os
import json
import csv
import xml.etree.ElementTree as ET

# =============================================================
# 1) BASIC FILE OPERATIONS (.txt)
# =============================================================
# The open() function uses modes: 'r' (read), 'a' (append), 'w' (write), 'x' (create).
# Using the `with` statement ensures the file automatically closes when done.

# Write: Overwrites existing content or creates a new file
with open('sample.txt', 'w') as f:
    f.write("This is an example to show how to open a file and read.\n")

# Append: Adds to the end of an existing file
with open('sample.txt', 'a') as f:
    f.write("This is the second line of the text.\n")

# Read: Extracting text
with open('sample.txt', 'r') as f:
    # read() gets everything as a single string
    full_text = f.read()
    print("--- read() ---")
    print(full_text)

with open('sample.txt', 'r') as f:
    # read().splitlines() returns a list of lines without the \n character
    lines = f.read().splitlines()
    print("--- splitlines() ---")
    print(lines)
# OUTPUT: ['This is an example to show how to open a file and read.', 'This is the second line of the text.']


# =============================================================
# 2) DELETING FILES
# =============================================================
# Use the os module to safely remove files.

file_path = 'sample.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"\n[Status] File '{file_path}' successfully deleted.")
else:
    print("\n[Status] The file does not exist.")


# =============================================================
# 3) JSON HANDLING (.json)
# =============================================================
# JSON (JavaScript Object Notation) is essentially a stringified dictionary.

# 3.1: Parsing JSON string to a Python Dictionary (json.loads)
person_json_str = '''{
    "name": "Vishnu",
    "country": "India",
    "skills": ["C++", "Python", "SQL"]
}'''

person_dct = json.loads(person_json_str)
print(f"\nParsed JSON Dictionary: {type(person_dct)}")
print(f"Name extracted: {person_dct['name']}")
# OUTPUT: Name extracted: Vishnu

# 3.2: Converting Python Dictionary back to a JSON string (json.dumps)
formatted_json = json.dumps(person_dct, indent=4)
print(f"Formatted JSON String:\n{formatted_json}")

# 3.3: Saving a Dictionary as a .json File (json.dump)
with open('profile.json', 'w', encoding='utf-8') as f:
    json.dump(person_dct, f, ensure_ascii=False, indent=4)


# =============================================================
# 4) CSV HANDLING (.csv)
# =============================================================
# Comma Separated Values are common for tabular spreadsheet/database data.

# (Creating a dummy CSV for the example)
with open('data.csv', 'w') as f:
    f.write("name,country,city,skills\nAsabeneh,Finland,Helsinki,JavaScript\nVishnu,India,Thanjavur,C++")

# Reading the CSV
with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    print("\n--- CSV Data ---")
    for row_idx, row in enumerate(csv_reader):
        if row_idx == 0:
            print(f"Headers: {', '.join(row)}")
        else:
            print(f"Data: {row[0]} lives in {row[2]} and codes in {row[3]}")
# OUTPUT:
# Headers: name, country, city, skills
# Data: Asabeneh lives in Helsinki and codes in JavaScript
# Data: Vishnu lives in Thanjavur and codes in C++


# =============================================================
# 5) XML HANDLING (.xml)
# =============================================================
# XML stores structured data using custom tags, similar to HTML.

# (Creating a dummy XML for the example)
xml_data = '''<?xml version="1.0"?>
<person gender="male">
  <name>John</name>
  <country>USA</country>
  <skills>
    <skill>Python</skill>
  </skills>
</person>'''

with open('data.xml', 'w') as f:
    f.write(xml_data)

# Parsing the XML
tree = ET.parse('data.xml')
root = tree.getroot()

print("\n--- XML Data ---")
print(f"Root tag: {root.tag}")
print(f"Root attributes: {root.attrib}")

for child in root:
    if child.tag == 'skills':
        for subchild in child:
            print(f"Nested element: {subchild.tag} -> {subchild.text}")
    else:
        print(f"Element: {child.tag} -> {child.text}")
# OUTPUT:
# Root tag: person
# Root attributes: {'gender': 'male'}
# Element: name -> John
# Element: country -> USA
# Nested element: skill -> Python

# Clean up files generated during this script
os.remove('profile.json')
os.remove('data.csv')
os.remove('data.xml')