# create arrays from existing data
#  converts input such as lists, tuples, or other arrays into NumPy arrays.


# from asarray
# asarray(input,           dtype,    order)
#           |                |         |
#         list              int      by default row major
#         tuple              si         row major:'c'
#       any combination     float       colomn major:'F'
# 
# Contiguous Memory: Elements stored next to each other in memory.
# Row-major (C-contiguous): Rows stored adjacently.
# Column-major (F-contiguous): Columns stored adjacently.
# order='C'
import numpy as np
a=[2,2,3,4,4]
b=[6,5,3,6,7]
e=np.asarray((a,b),dtype=int,order='C')
print(e)
print(e.flags)
for i in np.nditer(e):
    print(i)
# order='F'
e=np.asarray((a,b),dtype=int,order='F')
print(e)
print(e.flags)
for i in np.nditer(e):
    print(i)



 
# frombuffer
# np.frombuffer() is a NumPy function that creates an array from an object that can be interpreted as a buffer, such as bytes or a bytearray. 
# for representing string as a byte we use b as prefix
s=b"welcome"
# frombuffer(buffer,dtype,count,offset)
k=np.frombuffer(s,dtype='S1',count=-1,offset=0)
print(k)
k=np.frombuffer(s,dtype='S1',count=3,offset=2)
print(k)


# fromiter
# np.fromiter() is a NumPy function that creates a new one-dimensional array from an iterable object.
# a=np.fromiter(iterable data,dtype=("int","float","S1"), count=-1)
#                   |
#                  list
#                   tuple
#                   set
#                   dict
d={'a':'2','b':'3','c':'3'}
m=np.fromiter(d,dtype="S1",count=-1)
print(m)
items = [(k, str(v)) for k, v in d.items()]
dtype=[('key','U1'),('val','U21')]
n=np.fromiter(items,dtype=dtype,count=-1)
print(n)
print(n.shape)
print(n.ndim)
print(n.size)


# to add only keys into ndarray

d={'a':'2','b':'3','c':'3'}
m=np.fromiter(d.keys(),dtype="S1",count=-1)
print("keys:",m)
items = [(k, str(v)) for k, v in d.items()]
dtype=[('key','U1'),('val','U21')]
n=np.fromiter(items,dtype=dtype,count=-1)
print(n)
print(n.shape)
print(n.ndim)
print(n.size)
# to add only values into ndarray

d={'a':'2','b':'3','c':'3'}
m=np.fromiter(d.keys(),dtype="S1",count=-1)
print("keys:",m)

n=np.fromiter((str(v) for v in d.values()),dtype='S4',count=-1)
print("values",n)
print(n.shape)
print(n.ndim)
print(n.size)

# to add both key and values using fromiter 1d
p=[{'a':'2','b':'3','c':'3'},{'a':'2','b':'3','c':'3'}]
q=np.fromiter(d,dtype="S1",count=-1)
print(q)
items = [(k, str(v)) for dic in p for k, v in dic.items()]
dtype=[('key','U1'),('val','U21')]
n=np.fromiter(items,dtype=dtype,count=-1)
print(n)
print(n.shape)
print(n.ndim)
print(n.size)


# 2d

# import numpy as np

# # List of dictionaries
# p = [{'a': '2', 'b': '3', 'c': '3'}, {'a': '2', 'b': '3', 'c': '3'}]

# # Extract keys
# keys = list(p[0].keys())

# # Create arrays for keys and values
# keys_array = np.array(keys)
# values_array = np.array([[dic[key] for key in keys] for dic in p], dtype='<U21')

# # Combine keys and values into a 2D array
# # Here, we stack keys as a separate column to maintain a 2D structure
# combined_array = np.vstack([keys_array, values_array])

# # Print the combined 2D array
# print("Combined 2D array:\n", combined_array)

# # Print array details
# print("Shape:", combined_array.shape)
# print("Number of dimensions:", combined_array.ndim)
# print("Total number of elements:", combined_array.size)
# print("Data type of elements:", combined_array.dtype)
