def jawahar(str):
    return str.lower()


def kk(str):
    return str.upper()


def prakash(str):
    return str.capitalize()

def saro(str):
    x=10
    def saro1(str1):
        return str+str1
    return saro1(" i am here")


def Arun(sai):
    def Arun1():
        print("Summa")
    x = sai("HOW ARE YOU")
    Arun1()
    return lambda x1:x+x1


    
new = Arun(jawahar)
print(new(" Appending new Value"))
print(Arun(kk))
print(Arun(prakash))

print(saro("Hi how are you"))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
x=lambda pair: pair[0]
pairs.sort(key=x)
print(pairs)






