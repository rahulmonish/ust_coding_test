para= input("Enter the paragraph")
while(para.count(".")<4):
    para2=input("The paragraph is incomplete. Please continue.")
    para= para+para2
print("The paragraph is: ",para)
str1=" "
str2=" "
str="UST Global specializes in Healthcare, Retail and consumer goods, banking and financial services, telecom, media and technology, insurance, transportation and logistics and manufacturing and utilities."
for i in range(int(len(para)/2)):
    str1= str1 + para[i]

'''for i in range(int(len(para)/2), len(para)):
    str2= para[i]
    print(str2)
'''
para= str1 + str
print("Paragraph after updation is : " , para)

vowels=0
vowels+= para.count("a")

vowels+= para.count("e")

vowels+= para.count("i")

vowels+= para.count("o")

vowels+= para.count("u")

digit=0
upper=0
lower=0
special=0
for i in para:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i!="." or i!=" ":
        special+=1

print("no of vowels : ", vowels)

print("no of digit : ", digit)

print("no of upper : ", upper)

print("no of lower : ", lower)

print("no of special : ", special)

new_str=""
sentence= para.split(".")
s= sentence[0]
t= sentence[len(sentence)-1]
sentence[0]=t
sentence[len(sentence)-1]=s
final=""
for i in sentence:
    final= final+i
print("After swapping : ",final)

