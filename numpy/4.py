# Initialization functions in NumPy are used to create arrays with predefined values or patterns


# np.zeros(shape,   dtype=float, order='C')
#           |                |         |
#         (2,4)              int      by default row major
#                           si         row major:'c'
#                           float       colomn major:'F'
# 
# Contiguous Memory: Elements stored next to each other in memory.
# Row-major (C-contiguous): Rows stored adjacently.
# Column-major (F-contiguous): Columns stored adjacently.
# order='C'
# Creates an array filled with zeros.
import numpy as np
a=np.zeros((2,3),dtype=int)
print(a)

# np.ones(shape, dtype=float, order='C')
# Creates an array filled with ones.
b=np.ones((3,3),dtype=int)
print(b)

# np.full(shape, fill_value, dtype=None, order='C')
# Creates an array filled with a specified value (fill_value).
c=np.full((4,4),2,dtype=float)
print(c)


# np.eye(N, Mdtype=float)
# Creates a 2D array (matrix) with ones on the diagonal and zeros elsewhere (identity matrix).
# m is optional by default nxn
d=np.eye(4,dtype=int)
print(d)