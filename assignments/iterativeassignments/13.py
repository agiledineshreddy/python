#Program to print a multiplication table of 6 using a for loop.
count=0
j=0
for i in range(1,100):
    j=6*i
    print("6 *",i,"=",j)
    count=count+1
    if count==10:
        break
