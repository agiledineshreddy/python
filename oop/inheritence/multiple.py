#multiple inheritence
class parent:
    def m1(self):
        print("parent m1")
class child1(parent):
    def m2(self):
        print("child:1 m2")
class child2(parent):
    def m3(self):
        print("child:3 m3")

ob=child1()
ob.m2()
ob1=child2()
ob1.m3()
