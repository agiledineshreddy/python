#multi level inheritence
class grandparent:
    def __init__(self,a):
        self.a=a
        print(self.a)
    def m1(self):
        print("grand: m1 ")
class parent(grandparent):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
        print(a+b)
    def m2(self):
        print("parent: m2")
class child(parent):
    def m3(self):
        print("parent: m3")
ob=child(10,4)
ob.m3()
ob.m2()
ob.m1()