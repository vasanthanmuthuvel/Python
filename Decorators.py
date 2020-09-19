def addNumber(n):
        return n + 1

def FunctionAsArg(func):
    return func(10)

print(FunctionAsArg(addNumber))



def Prakash(x):
    def Hi_Prakash():
        return x
    return Hi_Prakash()

hello = Prakash
print(hello("How are you"))

def lc(func):
    def dec(x):
        return func(x).lower()
    return dec


@lc
def str(x):
    return x

print(str("Hey Where did you GO"))