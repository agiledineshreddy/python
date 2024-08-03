import numpy as np

# Original array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Convert using astype()
arr_float_astype = arr.astype(np.float64)

# Convert using np.array()
arr_float_array = np.array(arr, dtype=np.float64)

# Convert using view() (not recommended for general use)
# Only use if you understand the memory implications
# arr_float_view = arr.view(np.float)

print("Original array:", arr, "dtype:", arr.dtype)
print("Converted array (astype):", arr_float_astype, "dtype:", arr_float_astype.dtype)
print("Converted array (array):", arr_float_array, "dtype:", arr_float_array.dtype)
# print("Converted array (view):", arr_float_view, "dtype:", arr_float_view.dtype)
