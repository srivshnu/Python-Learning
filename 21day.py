"""
PYTHON CLASSES AND OBJECTS (Day 21)
-----------------------------------
Focus: Understanding object-oriented programming in Python, including creating classes, 
instantiating objects, using constructors, inheritance, and overriding methods.

"""

import math

# =============================================================
# 1) CREATING A CLASS AND AN OBJECT
# =============================================================
# Everything in Python is an object, with its properties and methods.
# A class is an object constructor, or a "blueprint" for creating objects.

class Person:
    pass

print(f"Class: {Person}")
# OUTPUT: Class: <class '__main__.Person'>

p = Person()
print(f"Object: {p}")
# OUTPUT: Object: <__main__.Person object at 0x...>


# =============================================================
# 2) CLASS CONSTRUCTOR (__init__)
# =============================================================
# The __init__ constructor function has a 'self' parameter which is a 
# reference to the current instance of the class.

class PersonWithConstructor:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = PersonWithConstructor('Alice', 'Smith', 30, 'Canada', 'Toronto')
print(f"Firstname: {p.firstname}")
print(f"Age: {p.age}")
# OUTPUT: 
# Firstname: Alice
# Age: 30


# =============================================================
# 3) OBJECT METHODS & DEFAULT VALUES
# =============================================================
# Objects can have methods, which are functions belonging to the object.
# We can also provide default values in the constructor to avoid errors.

class PersonWithMethod:
    def __init__(self, firstname='Alice', lastname='Smith', age=30, country='Canada', city='Toronto'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

p1 = PersonWithMethod()
print(p1.person_info())
# OUTPUT: Alice Smith is 30 years old. He lives in Toronto, Canada.

p1.add_skill('HTML')
p1.add_skill('CSS')
print(f"Skills: {p1.skills}")
# OUTPUT: Skills: ['HTML', 'CSS']


# =============================================================
# 4) INHERITANCE & OVERRIDING
# =============================================================
# Inheritance allows us to define a class that inherits all the methods 
# and properties from a parent class.

class Student(PersonWithMethod):
    def __init__(self, firstname='Alice', lastname='Smith', age=30, country='Canada', city='Toronto', gender='male'):
        self.gender = gender
        # Calling the parent constructor using super()
        super().__init__(firstname, lastname, age, country, city)
        
    def person_info(self):
        # Overriding the parent's person_info method
        gender_pronoun = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender_pronoun} lives in {self.city}, {self.country}.'

s1 = Student('Charlie', 'Brown', 22, 'Canada', 'Toronto', 'male')
s2 = Student('Diana', 'Prince', 24, 'Canada', 'Vancouver', 'female')

print(s1.person_info())
# OUTPUT: Charlie Brown is 22 years old. He lives in Toronto, Canada.

print(s2.person_info())
# OUTPUT: Diana Prince is 24 years old. She lives in Vancouver, Canada.


# =============================================================
# 5) EXERCISES: LEVEL 1 (Statistics Class)
# =============================================================
# Creating a Statistics class to calculate measures of central tendency
# and variability.

class Statistics:
    def __init__(self, data):
        self.data = data
        
    def count(self):
        return len(self.data)
        
    def sum(self):
        return sum(self.data)
        
    def min(self):
        return min(self.data)
        
    def max(self):
        return max(self.data)
        
    def range(self):
        return self.max() - self.min()
        
    def mean(self):
        return round(self.sum() / self.count())
        
    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]
        
    def mode(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1
        max_count = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_count]
        return (modes[0], max_count)
        
    def var(self):
        m = self.sum() / self.count()
        # Note: Calculating population variance to match standard statistical outputs
        return round(sum((x - m) ** 2 for x in self.data) / self.count(), 1)
        
    def std(self):
        return round(math.sqrt(self.var()), 1)
        
    def freq_dist(self):
        freq = {}
        for item in self.data:
            freq[item] = freq.get(item, 0) + 1
        n = self.count()
        # Formatting as a list of tuples: (percentage, value)
        dist = [(round((v/n)*100, 1), k) for k, v in freq.items()]
        dist.sort(reverse=True)
        return dist
        
    def describe(self):
        return f"""Count: {self.count()}
        Sum:  {self.sum()}
        Min:  {self.min()}
        Max:  {self.max()}
        Range:  {self.range()}
        Mean:  {self.mean()}
        Median:  {self.median()}
        Mode:  {self.mode()}
        Variance:  {self.var()}
        Standard Deviation:  {self.std()}
        Frequency Distribution: {self.freq_dist()}"""

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print("\n--- STATISTICS OUTPUT ---")
print(data.describe())
# OUTPUT:
# Count: 25
# Sum:  744
# Min:  24
# ... (matches the requested description format)


# =============================================================
# 6) EXERCISES: LEVEL 2 (PersonAccount Class)
# =============================================================
# Creating a class to manage a person's income and expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
        
    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'desc': description})
        
    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'desc': description})
        
    def total_income(self):
        return sum(item['amount'] for item in self.incomes)
        
    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)
        
    def account_balance(self):
        return self.total_income() - self.total_expense()
        
    def account_info(self):
        return (f"Account Info: {self.firstname} {self.lastname}\n"
                f"Total Income: ${self.total_income()}\n"
                f"Total Expense: ${self.total_expense()}\n"
                f"Current Balance: ${self.account_balance()}")

my_account = PersonAccount("Bob", "Jones")
my_account.add_income(5000, "Salary")
my_account.add_income(200, "Freelance")
my_account.add_expense(1500, "Rent")
my_account.add_expense(300, "Groceries")

print("\n--- PERSON ACCOUNT OUTPUT ---")
print(my_account.account_info())
# OUTPUT:
# Account Info: Bob Jones
# Total Income: $5200
# Total Expense: $1800
# Current Balance: $3400