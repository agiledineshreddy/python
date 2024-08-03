# Polymorphism means the ability to take multiple forms. for instance if the parent class has a method named abc 
# then the child class also can have same name method having its own parameters and variables.
# in programing , polymorphism refers to a function having the same name but being used in different ways and scenarios.
# IT HAS SOME KEY CONCEPTS:
#                             method over riding
#                             method over loading
#                             operator over loadig
#                             duck typing

class a:
    def add(self,a,b):
         print(self+a+b)
a=a()
a.add(1,2,3) 