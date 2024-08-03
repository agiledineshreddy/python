from csv import *
fp=open('one.csv','r')
data=list(reader(fp))
max_sal = 0
max_name = ""
for i in data[1:]:
    salary = int(i[2])
    if salary > max_sal:
        max_sal = salary
        max_name = i[1]
print(max_name)