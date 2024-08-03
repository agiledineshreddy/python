#alias function::
# In Python, an alias function refers to a new name given to an existing function. This is useful when you want to refer to a function with a different name,
#  either to make the code more readable or to simplify references to the function. Aliasing can be done by simply assigning the function to a new variable name.
def add(a,b):
    print(a+b)
abc=add
add(1,1)
abc(2,2)