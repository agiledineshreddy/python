# Data Abstraction in Python::

# Data abstraction in Python that hides complex implementation details while exposing  only essential information 
# and functionalities to users. In Python, we can achieve data abstraction by using abstract classes and 
# abstract classes can be created using abc (abstract base class) module and abstractmethod of abc module.

# Abstraction classes in Python
# Abstract class is a class in which one or more abstract methods are defined.
#  When a method is declared inside the class without its implementation is known as abstract method.

# Abstract Method: In Python, abstract method feature is not a default feature. To create abstract method and 
# abstract classes we have to import the “ABC” and “abstractmethod” classes from abc (Abstract Base Class) library.
#  Abstract method of base class force its child class to write the implementation of the all abstract methods defined in base class. 
# If we do not implement the abstract methods of base class in the child class then our code will give error. 

from abc import ABC, abstractmethod
class main1(ABC):
    @abstractmethod
    def me1(self):
        pass

class con1(main1):
    def me1(self):
        print("con me1")
class con2():
    def me1(self,n):
        print("co1 met")
        n.me1()
class con3(main1):
    def me1(self):
        print("con3 met")

m1=con1()
m1.me1()
m3=con3()
m3.me1()
m2=con2()
m2.me1(m3)