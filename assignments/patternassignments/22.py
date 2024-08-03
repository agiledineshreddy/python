'''
Print Right Angle Triangle with number are in continuous column pattern
 1
 2 7
 3 8 12
 4 9 1316
 5 10141719
 6 1115182021
'''
n=int(input("enter num of rows:"))
for i in range(n):
    var=i+1
    dec=n-1
    for j in range(i+1):
        print(var,end=' ')
        var=var+dec
        dec=dec-1
        
    print()