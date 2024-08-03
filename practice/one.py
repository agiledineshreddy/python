n=int(input("enter a number:"))
if n%2!=0:
    print("Weird")
elif n%2==0 and (2<=n<=5 or n>=20):
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
i=[9,4,4,0,9,6,0,4,6,1]
n=0
for j in i:
    n+=j
print(n)