def two(func):
    def inn(a):
        if a < 100 or a > 999:
            return "not a three-digit number"
        else:
            return func(a)
    return inn

@two
def one(i):
    if i % 2 == 0:
        return "even number"
    else:
        return f"{i} is not an even number"

a = one(int(input("Enter a number to find if it is a three-digit even number: ")))
print(a)
b=two(one(int(input("Enter a number to find if it is a three-digit even number: "))))
