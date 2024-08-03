#   Use composition when your system involves complex relationships and
#  you want to avoid deep inheritance hierarchies.

#  When you don't want or need to inherit all the methods and properties of a base class,
#  composition provides a more flexible and selective approach to assembling the functionality you need.
class salaries:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def salary(self):
        return (self.pay*12)+self.bonus
class employees:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def employee(self):
        total_salary=self.salary.salary()
        print(f"{self.name} with salary {total_salary} at the age {self.age}")
a=salaries(1200,2000)
b=employees('om',23,a)
b.employee()

# with inheritence
class sal:
     def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
     def sala(self):
        return (self.pay*12)+self.bonus

class emp(sal):
    def __init__(self,name,age,pay, bonus):
        super().__init__(pay, bonus)
        self.name=name
        self.age=age
    def empd(self):
        total_salary=self.sala()
        print(f"{self.name} with salary {total_salary} at the age {self.age}")
e=emp('puli',24,1200,3000)
e.empd()


    



    
    