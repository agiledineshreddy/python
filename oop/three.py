'''
constructor method:-
To initialize object values we use constructor method.
 constructor method executes automatically at the object creation time.
 syntax:: def __init__(self,a,b,c):
                pass
'''
class account:
    def __init__(self,a,b,c):
        print(a)
    def __init__(self,d,e,f):
        print(d)
    def deposited_amount(self,a):
        print(a)
a1=account(101,'rahul',5000)
a2=account(d=100,e=3,f=4)
a1.deposited_amount(150000)