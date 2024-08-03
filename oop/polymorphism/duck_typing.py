#  If multiple classes have methods with the same names and signatures (i.e., they take the same parameters),
#  you can use duck typing to treat instances of these classes interchangeably.
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

# Instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using duck typing to handle both instances
animal_speak(dog)  # Output: Woof!
animal_speak(cat)  # Output: Meow!
