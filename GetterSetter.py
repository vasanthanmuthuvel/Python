class iNautix:
    def __init__(self, first,last, age):
        self.__age = age
        self.__first = first
        self.__last = last

    def fullname(self):
        return "I am {} {} and {} years old".format(self.__first, self.__last, self.__age)
    

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age
    
    # @property
    # def fullname(self):
    #     return "I am {} {} and i am {} years old".format(self.__first, self.__last, self.__age)
    
    # @fullname.setter
    # def fullname(self, newValue):
    #     first, last, age = newValue.split(' ')
    #     self.__age = age
    #     self.__first = first
    #     self.__last = last
    
    def salary(self):
        return self.__age * 1.5
    

i = iNautix("Vasanthan", "Muthuvel", 45)
i.age=35
print(i.fullname())
print(i.salary())
# i.age=40
# print(i.fullname)
# print(i.salary())

