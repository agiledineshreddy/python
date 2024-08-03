#heirachical inheritence
class parent1:
    def m1(self):
        print("parent1 m1")
class parent2:
    def m2(self):
        print("parent2 m2")
class child(parent1,parent2):
    def m3(self):
        print("child m3")
ob=child()
ob.m3()
ob.m2()
ob.m1()