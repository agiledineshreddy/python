# Program to check if a number is divisible by 7 or not?
a=int(input("enter a number to check if it is divisable by 7 or not:"))
if a%7==0:
    print("divisable by 7")
else:
    print("not divisable by 7")
#ternary operator
b=int(input("enter a number to check if it is divisable by 7 or not:"))   
m="divisable by 7" if a%7==0 else "not divisable by 7"
print(m)


