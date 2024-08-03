# Initialization functions in NumPy are used to create arrays with predefined values or patterns


# numpy.arange([start, ]stop, [step, ]dtype=None)
# it generate values with step difference and with in the range
# arange doesnt support str_
# it is same like range function in python but it returns ndarray not a list
import numpy as np
a=np.arange(4,90,3,dtype=int)
b=np.arange(4,90,3,dtype=float)
c=np.arange(1,10)
c_bool=c%2==0
r=np.arange(6)
print(r)
print(a)
print(b)
print(c)
print(c_bool)

# function returns evenly spaced numbers over a specified interval.
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
d,step=np.linspace(1,20,num=30,endpoint=True,retstep=True,dtype=None)
print(d)
print(d.dtype)
print(step)

# logspace
# np.logspace() generates numbers that are evenly spaced on a logarithmic scale. It is used when you need values spread exponentially.
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# formula  for a given base b and a number x:
# log𝑏(𝑥)=𝑦
# means b^y=x

l=np.logspace(0, 6, num=10, endpoint=True, base=10.0, dtype=None)
print(l)

# The np.logspace(0, 6, num=10) function call calculates and generates 10 values that are evenly spaced on a logarithmic scale between 10^0 to 10^6 
 
