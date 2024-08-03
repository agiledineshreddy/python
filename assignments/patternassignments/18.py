'''
Reverse or Inverted Right Angle Triangle using alphabet in descending order.
 D C B A
 D C B
 D C
 D
'''

m=int(input("enter size"))
n=ord('A')#65
for i in range(m,0,-1):
    for j in range(m,m-i,-1):
        print(chr(n+j-1),end=' ')
    print()

