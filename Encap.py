class BNYM:
    def __init__(self,firstname,lastname,age):
         self.__firstname = firstname
         self.__lastname = lastname
         self.__age = age

    def setFirstName(self, firstname):
        self.__firstname = firstname
    
    def getFirstName(self):
        return self.__firstname
    
    def setLastName(self, lastname):
        self.__lastname = lastname
    
    def getLastName(self):
        return self.__lastname

    def setAge(self, age):
        self.__age = age
    
    def getAge(self):
        return self.__age
        
    def fullname(self):
        return "My Name is {} {} and i am {} years of Old".format(self.__firstname, self.__lastname, self.__age)


B = BNYM("Krishnakumar","Dhaksnamurthy",34)
B.setFirstName("Vasanthan")
B.setLastName("Muthuvel")
B.setAge("37")
B.age=35
print(B.getAge())
print(B.age)