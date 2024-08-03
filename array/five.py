# reverse of an array without inbuilt functions
import array as arr
a=arr.array('i',[1,2,3,4])
n=len(a)
for i in range(n//2):
    temp=a[i]
    a[i]=a[n-i-1]
    a[n-i-1]=temp
print(a)
