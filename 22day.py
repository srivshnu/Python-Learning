import requests
from bs4 import BeautifulSoup

# =============================================================
# 1) WHAT IS WEB SCRAPING & INSTALLATION
# =============================================================
# Web scraping is the process of extracting data from websites and 
# storing it locally or in a database.
# 
# Required packages:
# $ pip install requests
# $ pip install beautifulsoup4


# =============================================================
# 2) FETCHING DATA FROM A URL
# =============================================================
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Use the requests get method to fetch the data from the URL
response = requests.get(url)

# Check the status code (200 means successful)
status = response.status_code
print(f"Status Code: {status}") 


# =============================================================
# 3) PARSING HTML WITH BEAUTIFULSOUP
# =============================================================
# Get all the content from the website
content = response.content 

# BeautifulSoup parses the content
soup = BeautifulSoup(content, 'html.parser') 

# Extracting specific parts of the HTML
print(f"Title tag: {soup.title}") 
print(f"Title text: {soup.title.get_text()}") 

print(soup.body.get_text()[:500]) # Print the first 500 characters of the body text 


# =============================================================
# 4) EXTRACTING SPECIFIC ELEMENTS (e.g., Tables)
# =============================================================
# Targeting a table with a specific attribute (cellpadding='3')
# Note: The UCI website structure might have changed since the course was written.
tables = soup.find_all('table', {'cellpadding': '3'})

if tables:
    table = tables[0] # The result is a list, take the first table
    
    # Find the first row ('tr') and all its columns ('td')
    for td in table.find('tr').find_all('td'):
        print(td.text)
else:
    print("Could not find the specified table. The website HTML structure may have changed.")