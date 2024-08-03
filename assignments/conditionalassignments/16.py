#Print min numbers in given 3 numbers-using Ternary operator?
a,b,c=int(input()),int(input()),int(input())
z=a if a<b and a<c else(b if b<a and b<c else c)
print("min number is:",z)