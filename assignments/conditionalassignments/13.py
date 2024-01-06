#Program to print given 3 numbers in descending order?
def asc(a,b,c):
    if a<b and a<c and b<c:
        return a,b,c
    elif b<a and b<c and c<a:
        return b,c,a
    elif c<b and c<a and a<b :
        return c,a,b
    elif a<b and a<c and c<b:
        return a,c,b
    elif b<a and b<c and a<c:
        return b,a,c
    elif  c<a and c<b and b<a:
        return c,b,a
result=asc(a=int(input()),b=int(input()),c=int(input()))
print ("descending order:",result)
