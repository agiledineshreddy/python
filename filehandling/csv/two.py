import csv
fp=open('one.csv','r')
data=list(csv.reader(fp))
for i in data[1:]:
    print(i[0])
  