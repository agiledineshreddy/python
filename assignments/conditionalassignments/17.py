#Print max numbers in given 3 numbers-using Ternary operator?
a,b,c=float(input()),float(input()),float(input())
z=a if a>b and a>c else(b if b>a and b>c else c)
print("max number is:",z)