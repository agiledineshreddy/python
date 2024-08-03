# Definition: When a subclass provides a specific implementation for a method that is already defined in its superclass.
# Benefit: Allows a subclass to alter the behavior of a method inherited from a superclass.
class animal:
    def sound(self):
        print("default sound")
class dog(animal):
    pass
class cat(animal):
    def sound(self):
        print("alter sound")
# we are over riding tbhe default sound method of super class from subclass by altering the method
a=animal()
b=dog()
c=cat()
a.sound()
b.sound()
c.sound()

