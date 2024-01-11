# Program to calculate the sum of the first 10 natural numbers using for Loop-for loop and While loop?
n=0
for i in range(1,11):

    n=n+i
print(n)
d=0
m=0
while d<=10:
    m=m+d
    d=d+1
print(m)

#using lambda
from functools import reduce
na=list(filter(lambda a:a<=10,range(100)))
print(na)
su=reduce(lambda a,b:a+b,na)
print(su)


       