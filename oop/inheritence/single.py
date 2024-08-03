#single inheritence
class parent:
    def m1(self):
        print("parrent m1")
class child(parent):
    def m2(self):
        print("child m2")
ob=child()
ob.m2()
ob.m1()