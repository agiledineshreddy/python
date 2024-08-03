#python has some inbuilt modules, this modules contains some inbuilt functions
#we can find it using help(module name) function
#math module and random module
'''
math module
'''
import math
#help(math)
print(math.sqrt(9))
from math import sqrt
print(sqrt(4))
from math import *
#import * imports all the objects in the module
print(sqrt(7))
'''
random module
'''
from random import *
for i in range(30):
    #random gives values in between 0 to 1
    print(random())
for i in range(20):
    print(randint(1,20))

emp=["rahul","sonia","surya"]
for i in range(9):
    print(choice(emp))