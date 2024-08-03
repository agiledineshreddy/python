# copy: A copy is a new array that owns its own data. Changes to the copy do not affect the original array and vice versa.
import numpy as np
a=np.array([12,2,3,4,44])
c=np.copy(a)
print(a)
print(c)
c[2]=99
print(c)
print(c.dtype)
print(a)
# view :A view is a new array object that looks at the same data of the original array. Modifying the view will affect the original array and vice versa.


arr = np.array([1, 2, 3])
arr_view = arr.view()
arr_view[0] = 10
print("view",arr)      # Output: [10 2 3]
print(arr_view) # Output: [10 2 3]
