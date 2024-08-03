
# Inheritance allows a new class (derived or child class) to inherit the attributes and methods of
#  an existing class (base or parent class). This promotes code reusability and
#  establishes a hierarchical relationship between classes.
class account:
    savings_min_bal=500
    current_min_bal=5000
    def __init__(self,type,bal):
        account.bal=bal
        account.type=type
        print(account.type,"account opened successfully")
class savings(account):
    def deposite(self,amount):
        self.amount=amount
        account.bal=self.amount+account.bal-account.savings_min_bal
        print(self.amount,"amount deposited successfully")
    def get_bal(self):
        print("total balance",account.bal)
        
class current(account):
    def deposite(self,amount):
        self.amount=amount
        account.bal=self.amount+account.bal
    def get_bal(self):
        account.bal=self.bal-account.current_min_bal
        return account.bal
ob=savings("savings",25000)
ob.get_bal()
ob.deposite(19)
ob.get_bal()
ob.deposite(9999)
ob.get_bal()
