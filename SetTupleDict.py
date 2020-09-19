# # string="Welcome"

# li=[1,2,2,2,2,23,4]
# print('before change-->',li)
# li[2]=9

# print("after change-->",li)

# for index, item in enumerate(li):
#     print(index,item)

# print(100*'-')

# tup=(1,2,2,2,2,3,['a','b','c'],3)


# print('before tuple change-->',tup)
# # print(tup[1])

# # tup[2]='change'
# # print('before tuplechange-->',tup)
# # print(dir(tup))
# print(100*'-')
# # print(tup.index(['a','b','c']))

# for index, item in enumerate(tup):
#     print(index,item)

# print(100*'-')
# print(li.count(2))
# print(tup.count(3))
# print(100*'-')

# print(dir(tup))

# print(100*'-')
# print(len(li))
# print(len(tup))
# print(100*'-')

# string='Welcome to iNautix Learning!'
# for index,i in enumerate(string):
#     print(index,i)

print(100*'-')
s1={'Arun','Bharathi','Jawahar','KK','Sai','Saro','Vasanthan','KK'}
s2={'ragav','prakash','suby','KK','Sai','Bharathi'}

print(s1)
print(100*'-')

print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.union(s2))

# print(100*'-')
# for i in range(10):
#     print(i)

print(100*'-')
# Dictionaries 
sample={'name':'Arun J,KK','native':'Cuddalore','look':'handsome','name':'cupid,AJ','phone':[9340324398,2098394830]}
print(sample.get('name'))

# sample['name']='Arun Jayaraman'
print(sample)

print(sample['native'])

print(100*'-')

for key,value in sample.items():
    print(key,value)


li=[1,2,2,2,2,23,4]
print(li)

for i in li:
    print(i)


for i in range(len(li)):
    print(i)

