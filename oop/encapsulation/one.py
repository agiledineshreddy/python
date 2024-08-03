# Encapsulation primarily focuses on protecting data and methods from unauthorized access and modification. 
#  It involves restricting direct access to some of an object's components, 
# which can prevent the accidental or intentional misuse of the object's data.

# Encapsulation is implemented using access modifiers to define the visibility of attributes and methods. 
# Common access modifiers include:
#       Public   : Accessible from any other class.
#       Protected: Accessible within its class and by derived class instances.
#       Private  : Accessible only within its own class.
class a():
    __a=10
    _b=5
    c=77
    def aa(self):
        print(a.__a)
class b(a):
    _b=9
    def bb(self):
        print(a._b)
class c():
    print(a.c)
a=a()
a.aa()
b=b()
b.bb()
c=c()
