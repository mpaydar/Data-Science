import re

text="555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
i=0
# for index in range(len(text)):
#     # substring+=text[index]
#     # print(substring)
#     if re.match('r [A-Za-z]',text):
#         print(text[index])
substring1=[]
substring2=[]




numberList=[]
def listNumbers(list_review):
    for i in list_review:
        if i!='':
            numberList.append(i)
    return numberList




character_dictionary=[]
def NameList(review):
    for i in review:
        white_space=i.count(' ')
        # print(white_space)
        if white_space==0:
            character_dictionary.append(i)
        if white_space==1:
            character_dictionary.append(i)
        elif white_space==2:
            character_dictionary.append(i)
        elif white_space==3:
            character_dictionary.append(i)
    return character_dictionary


NameCheckOut=[]
def checkLastOrMiddleName(review):
    r="Dr. Moe Bayat"
    regex="[A-Za-z]*\s.+"
    for i in range(len(review)):
         r=re.search(regex,review[i])
         if r!=None:
            NameCheckOut.append(True)
         else:
            NameCheckOut.append(False)
    print(NameCheckOut ,'\n')    








title1=[]
def checkTitle(review):
    regex="^[A-Za-z]*\."
    for i in range(len(review)):
        r=re.search(regex,review[i])
        if r!=None:
            title1.append(True)
        else:
            title1.append(False)
    print(title1 ,'\n')




r1=re.findall("\d*",text)
print(len(r1))
result_n=listNumbers(r1)
print("This is the list of all numbers within the given text",result_n)
title=False
list=[]
dictionary={}
t=0
LastName=False
blank=0
NotBlank=0
r2=re.findall("[A-Za-z]*\.?",text)
# print("This is the list of all the names within the given text",r2)
substring=""
for i in r2:
    if i != '':
        substring+=i
        if substring=='Dr.' or substring=='Rev.':
            t=1
            substring+=' '
            # print(substring)
        # elif blank==1:
        #     LastName=True
        else:
            substring+=' '
        blank=0       
    else:
        blank+=1
        white_space=substring.count(' ')
        if 1<blank:
            # print(substring)
            list.append(substring)
            if t==1 and white_space==2:
                t=0               
            substring=''


final_list=[]
for i in list:
    if i!='':
        i=i.rstrip()
        final_list.append(i)
result=NameList(final_list)
print("This are the names listed in the given string:",result)
checkTitle(final_list)
checkLastOrMiddleName(final_list)






txt2="<title>+++BREAKING NEWS+++<title>"
#  Writing “<.+>” :
# It means a regex that start with < followed by any character one or more times , which follows with closing >
# . : is any character
# + : One more occurances



# Correct Regex
x = re.findall("<[a-z]+>", txt2)
print("#6 solution",x)



# Writing  “[^0-9=+*()]+ is wrong because:
# [] : grouping of set character within it
# Start with digits ranging 0-9 follow by =+*() one or more time
txt2="(5-3)^2=5^2-2*5*3+3^2"

# Correct Regex
x = re.findall("\(\d\-\d\)\^\d.*", txt2)
print("#7 solution",x)









