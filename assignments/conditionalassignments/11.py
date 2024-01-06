#Program to print the greatest number in given three numbers?
def three(a,b,c):
   
    if a>b and a>c:
        return "a is greater than b and c"
    elif b>a and b>c:
        return "b is greater than a and c"
    elif c>a and c>b:
        return "c is greater than a and b"
    else:
        return "all are equal"
    
result=three(a=int(input("enter a value:")),b=int(input("enter b value:")),c=int(input("enter c value:")))
print(result)

