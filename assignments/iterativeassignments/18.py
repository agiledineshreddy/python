#Program to print Fibonacci number series upto a given number
i=int(input("enter a number"))
j=0
m=1
n=0
while m<=i:
    n=(j+m)
    j=m
    m=n
    print(j)

   


