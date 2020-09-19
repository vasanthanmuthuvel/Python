# x=1
# y=2
# z=3
# n = 2
# result=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i + j + k) != 2:result.append([i, j, k])
            

# print(result)

# x=0
# result = [57,57,-57,57]
# for i in result:
#     if x < i:
#       y = x
#       x = i
#     else:
#       if y>i:y=i 

# print(y)

# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# def score_words(words):
#     score = 0
#     for word in words:
#         num_vowels = 0
#         for letter in word:
#             if is_vowel(letter):
#                 num_vowels += 1
#         if num_vowels % 2 == 0:
#             score += 2
#         else:
#             score += 1
#     return score


# n = int(input())
# words = input().split()
# print(score_words(words))

s = 'Jaw         ahar'
count = 1
found=False
for i in s:
    for j in range(count, len(s)):
        if i == s[j]:
            print(j)
            found = True
            break
    if found==True:
        break
    count = count + 1
    
# str = "Hi GuYs HOW are You 123"

# #expected output
# "hI gUyS how ARE yOU 123"

# ord('A') - - -> 65

def add(x):
    return x * x

y=lambda x:x*x # lambda arguments:expression

print(add(5))

print(y(5))


def createList(x):
    list = []
    for i in range(x):
        list.append(i)
    return list
    
print(createList(10))


l = [lambda x:x for i in range(x)]

print(l(10))



        