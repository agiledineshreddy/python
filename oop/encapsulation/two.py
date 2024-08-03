class a:
    def _aa(self):
        return "giig"
    def __bb(self):
        return "hi"
class b(a):
    def bb(self):
        b=a._aa(self)
        print(b)

b=b()
b.bb()
