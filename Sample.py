# # for i in range(1,11): print(i)

# # if True: 
# #     print('Pa"ss')


# print(30*'#')

# x,y,z=5,10,4

# print(x)
# print(y)
# print(100*'-')
# print('hey\n'*5)
# print(100*'-')
# x,y,z=input('Enter the numbers').split(',')
# print("x=",x)
# print("y=",y)
# print("z=",z)
# print(100*'-')

#List

Training=[1,2,3,4,5,6,7]

print(Training[0])
print(100*'-')
for item in Training:
    print(item)


print(100*'-')
print(Training)
print(100*'-')



print(100*'-')
print(Training[0:4])
print(100*'-')
print(Training[::-1])
print(100*'-')


str="Welcome"
print(str[0:4])
print(str[-2:-4])
print(str[-4:-2])
print(100*'-')
sq=['Mike','Steve',23,2000,[1,2,3,4,5]]

for item in sq:
    print(item)


print(100*'-')

sq1=sq[4]
print(sq1[3])
print(100*'-')

print(sq[4][3])
print(100*'-')

# result=[]
num=[1,2,3,4,5,6]
# for item in num:
#     result.append(item**2)


print([item**2 for item in num][::-1])

print(100*'-')

i=10
print(['greater' if i==10 else 'lesser'])
print(100*'-')

for item in Training:
    if item%2!=0:
        print(item)


print(100*'-')
print([item for item in Training if item%2!=0])
print(100*'-')

duplicates=[2,2,4,5,5,6,7]

print(set(duplicates))

print(100*'-')
duplicates[1]='changed'
print(duplicates)

duplicates.remove(5)
print(duplicates)


