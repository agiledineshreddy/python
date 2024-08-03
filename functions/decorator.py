#decorator function: is a function that modifies the behavior of another function or method. 
#                    Decorators allow you to wrap another function to extend its behavior without explicitly modifying it. 
def ccverification(func):
    def verify(cc):
        if cc <= 249 or cc >= 301:
            print("TO participate in MOTO2 the bike cc must be in between 250CC and 300CC")
        else:
            return func(cc)
    return verify
@ccverification
def moto2(cc):
    print(f"||WELCOME to MOTO2 RACING||with {cc} CC")


moto2(int(input("enter your bike CC:")))

print("''''''")
def out(func):
    def inn(a,b):
        if b==0:
            return "division not possible"
        else:
            return func(a,b)    
    return inn
@out
def nor(a,b):
    return a//b
print(nor(10,0))
print(nor(10,3))
