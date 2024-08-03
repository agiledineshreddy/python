def high(arr):
     n=len(arr)
     l=0
     m=0
     for i in range(n-1):
         k=(arr[i]**arr[i+1])%((10**9)+7)
         if k>l:
            l=k
            m=i
     return m
    
arr = [5, 4, 3, 4, 1,5,5,5,5,5,5,5,5,5]

result=high(arr)
print(result)