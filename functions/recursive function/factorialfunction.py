# factorial with recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(int(input("enter a number to find factorial")))
print(result)
