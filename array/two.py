# how to create new array from existing array
import array
a = array.array('i',[1,2,2,])
b = array.array(a.typecode,( x for x in a))
print(b)