"""
PYTHON REGULAR EXPRESSIONS (re MODULE)
--------------------------------------
Focus: Finding patterns in text and strings using the RegEx module.

"""

import re

# =============================================================
# 1) MATCH (re.match)
# =============================================================
# Searches only at the beginning of the first line of the string.
# Returns a match object if found, else returns None.

txt = 'I love to teach python and javaScript'

# Using re.I for case-insensitive matching
match = re.match('I love to teach', txt, re.I)
print(f"Match object: {match}")
# OUTPUT: Match object: <re.Match object; span=(0, 15), match='I love to teach'>

# Extracting the matched substring using span()
start, end = match.span()
print(f"Extracted substring: {txt[start:end]}")
# OUTPUT: Extracted substring: I love to teach

# Checking for a pattern that is NOT at the beginning
failed_match = re.match('I like to teach', txt, re.I)
print(f"Failed match: {failed_match}")
# OUTPUT: Failed match: None


# =============================================================
# 2) SEARCH (re.search)
# =============================================================
# Returns a match object if there is one anywhere in the string,
# including multiline strings.

txt_multiline = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

search_match = re.search('first', txt_multiline, re.I)
print(f"Search found: {search_match}")
# OUTPUT: Search found: <re.Match object; span=(100, 105), match='first'>


# =============================================================
# 3) FIND ALL (re.findall)
# =============================================================
# Checks for the pattern throughout the whole string and 
# returns all the matches as a list.

matches = re.findall('language', txt_multiline, re.I)
print(f"Findall matches: {matches}")
# OUTPUT: Findall matches: ['language', 'language']

# Using pattern brackets instead of re.I flag
pattern_matches = re.findall('[Pp]ython', txt_multiline)
print(f"Bracket pattern matches: {pattern_matches}")
# OUTPUT: Bracket pattern matches: ['Python', 'python']


# =============================================================
# 4) REPLACE SUBSTRING (re.sub)
# =============================================================
# Replaces one or many matches within a string.

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt_multiline)
print(f"Replaced text:\n{match_replaced}")
# OUTPUT: 
# Replaced text:
# JavaScript is the most beautiful language that a human being has ever created.
# I recommend JavaScript for a first programming language

# Cleaning noisy text
noisy_txt = '%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.'
clean_txt = re.sub('%', '', noisy_txt)
print(f"Cleaned text: {clean_txt}")
# OUTPUT: Cleaned text: I am teacher and  I love teaching.


# =============================================================
# 5) SPLITTING TEXT (re.split)
# =============================================================
# Takes a string, splits it at the match points, and returns a list.

txt_to_split = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.'''

split_list = re.split('\n', txt_to_split)
print(f"Split by newline: {split_list}")
# OUTPUT: 
# Split by newline: ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.']


# =============================================================
# 6) WRITING REGEX PATTERNS
# =============================================================
# Using metacharacters to define complex search criteria.

txt_fruits = 'Apple and banana are fruits. An old cliche says an apple a day...'
txt_dates = 'This regular expression example was made on December 6, 2019 and revised on July 8, 2021'
txt_email = 'Some people write it as email others may write it as Email or E-mail.'

# Square Brackets [] (A set of characters) & OR operator (|)
print("Square brackets:", re.findall(r'[Aa]pple|[Bb]anana', txt_fruits))
# OUTPUT: Square brackets: ['Apple', 'banana', 'apple']

# Escape characters (\d for digits) & One or more times (+)
print("Digits (+):", re.findall(r'\d+', txt_dates))
# OUTPUT: Digits (+): ['6', '2019', '8', '2021']

# Period (.) for any character & Zero or more times (*)
print("Period and (*):", re.findall(r'[a].*', txt_fruits[:27]))
# OUTPUT: Period and (*): ['and banana are fruits']

# Zero or one time (?)
print("Optional (?):", re.findall(r'[Ee]-?mail', txt_email))
# OUTPUT: Optional (?): ['email', 'Email', 'E-mail']

# Quantifiers {} (Specifying exact lengths)
print("Quantifier {4}:", re.findall(r'\d{4}', txt_dates))
# OUTPUT: Quantifier {4}: ['2019', '2021']

# Starts with (^) and Negation ([^])
print("Starts with ^:", re.findall(r'^This', txt_dates))
# OUTPUT: Starts with ^: ['This']

print("Negation [^A-Za-z ]:", re.findall(r'[^A-Za-z ]+', txt_dates))
# OUTPUT: Negation [^A-Za-z ]: ['6,', '2019', '8,', '2021']