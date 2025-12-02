#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
'''
age = [22, 19, 24, 25, 26, 24, 25, 24]
ageSet=set(age)
print(ageSet)
if (len(ageSet)>len(age)):
    print("BIGGER : ",ageSet)
elif (len(ageSet)<len(age)):
    print('BIGGER :',age)
else:
    print('equal')

'''
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.list the letters in all the words too.

s='I am a teacher and I love to inspire and teach people'
words=s.split()
st=set(words)
print(words)
print(st)

for word in words:
    letters=list(word)
    print(letters)
    print('unique letters:',set(letters))
               
