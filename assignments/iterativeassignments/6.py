# Program to print the first 10 even numbers using a while loop?
i=0
j=2
while i<10:
    print(j)
    j=j+2
    i=i+1
#using map function
x=list(filter(lambda a:a%2==0,range(50)))
print(x)


