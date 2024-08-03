# Program to print 15 to 10 numbers using for loop and while loop?
for i in range(15,9,-1):
    print(i)
k=15
while k<=9:
    print(k)
    k=k-1

#using filter function
x=list(filter(lambda a:a,range(15,9,-1)))
print(x)