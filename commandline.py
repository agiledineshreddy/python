# Command-line arguments are parameters passed to a program at the time of execution.
# for that we need to import sys module
# we need to give the parrameters beside the file name 
# it will take file name is also as a parameter
# output:PS D:\backend\python> py commandline.py 2 2 3 3 4
# ['commandline.py', '2', '2', '3', '3', '4']
# it consider all the paramenters as strings
import sys
print(sys.argv)
print(type(sys.argv),"hi")
for i in range(1,len(sys.argv)):
    print(i)
    print(type(i))
