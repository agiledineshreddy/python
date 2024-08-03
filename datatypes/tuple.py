####tuple is read only version of list
## once tuple object is created we cannot modify it
aa=()
print(type(aa))
a=("jhgfd","jhgfdf","jhgfdf",[9])
print(a)
b=("sarrr",)#to create a tuple with only one element we have to add a coma after the item other wise python will not recognize it as a tuple
print(type(b))
bb=("sarerr")
print(type(bb))
c=tuple(range(8))
print(c)
d=(1,2,3,4,5,[66,99,88],True,{6,7,8,'rahul',88})
print(d)#order guarrentee, indexing concept is there.
print(d[3])#iterate tuple object  or    ss tupe elements

#reading tuple elements using loop concepts
i=0
while i <= len(d)-1:
    print(d[i])
    i=i+1

for ds in d:
    print(ds)


#there is no update in tuple concept
    
#d[0]=999
#print(d)# tuple object does not support item assignment


#how to sort list
#how to sort tuple
#there is no sort and reverse concept in tuple
#to sort we need to use sorted inbuilt function
names=['Rahul','Sonia','Priyanka','Modi','Balaji']
enames=('Rahul','Sonia','priyanka','modi')



names.sort()
print(names)

x=tuple(sorted(enames))
print(x)
