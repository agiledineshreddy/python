s1={}
print(s1)       #{}
print(type(s1)) #<class,dict>
s2={10,}
print(type(s2))#
#why they gave priority for dict?
#most frequently data exachange format is JSON/nothing but python dict.
a={1,2,3,3,4,5,5,6,6,7,'rahul'}
print(a)#there is no order guarrente in set type because no indexing concept.
b=set(range(9))
print(b)
c=set([1,2,3,4])
print(type(c))



#update


c.add(88)#add expecting only one element
print(c)
c.update(range(9))# update expecting iterable object
print(c)#duplicates not allowed
#c.update(104) # error
#print(c)
c.update(a)
print(c)
# c=a.copy()
# print(c)
print(c.union(a)) #union or |
print(c|a)
print(c.difference(a))#difference or -

print(c - a)
print(c & a)#& or intersection
print(c.intersection(a))
print(c.symmetric_difference(a))#symmetric_difference or ^
print(a^c)


#delete

print(c)
c.pop()
print(c)
c.remove(4) #if specified element is not there shows error
print(c)
c.discard(4)#if specified element is not there no error
print(c)
c.clear()
print(c)
