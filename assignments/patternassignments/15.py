'''
.Pythonprogramtoprintahollowsquarepatternofstar
 * * * * *
 *       *
 *       *
 *       *
 * * * * *
'''
n=int(input("enter size of square:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i==n-1 or j==0 or j== n-1: 
            print("p",end=' ')
        else:
            print(' ',end=' ')
    print()