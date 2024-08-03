def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    return inner


inner1 = outer()
inner1()
inner1()


