'''
PrintRightAngleTrianglewithSequenceofAlphabet-eachrow
 A
 A B
 A B C
 A B C D
'''
n=ord('A')
for i in range(5):
    for j in range(i+1):
        print(chr(n+j),end=' ')
    print()
