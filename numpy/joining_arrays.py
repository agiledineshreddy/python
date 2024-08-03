import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

print("Array 1:")
print(array1)
print("Array 2:")
print(array2)

# Concatenate along the first axis (rows)
result_axis0 = np.concatenate((array1, array2), axis=0)
print("Concatenate along the first axis (rows):")
print(result_axis0)

# Concatenate along the second axis (columns)
result_axis1 = np.concatenate((array1, array2), axis=1)
print("Concatenate along the second axis (columns):")
print(result_axis1)
# stack
result_stack = np.stack((array1, array2),axis=1)
print("stack:")
print(result_stack)
# Stack arrays vertically
result_vstack = np.vstack((array1, array2))
print("Vertical stack:")
print(result_vstack)

# Stack arrays horizontally
result_hstack = np.hstack((array1, array2))
print("Horizontal stack:")
print(result_hstack)

# Stack arrays depth
result_dstack = np.dstack((array1, array2))
print("depth stack:")
print(result_dstack)
