import pyttsx3
toSpeak=pyttsx3.init()
strList=['Hi Friends How are you','Stage 1 Learing python','Stage 2-Mastering Python','Stage 3 Becoming world class programmer']
for i in strList:
    toSpeak.say(i)



toSpeak.runAndWait()

# st=[{'[1,2,3]','3','Hello'}]
# print(type(st))

# print("iNautix Learning Welcomes You"[:1:-2])
# st1 ={'[1,2,3]','3','Hello'}

# st.append(st1)
# print(st)

# i='12344'
# print(i[-2:])
