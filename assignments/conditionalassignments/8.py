# Program to print even or odd for a given number from CMD/CLA?
a=int(input("enter a number:"))
if a%2==0:
    print("even number")
else:
    print("odd number")


#using function
def even(a):
    if a%2==0:
        return True
    else:
        return False
a=int(input("enter a value:"))
if even(a):
    print("even number")
else:
    print("odd number")