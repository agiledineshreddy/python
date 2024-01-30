import csv
fp=open('one.csv','r')
data=csv.reader(fp)
print(type(data))
for details in data:
    print(details[0])