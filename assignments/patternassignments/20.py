'''
 Print Right Angle Triangle with Continuous Character pattern
 A
 BC
 DEF
 GHIJ
 KLMNO
'''
n=int(input("enter number of rows:"))
k=ord('A')
for i in range(1,n):
    for j in range(i):
        print(chr(k),end='')
        k=k+1
    print()