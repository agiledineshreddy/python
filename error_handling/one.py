class div:
    def __init__(self,a):
        self.a=a
class div2(div):
    def div2(self,b):
        self.b=b
        try:
            print(self.a/self.b)

        except:
            print("ded")
d=div2(int(input("enter a number")))
d.div2(int(input("enter another num to devide")))

'''KJHGFGHJHG
'''
# how to create custom/user defined errors
class InsuffientFundsError(Exception):
    def __init__(self, arg):
        self.msg = arg


amount = int(input("Enter Amount::::"))

if amount > 5000:
    raise InsuffientFundsError("Less Account Balance")
else:
    print("Transaction Success!")


