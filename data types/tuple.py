####tuple is read only version of list
## once tuple object is created we cannot modify it
a=("jhgfd","jhgfdf","jhgfdf")
print(a)
b=("sarrr",)#to create a tuple with only one element we have to add a coma after thde item other wise python will not recognize it as a tuple
print(type(b))
bb=("sarerr")
print(type(bb))
c=tuple(range(8))
print(c)