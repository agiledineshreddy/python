def rat(r,unit,arr):
    if arr is None:
        return -1
    total_foodunitsneeded=r*unit
    available_unit=0
    for i in arr:
        if i is not None:
            available_unit+=i
            
    if total_foodunitsneeded>=available_unit:
        return 0  
    return i+1
r = 7
unit= 2
arr=[2]
# arr=None
food=rat(r,unit,arr)
print(food)