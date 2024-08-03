#Write a program to check if a given number is an Armstrong number or not
num=int(input("enter a number"))
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
    print(num,"is not a arm strong")
    

