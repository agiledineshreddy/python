print(dir())
#for every module python interpritetor add some special properties at the time of execution,for internal use.
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(__file__)
#__file__ gives the path of the file
def che():
    if __name__ == "__main__":
        print("true")
    else:
        print("false")

che()
#__name__ property gives __main__ when we execute any module individually.
#by using __name__ we can identify the file is executing directly or by module. 
 
