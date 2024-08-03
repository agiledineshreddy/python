
print("'''''")
a=int(input())
b=int(input())
c=int(input())
n=int(input())
x=[]
for s in range(0,a+1):
    for d in range(0,b+1):
        for f in range(0,c+1):
            if(s+d+f)!=n:
                x.append([s,d,f])
            pass
        pass
    pass
print(x)