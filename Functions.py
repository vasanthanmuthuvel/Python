
# def Vanakkam(msg, msg2, msg1="to session", msg4="Python"):
#     print(msg, msg1, msg2)


# Vanakkam("Hi", msg2="Some Value", msg1="Latest Value")


# def greet(*words):
#     return words[0]


# # f = greet("Welcome", "you", "all", "all")
# # print(f)


# # def greet1(**words):
# #     for key, value in words.items():
# #         print(key, value)

# #     return words.values()


# # f = greet1(s1="Welcome", s2="you", s3="all")
# # print(f)

# Saro = greet
# print(type(Saro))
# print(Saro(1, 2, 3, 4, 5))

# f = "Modified"
# print('after calling', f)

# def sq(x):
#     return x**2


# print(sq(5))

def sumofNumber(n):
    x = 0
    for i in range(n):
        x = x+i

    return x


print(sumofNumber(10))

s=lambda x: x**2
print(s(5))
