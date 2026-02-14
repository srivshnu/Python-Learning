"""
PYTHON datetime MODULE – FULLY EXPLAINED (PROGRAM FILE)
------------------------------------------------------
Key idea:
Computers represent time as numbers, but humans need readable dates.
The datetime module bridges that gap.
"""

# =============================================================
# 1) WHAT IS datetime MODULE?
# =============================================================
# The datetime module helps you work with:
# - Dates (year, month, day)
# - Time (hour, minute, second)
# - Date + Time together
# - Time differences

import datetime

# dir() shows everything available inside a module
print(dir(datetime))

# =============================================================
# 2) datetime.datetime — CURRENT DATE & TIME
# =============================================================
# datetime.now() gives the current local date and time

from datetime import datetime

now = datetime.now()

# Individual components
print("Current datetime:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Unix timestamp
# Number of seconds since 1 Jan 1970 (UTC)
print("Timestamp:", now.timestamp())

# =============================================================
# 3) FORMATTING DATE & TIME (strftime)
# =============================================================
# Computers store datetime in fixed format
# Humans need readable formats

formatted_time = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Formatted time:", formatted_time)

# Common format symbols:
# %d → day
# %m → month
# %Y → year
# %H → hour (24-hour)
# %M → minute
# %S → second

# =============================================================
# 4) STRING → DATETIME (strptime)
# =============================================================
# Converts human-readable date string into datetime object

from datetime import datetime

date_string = "5 December, 2019"
parsed_date = datetime.strptime(date_string, "%d %B, %Y")

print("Date string:", date_string)
print("Parsed datetime:", parsed_date)

# =============================================================
# 5) date OBJECT (ONLY DATE, NO TIME)
# =============================================================
# Used when time is not needed

from datetime import date

# Create specific date
d = date(2020, 1, 1)
print("Specific date:", d)

# Today's date
today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# =============================================================
# 6) time OBJECT (ONLY TIME, NO DATE)
# =============================================================
# Used when date is irrelevant

from datetime import time

# Default time (midnight)
t1 = time()
print("t1 =", t1)

# Hour, minute, second
t2 = time(10, 30, 50)
print("t2 =", t2)

# With microseconds
t3 = time(10, 30, 50, 200555)
print("t3 =", t3)

# =============================================================
# 7) DIFFERENCE BETWEEN TWO DATES (date - date)
# =============================================================

from datetime import date

start = date(2019, 12, 5)
end = date(2020, 1, 1)

diff = end - start
print("Days between dates:", diff)

# =============================================================
# 8) DIFFERENCE BETWEEN TWO DATETIMES
# =============================================================

from datetime import datetime

t1 = datetime(2019, 12, 5, 0, 59, 0)
t2 = datetime(2020, 1, 1, 0, 0, 0)

print("Datetime difference:", t2 - t1)

# =============================================================
# 9) timedelta — DURATION OBJECT
# =============================================================
# Used to represent time duration

from datetime import timedelta

span1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
span2 = timedelta(days=7, hours=5, minutes=3, seconds=30)

result = span1 - span2
print("Timedelta result:", result)

