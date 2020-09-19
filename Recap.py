# #Print 
# print("This is python")
# # check = input("Enter the value ")
# # print(check)

# str = "How are you"


# li = [2, 3, 4, 'python']
# if 'python' in li:
#     print("it is available")
# elif 'python' in li:
#     print("IT is also available")
# else:
#     print("not avaialble")

# str="Python session 234Welcomes you"

# print(str[::-1])

# print(str[4:5:2])

# print(li[1:3])

# print(li[-1][-1])

# li.append("numpy")
# print(li)
# li.insert(1, "pandas")
# print(li)
# print(li.pop())
# li.insert(1, 2.2)
# print(li)
# exp=['python','pandas','numpy','django','flask']
# exp.sort()
# print(exp)
# exp.sort(reverse=True)
# print(exp)

# tup = (2, 3, 4, 5)
# print(tup)

# exp[2] = "API"
# print(exp)
# # tup[2] = 6

# s = {'covid', 'corona', 'economy', 'death', 'covid'}
# print(s)

# users = {'kk': 'kk1', 'pc': 'pc1', 'sai': 'sai1', 'saro': 'saro1'}

# un = input("enter the user name--> ")

# if un in users.keys():
#     print("user available")
#     pwd = input("enter the password--> ")
#     if pwd == users[un]:
#         print("login successful")
#     else:
#         print("login not successful")
# else:
#     print("user not available")

# for item,item1 in users.items():
#     print(item, item1)

# for i in range(10):
#     print(i)

# x = range(10)
# print(x)

# for i in range(0, 10, 2):
#     print(i)

email = input("enter the email address to validate")
if '@' in email:
    listEmail = email.split('@')
    userName = listEmail[0]
    companyName = listEmail[1]
    extension = companyName.split('.')[-1]
    companyName = companyName.replace("." + extension, "")
    for c in userName:
        if not c == '-' or c == '_' or c.isalnum():
            result=False
    print(userName,companyName,extension)
    
else:
    print(False)



