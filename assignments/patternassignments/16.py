'''Print invertedRightAngleTrianglewithsequenceofAlphabets
 A B C D
 A B C
 A B
 A
'''
n=ord('A')
for i in range(5,0,-1):
    for j in range(i):
        print(chr(n+j),end=' ')
    print()