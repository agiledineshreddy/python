#decorator
def ccverification(func):
    
    def verify(cc):
        if cc <= 249 or cc >= 301:
            print("TO participate in MOTO2 the bike cc must be in between 250CC and 300CC")
        else:
            return func(cc)
    return verify

@ccverification
def moto2(cc):
    print("||WELCOME to MOTO2 RACING||",cc)


moto2(int(input("enter your bike CC:")))

        
