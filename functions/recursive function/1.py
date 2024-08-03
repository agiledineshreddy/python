#recursive function : a function calling it self
# def greet():
#     print("hello")
#     greet()
# greet()

#  python by default set a limit of 1000 for recursive we can set limit by sys.setrecursionalimit(2000)

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print("hello", i)
    greet()
greet()



