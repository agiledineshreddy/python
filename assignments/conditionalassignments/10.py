#Program to print the least/small number in given two numbers?

def small(a,b):

    if a<b:

        return "a is small number "

    elif a>b:

        return "b is small number"

    else:
        return "both are equal numbers"
a,b=int(input("enter a value:")),int(input("enter b value:"))
c=small(a,b)
print(c)

