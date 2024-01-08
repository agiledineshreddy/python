'''
Print right angle triangle with fixed digit symbol in every row
 1
 2 2
 3 3 3
 4 4 4 4
'''
n=int(input("enter num of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()
    