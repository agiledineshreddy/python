# overloading in the classical sense, using optional arguments
class calculator:
    def calculator(self,*args):
        for a in args:
            print(f"{a},hi ")
   
a=calculator()
a.calculator('dini','om')