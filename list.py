#1.Rotate a List Right by n Positions to right or left
'''
def rotate(l1,n,RorL):
    if(n<=len(l1)):
        if(len(l1)==1) :
            return l1
        else:
            if(RorL==True):#right
                return l1[len(l1)-n-1:len(l1)]+l1[0:len(l1)-n-1]
            else:
                return l1[len(l1)-n:len(l1)]+l1[0:len(l1)-n]
    else:
        return []
    
x=[1,43,5,-33,'xy']
print(rotate(x,2,False))
print(rotate(x,2,True))

'''
#Print all sublists and Sum of all the sublists
'''
def printSublist(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)+1 ):
            print(l[i:j])

def SumOfSublists(l):
    for i in range(len(l)):
        sum=0
        for j in range(i+1,len(l)+1):
            l1=l[i:j]
            for i in range(len(l1)):
                sum=sum+l1[i]
            print(sum)




li=[1,4,3]
printSublist(li)
SumOfSublists(li)

'''
# Given an integer array nums, return all unique triplets (a, b, c) such that: a + b + c = 0

'''
def TriSublists(l):
    for i in range(len(l)-2):     
        sub = l[i:i+3]            
        if sum(sub) == 0:         
            print(sub)

lx = [55, 3, 4, 21]
TriSublists(lx)

'''
'''
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,third,*rest=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(rest)
print(first)
print(second)
print(third)

'''
#Find the range of the ages (max minus min)
'''
def age_range(ages):
    return max(ages) - min(ages)

ages = [12, 18, 25, 30, 16, 40]
print("Range of ages:", age_range(ages))

'''
list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

for i in range (len(list)):
    print((list[i]).upper())

for i in range(5):
    list.pop() 
print(list)

