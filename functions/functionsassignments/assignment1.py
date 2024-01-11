'''
take a data set with names and make first letter to upper case.

'''
emp=[{'id':101,'ename':'rahul'},
     {'id':102,'ename':'surya'},
     {'id':103,'ename':'puli'},
     {'id':104,'ename':'kodi'}
]
c=[]
for em in emp:
    b=em.get(('ename'))
    c.append(b.title())
print(b)
print(c)
