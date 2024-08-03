a=int(input("enter your marks:"))
if a<=34:
    print("Fail")
elif a<=50 and a>=35:
    print("C grade")
elif a>=51 and a<=75:
    print("B grade")
elif a>=76 and a<=100:
    print("A grade")
else:
    print("enter correct marks")

print(":::::")
while a<=34:
    print("fail")
    break

while 35<a<=50:
    print("c grade")
    break
while 51<a<=75:
    print("b grade")
    break
while 75<a<=100:
    print("a grade")
    break




