import numpy as np
a=np.array([[1,1,3,3],[2,2,3,4]],dtype=int)
print(a)
print(a[0:1,0:1])
import numpy as np
a=np.array([1,1,3,3,2,2,3,4],dtype=int)
print(a)
print(a.shape)
print(a[0:1])
print(a[2::])
print(a[-1::-1])

print()
b=np.array([[1,1,3,3],[2,2,3,4]],dtype=int)
print(b.shape)
print(b[1,0:2])

c=np.array([[[1,1,3,3],[2,2,3,4]],[[1,1,3,3],[2,1,3,4]]],dtype=int)
print(c.shape)
print(c)
print(c[0:2,1,])
print(c[1,1,-1::-1])