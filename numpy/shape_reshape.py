# shape: Attribute that describes the current dimensions of the array.
# Provides information about the structure of the array.
import numpy as np

arr = np.array([1, 2, 3,4, 5, 6])
print(arr.shape) 


reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# reshape: Method to change the dimensions of the array without altering its data.
# Returns a new array with the specified shape.
# The total number of elements must remain the same before and after reshaping.