'''how to define static variable and instance variables
'''
class alpha:
        #inside a class outside method
    a=10
    def __init__(self):
        #inside constructor
        alpha.b=11
    def c1(self):
       #inside instance method
       alpha.c=12
       print(alpha.c)
    @classmethod
    def d1(cls):
        #inside class method
        alpha.d=13
        #to update static variable we use cls in classmethod
        cls.a=9
        print(alpha.a)
        print(alpha.d)
    @staticmethod
    def e1():
        print(alpha.f,alpha.a)
aa=alpha()
aa.c1()
#outside a class using class name
alpha.f=14
aa.d1()
aa.e1()

