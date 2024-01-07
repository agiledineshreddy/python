#.Program to print the first 5 odd numbers using a for loop?

count=0
for i in range(1,100):
    if i%2!=0:
        print(i)
        count=count+1
        if count==5:
            break



    