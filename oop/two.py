'''
there are three types of variables and three types of methods
                        instance variable              instance method(if method contains self then it is called as instance method)
                        static variable                 static method()
                        local variable                  class method
'''
'''
self is a pointer pointing to current object to refer class member inside a class '''
class a:
    def deposite_amount(self,amount):
        self.account_bal=amount #instance variable
        print(self.account_bal)
a1=a()
a1.deposite_amount(5000)
print(a1.__dict__)
'''
to invoke a method inside a class we use self
                    outside a class we use object
'''