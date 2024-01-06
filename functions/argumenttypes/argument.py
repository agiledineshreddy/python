'''____________________________________________________________________________________
arguments are 4 types--
1.positional arguments.
2.actual arguments.
3.default arguments.
4.variable length arguments.

'''
#formal arguments
def add(a,b):
    c=a+b
    print(c)
add(2,4)    
#positional arguments
def sub(a,b):
    c=a-b
    print(c)
sub(30,4)
#named arguments
def mul(a,b):
    c=a*b
    print(c)
mul(b=10,a=2)
#default arguments
def div(a,b=10):
    c=a/b
    print(c)
div(2)
#variable length arguments
def li(a,*b):
    print(a,b)
li(33,21,2,44,53)
