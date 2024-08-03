'''
#.PrintRightAngleTrianglewithSequenceofDigits-eachrow
 1
 1 2
 1 2 3
 1 2 3 4
'''
for i in range(5):
    for j in range(i):
        print(j+1,end=' ')
    print()