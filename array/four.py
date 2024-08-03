# deleting a value ithout using inbuilt functions(pop,del)
import array
a=array.array('i',[1,1,2,23,3])
d=int(input("enter the index number to delete number:"))
if d<0 or d>=len(a):
    print("index is out of range")
else:
    for i in range(d,len(a)-1):
        a[i]=a[i+1]
    a=a[:-1]
    print(a)

# with inbuilt functions
import array
z=array.array('u',['s','s','d'])
y=int(input("enter the index number to delete number:"))
if y<0 or y>=len(z):
    print("index out of range")
else:
    z.pop(y)
    print(z)