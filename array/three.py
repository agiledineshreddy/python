# creating a array using user input and search for an element index
import array
a=array.array('i',[])
n=int(input("enter the size of the array:"))
for i in range(n):
    x=int(input(f"enter the value of {i+1} element:"))
    a.append(x)
print(a)
 

c=input("do you want to search for index of a value(Y/N)::")
if c == 'Y' or c=='y':
    y=int(input("enter the number to search:"))
    k=0
    for b in a:
        if y==b:
            print("the index number is ",k)
            break
            k+=1
            
        else:
            exit
           

    try:
        print(a.index(y))
    except:
        print("value not found")
