class base:
    def __init__(self,y1):
        print("hey i am in base class")
        self.y1=y1
    
    def intstance1(self,y):
        print(y)

class sub1(base):
    def __init__(self):
        print("hey i am in sub1 class")
        super().__init__()

    def intstance1(self,y):
        print(y)
        super().intstance1("Hi")

class sub2(sub1):
    def __init__(self):
        print("hey i am in sub2 class")
        super().__init__()


    def intstance1(self,y):
        print(y)
        super().intstance1("Hey")


s = sub2()
s.intstance1("Cool")
