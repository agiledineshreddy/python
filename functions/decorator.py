#decorator
def ccverification(func):
    def verify(cc):
        if cc <= 249 or cc >= 301:
            print("TO participate in MOTO2 the bike cc must be in between 250CC and 300CC")
        else:
            return func(cc+1)
    return verify
@ccverification
def moto2(cc):
    print("||WELCOME to MOTO2 RACING||")


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
