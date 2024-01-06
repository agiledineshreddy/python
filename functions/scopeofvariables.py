
#scope of variables

#local variable
def loc(m):
    s=10
    print(s,m)
loc(3)
#global variable
m=234
def glo(n):
    print(n,m)
glo(4)
#make local variable as global using global key word
a=100
def f1():
    global b
    c=8
    b=11
    print(a,b,c)
def f2():
    print(a,b)

f1()
f2()
    