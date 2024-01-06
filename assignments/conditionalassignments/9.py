# Program to print the greatest number in given two numbers?
def great(a,b):
    if a>b:
        return True
    else:
        return False
a,b=int(input("enter a value:")),int(input("enter b value:"))
if great(a,b):
    print("a is greater than b")
else:
    print("b is greater than a")
