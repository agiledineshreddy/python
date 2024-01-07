'''
PrintRightAngleTrianglewithFixedAlphabetSymbol
 A
 B B
 C C C
 D D D D
'''
n=ord('A')
for i in range(5):
    for j in range(i+1):
        print(chr(n+i),end=' ')
    print()