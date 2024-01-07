'''
Print the string in right angled triangle pattern
 p
 py
 pyt
 pyth
 pytho
 Python
'''
n=input("enter a string:")
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end='')
    print()
