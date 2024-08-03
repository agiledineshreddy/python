i=int(input("enter a number"))
for num in range(1,i):
    num_digits = len(str(num))
    temp = num
    m = 0
    while temp > 0:
        digit = temp % 10
        m =m +( digit **num_digits)
        temp = int(temp/10)

    if m == num:
        print(num, "is an Armstrong number.")
    else:
        pass
    