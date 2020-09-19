try:
    x=x+3
except:
    print("it will execute when try fails")
else:
    print("it will execute when try succeeds")
finally:
    print("always")


#object oriented programming
class Employee:
    """ Employe Details of iNautix """
    def __init__(self, exp, sal):
        self.exp = exp
        self.sal = sal

    def salaryHike(self,hikePercent):
        self.sal=self.sal*hikePercent      

kk = Employee(12,12000)
sai = Employee(10,10000)
suby = Employee(14,14000)
prakash = Employee(13,13000)
saro = Employee(9, 9000)
suby.offer=15000

print(sai.sal)
print(prakash.exp)
print(suby.sal)
suby.salaryHike(1.1)
print(suby.sal)
help(suby)
print(suby.__dict__)


