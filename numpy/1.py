# numpy provides lot of inbuilt functions to deal with matrixs and arrays
import numpy
b=numpy.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]],dtype=int)
a=numpy.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]],dtype=numpy.str_)
print(b)
print(a)
print(a[1:2,::2])
print(type(a.dtype))



print("ffffjgnbfndms,df")
b=numpy.ndarray(shape=(3,3,3,3),dtype=int)
print(b.size)
x=b.shape[0]
y=b.shape[1]
z=b.shape[2]
z1=b.shape[3]
val=2
for i in range(x):
    for j in range(y):
        for k in range(z):
            for l in range(z1):
                b[i][j][k][l]=val
                val+=1

print(b)

