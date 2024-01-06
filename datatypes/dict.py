'''
dict --- group of key value pairs as one entity
            where duplicate key are not allowed, duplicate values are allowed
            no indexing concept 
'''
#create

a={}
print(type(a))
a={'id':101,'name':'rahul','name':'surya'}#duplicate keys not allowed
print(a)
b=[{'id':101,'name':'rahul','sal':4500},
   {'id':102,'name':'puli','sal':500},
   {'id':103,'name':'thar','sal':400}]
for b in b:
    print(b.get('name'))
c= {'id':103,'name':'thar','sal':400}   
print(c['id'])
print(c.get('id'))
print(c.keys())
print(c.items())
print(c.values())
#update
c['loc']=['ban','delhi']

#Read operations
print(c['loc'][1])
print(c.get('loc')[1])          #a.get('key')
print(len(c))                   #len()
#update
c['email']  = "rahul@gmail.com"
print(c)

#print all values

for value in c.values():
    print(value)


#print all emp key and values
#print(emp.items())

for key,value in c.items():
    print(key,":",value)


#delete
    

c.popitem()    
print(c)
c.pop('id')
print(c)
del b['id']
print(b)