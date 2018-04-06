
num=[12,6,48,37,88,31,54,11,60,122,105,88,122,155,105]

num.sort()

n= input("enter the number")

for i in range(len(num)):
    if(num[i]==n):
        print("position : ", i)

