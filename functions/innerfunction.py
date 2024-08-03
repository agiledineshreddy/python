def add(a,b):
    print("sum of a+b is :",a+b)
    def inner(c,d):
        return c-d
    f=inner(6,3)
    print(f)
add(1,1)
#we cannot invoke inner function out of a function
#inner(4,5) is error

def outer():
    print("outer")
    def inner():
        print("inner")

    return inner
x=outer()
a=x()
print(a)