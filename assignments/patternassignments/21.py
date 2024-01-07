'''
Print Right Angle Triangle with numbers continuous pattern
 1
 2 3
 4 5 6
 7 8 9 10
 11 12 13 14
'''
n=int(input("enter num of rows:"))
k=1
for i in range(1,n):
    for j in range(i):
        print(k,end=' ')
        k=k+1
    print()

