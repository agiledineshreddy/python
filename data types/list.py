#crud mechanism for list type
#create
a=[2,3,"serr"]
b=list(range(9))
c="hi surya".split()
d=eval(input("enter list"))
e=["surya","puli","puli","thar",["thar"],"surya","surya"]
g=["surya","puli","puli","thar","surya","surya"]
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#read ///
print(a)
print(a[2])#index
print(a[2:])#slice operator
for x in a:#for loop
    print(x) 
    
i=0
while i<=len(b)-1:#while loop
    print(b[i])
    i=i+1
a.reverse()#reverse
print(a)

print(e.count('puli'))#count returns no of occurencies of a specified element
print(e.count('thar'))
print(e.count('surya'))

f=e.copy()#copy
print(f)

g.sort()#sort
print(g)

print(len(g))

print(g.index("thar")) #it gives what is the position of the value


#update list////
a.append(223)#append adds element at end of the list
print(a)

a.insert(1,333)#insert method inserts elements at specified position
print(a)
a.extend(g)#extend() method adds the specified list elements to end of current list  
print(a)

#delete list///

a.remove(223)#removes an element from list
print(a)

g.pop(2)#pop
print(g)

a.clear()#clear it delete all the elements in the list
print(a)
print (g)
del g#it gives error because list deketed successfully
#print(g)



