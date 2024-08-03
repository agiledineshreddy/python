#hybrid inheritence
class grandparent:
    def m1(self):
        print("grandparent1:m1")
class parent1(grandparent):
    def m2(self):
        print("parent1:m2")
class parent2(grandparent):
    def m3(self):
        print("parent2:m3")
class child(parent1,parent2):
    def m4(self):
        print("child::m4")

ob=child()
ob.m4()
ob.m3()
ob.m2()
ob.m1()