'''
Print Right Angle Triangle with Alphabet are in continuous column pattern
 A
 B E
 C F H
 D G I J
 '''
n=int(input("enter num of rows:"))

for i in range(n):
    m=ord('A')
    r=m+i
    dec=n-1
    for j in range(i+1):
        print(chr(r),end=' ')
        r=r+dec
        dec=dec-1
    print()