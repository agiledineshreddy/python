#Program to print the reverse of digits of numbers.
i=int(input("enter athree digit number:"))
j=0
m=0
while i>0:
    j=int(i%10)
    m=(m * 10)+j
    i=int(i/10)
print(m)
  
