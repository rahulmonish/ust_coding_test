dict={}

for i in range(20):
    s= input("enter the name")
    dict[s]= int(input("enter the age"))
    if(dict[s]<=10):
        print(s," is a child")
    elif(dict[s]>10 and dict[s]<=18):
        print(s," is a youth")
    elif(dict[s]>18 and dict[s]<60):
        print(s," is a middle aged")
    else:
        print(s," is old")

print("the family members are : ",dict)


