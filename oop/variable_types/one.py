'''
there are two types of variables 1.instance
                                    2.static / class
'''
class test:
    branch="banglore"    #static variables / class variable
    def __init__(self,name,amount):
        self.min_bal=400
        self.name=name      #instance variable
        self.amount=amount
        print(self.name,"account opened successfully")
    def amount_deposite(self,b):
        self.b=b
        self.amount=self.amount+self.b-c.min_bal 
        return"amount deposited successfully"
    def bal(self):
        print("balance amount::",self.amount)
c=test("rahul",5000)
c.min_bal=300       #we can declare variable using object
print(c.amount_deposite(101))
c.bal()
print(c.__dict__)