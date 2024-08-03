n=int(input())
j="welcome"
if n%2!=0:
    m=n*3
    c=".|."
    for i in range(1,n+1):
        if i==(n+1)//2:
            print(j.center(m,'_'))
        elif i<(n+1)//2:
            print((c*((2*i)-1)).center(m,'_'))
        else:
            print((c*(2*((n+1)-i))).center(m,'_'))
        
        
else:
    print("enter odd number")