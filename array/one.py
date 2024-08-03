# using list : They can store elements of different types and are very flexible.

my_list = [1, 2, 3, 4, 5]
print(my_list)

 # Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 20, 3, 4, 5, 6]

# Removing elements
my_list.pop(2)
print(my_list)  

# using array module:: This module provides a more efficient array storage than lists if all elements are of the same type.
import array
var = array.array('i',[2,2,3,8,4])
for i in var:
    print(i)
   

# using numpy::NumPy is a powerful library for numerical computing in Python. It provides support for arrays and matrices, along with many mathematical functions to operate on these arrays.


import numpy as np

my_numpy_array = np.array([1, 2, 3, 4, 5])
print(my_numpy_array)
# Adding elements (need to use np.append, numpy arrays are fixed-size)
my_numpy_array = np.append(my_numpy_array, 6)
print(my_numpy_array)  # Output: [ 1 20  3  4  5  6]
# Removing elements (need to use slicing or fancy indexing)
my_numpy_array = np.delete(my_numpy_array, 2)
print(my_numpy_array)  # Output: [ 1 20  4  5  6]