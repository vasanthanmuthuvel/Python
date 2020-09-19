# lambda parameter_list: expression

def x(y):
    print(y)

x("Hello Suby")

z = x
z("Hello Again Suby")

i = lambda y: y

v = i("Hello How are you")
print(v)

print([x for x in range(10)])

print(list(map(lambda j:j+10, [1, 2, 3, 4, 5])))

print(list(filter(lambda j: (j % 2 != 0), [1, 2, 3, 4, 5])))

gang = [(13, 'Suby'), (10, 'KK'), (9, 'Saro')]

gang.append((12, 'Prakash'))

print(gang[1][1])

exp=lambda EXP:EXP[0]
gang.sort(key=exp)
print(gang)