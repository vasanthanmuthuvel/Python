#Inheritance in Python
class languages:
    def __init__(self, student_name, language_name,exp,activity):
        self.student_name = student_name
        self.language_name = language_name
        self.activity=activity
        self.department = "QA"
        self.exp=exp
        print("inside main class")
    
    def baselang(self):
        print("Basic is known language")

class eca:
    def activities(self):
        print("i know "+self.activity)

class student(languages,eca):
    def specilizedlang(self):
        print("My name is " + self.student_name + " i am specilized in " + self.language_name)

s = student("Suby Kurian", "Java",14,"Swimming")
s.baselang()
s.specilizedlang()
s.activities()
print(s.department)

k = student("KK", "Groovy",12,"Cricket")
k.baselang()
k.specilizedlang()
print(k.department)

S = student("Sai", "Python",8,"Badmitton")
S.baselang()
S.specilizedlang()
print(S.department)

print(k.exp)

    