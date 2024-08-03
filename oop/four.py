class bank:
    bank_name="BOI"
    def __init__(self,a):
        self.a=a
        print(bank.bank_name,"BANK:", self.a,"account opened successfully")
    def deposit_amount(self,b):
        self.b=b
        self.acc_bal=0
        self.acc_bal=self.acc_bal+self.b
        print(self.b,"amount deposited","in::",bank.bank_name)
    def total_bal(self):
        print("total balance",self.acc_bal)

a1=bank(input("enter ur name:"))

a1.deposit_amount(int(input("enter amount to deposit::")))
a1.total_bal()

