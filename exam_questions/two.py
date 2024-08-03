def a(arr, le):
    count = 0
    for i in range(le):
        flag = 0
        for j in range(i+1,le):
            if arr[i] == arr[j]:
                flag = 1
                break
        if flag == 0:
            count += 1 
    return count
arr = [1, 2, 1, 3, 3, 4, 1,9]
le = len(arr)
h = a(arr, le)
print(h) 
